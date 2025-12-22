const express = require('express');
const rateLimit = require('express-rate-limit');
const { PythonShell } = require('python-shell');
require('dotenv').config();
const config = require('../config/app');
const { startP2PNode } = require('../integration/p2p');
const ResearchData = require('../models/ResearchData');
const { sendResearchDataToBioSync, getCoLabResults } = require('../bridges/bioSyncBridge');

const app = express();
app.use(express.json());

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: config.rateLimit,
  message: 'Too many requests, please try again later.',
});
app.use(limiter);

const researchDataStore = {};

app.post('/research/verify', async (req, res) => {
  try {
    const { researchId, biomedData } = req.body;
    if (!researchId || !biomedData) return res.status(400).json({ error: 'Research ID and biomed data required' });

    const options = {
      mode: 'text',
      pythonPath: 'python3',
      pythonOptions: ['-u'],
      scriptPath: './integration',
      args: [biomedData]
    };

    PythonShell.run('ai.py', options, (err, results) => {
      if (err) {
        console.error('Verification error:', err);
        return res.status(500).json({ error: 'Verification failed' });
      }
      const receipt = `Reproducibility receipt: ${results[0]}`;
      const researchData = new ResearchData(researchId, biomedData);
      researchData.addReproducibilityReceipt(receipt);
      researchDataStore[researchId] = researchData;
      res.json({ receipt });
    });
  } catch (error) {
    console.error('Server error:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/research/federate', async (req, res) => {
  try {
    const { researchId } = req.body;
    if (!researchId || !researchDataStore[researchId]) return res.status(400).json({ error: 'Valid research ID required' });

    const data = researchDataStore[researchId];
    await sendResearchDataToBioSync(researchId, data.toJSON());
    res.json({ status: 'Federated to BioSync' });
  } catch (error) {
    res.status(500).json({ error: 'Federation failed' });
  }
});

app.get('/research/colab/:researchId', async (req, res) => {
  try {
    const { researchId } = req.params;
    const results = await getCoLabResults(researchId);
    res.json({ coLabResults: results });
  } catch (error) {
    res.status(500).json({ error: 'Co-lab fetch failed' });
  }
});

startP2PNode().catch(console.error);

app.listen(config.port, () => console.log(`DeSci API listening on port ${config.port}`));
