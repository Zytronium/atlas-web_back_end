#!/usr/bin/node
const { expect } = require('chai');
const calculateNumber = require("./2-calcul_chai.js");

describe('calculateNumber', function () {
    it('should return -2 for ("SUBTRACT", 1, 3)', function () {
        expect(calculateNumber("SUBTRACT", 1, 3)).to.equal(-2);
    });

    it('should return -2 for ("SUBTRACT", 1.2, 3)', function () {
        expect(calculateNumber("SUBTRACT", 1.2, 3)).to.equal(-2);
    });

    it('should return 2 for ("SUBTRACT", 1.6, 0)', function () {
        expect(calculateNumber("SUBTRACT", 1.6, 0)).to.equal(2);
    });

    it('should return 4 for ("SUM", 1.2, 3.1)', function () {
        expect(calculateNumber("SUM", 1.2, 3.1)).to.equal(4);
    });

    it('should return 2 for ("SUM", 1.6, 0)', function () {
        expect(calculateNumber("SUM", 1.6, 0)).to.equal(2);
    });

    it('should return 2 for ("DIVIDE", 3.9, 2.4)', function () {
        expect(calculateNumber("DIVIDE", 3.9, 2.4)).to.equal(2);
    });

    it('should return 6 for ("DIVIDE", 30.4, 5)', function () {
        expect(calculateNumber("DIVIDE", 30.4, 5)).to.equal(6);
    });

    it('should return 2.25 for ("DIVIDE", 9, 4)', function () {
        expect(calculateNumber("DIVIDE", 9, 4)).to.equal(2.25);
    });

    it('should return -2.25 for ("DIVIDE", 9.3, -4)', function () {
        expect(calculateNumber("DIVIDE", 9.3, -4)).to.equal(-2.25);
    });

    it('should return 0 for ("DIVIDE", 0, 2.1)', function () {
        expect(calculateNumber("DIVIDE", 0, 2.1)).to.equal(0);
    });

    it('should return "Error" for ("DIVIDE", 1, 0)', function () {
        expect(calculateNumber("DIVIDE", 1, 0)).to.equal("Error");
    });

    it('should return "Error" for ("DIVIDE", 1.5, 0.2)', function () {
        expect(calculateNumber("DIVIDE", 1.5, 0.2)).to.equal("Error");
    });

    it('should return "Error" for ("DIVIDE", 1, -0)', function () {
        expect(calculateNumber("DIVIDE", 1, -0)).to.equal("Error");
    });

    it('should return "Error" for ("DIVIDE", 1, -0.5)', function () {
        expect(calculateNumber("DIVIDE", 1, -0.5)).to.equal("Error");
    });

    it('should return "Error" for ("Invalid", 1, 5)', function () {
        expect(calculateNumber("Invalid", 1, 5)).to.equal("Error");
    });
});
