# DeSci API Documentation

## Overview
DeSci API supports research networks, verifiable scientific computation, decentralized biomed data layers, reproducibility receipts, open-data knowledge graphs, federation of research agents, human-machine co-labs, and bridges to Aethera BioSync for post-operative care research.

## Endpoints

### POST /research/verify
Verifies scientific computation for reproducibility.

- URL: `/research/verify`
- Method: POST
- Request Body: `{ "researchId": "string", "biomedData": "string" }`
- Response Success: `{ "receipt": "Reproducibility receipt" }`
- Possible Errors: 400 (bad input), 500 (server errors), 429 (rate limited)

### POST /research/federate
Federates research data to Aethera BioSync.

- URL: `/research/federate`
- Method: POST
- Request Body: `{ "researchId": "string" }`
- Response Success: `{ "status": "Federated to BioSync" }`
- Possible Errors: 400 (bad input), 500 (server errors)

### GET /research/colab/:researchId
Retrieves co-lab results from BioSync.

- URL: `/research/colab/:researchId`
- Method: GET
- Response Success: `{ "coLabResults": "data" }`
- Possible Errors: 500 (server errors)

## Setup
- Start server: `node api/index.js`
- Use Postman or curl for testing.

## Security
- Encrypted data transmission.
- Rate limited requests.
- Audit logs for reproducibility.
