const { expect } = require("chai");
const { ethers } = require("hardhat");
const ResearchData = require("../models/ResearchData");

describe("DeSci Basic Tests", function () {
  let desci, desciToken;

  beforeEach(async function () {
    const MedToken = await ethers.getContractFactory("MedToken");
    desciToken = await MedToken.deploy();
    await desciToken.deployed();

    const DeSci = await ethers.getContractFactory("DeSci");
    desci = await DeSci.deploy(desciToken.address);
    await desci.deployed();
  });

  it("should encrypt research data", function () {
    const data = new ResearchData("research1", "biomed data", "agent1");
    data.encrypt();
    expect(data.encrypted).to.be.true;
  });

  it("should deploy contracts", async function () {
    expect(desciToken.address).to.not.be.undefined;
    expect(desci.address).to.not.be.undefined;
  });

  it("should submit and verify research", async function () {
    await desci.submitResearch("biomed data", "receipt");
    await desci.verifyResearch(0);
    const record = await desci.getResearch(0);
    expect(record.verified).to.be.true;
  });
});
