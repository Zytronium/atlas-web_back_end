#!/usr/bin/node
const assert = require('assert');
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', function () {
    it('should return -2 for ("SUBTRACT", 1, 3)', function () {
        assert.strictEqual(calculateNumber("SUBTRACT", 1, 3), -2);
    });

    it('should return -2 for ("SUBTRACT", 1.2, 3)', function () {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.2, 3), -2);
    });

    it('should return 2 for ("SUBTRACT", 1.6, 0)', function () {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.6, 0), 2);
    });

    it('should return 4 for ("SUM", 1.2, 3.1)', function () {
        assert.strictEqual(calculateNumber("SUM", 1.2, 3.1), 4);
    });

    it('should return 2 for ("SUM", 1.6, 0)', function () {
        assert.strictEqual(calculateNumber("SUM", 1.6, 0), 2);
    });

    it('should return 2 for ("DIVIDE", 3.9, 2.4)', function () {
        assert.strictEqual(calculateNumber("DIVIDE",  3.9, 2.4), 2);
    });

    it('should return 6 for ("DIVIDE", 30.4, 5)', function () {
        assert.strictEqual(calculateNumber("DIVIDE",  30.4, 5), 6);
    });

    it('should return 2.25 for ("DIVIDE", 9, 4)', function () {
        assert.strictEqual(calculateNumber("DIVIDE",  9, 4), 2.25);
    });

    it('should return -2.25 for ("DIVIDE", 9.3, -4)', function () {
        assert.strictEqual(calculateNumber("DIVIDE",  9.3, -4), -2.25);
    });

    it('should return 0 for ("DIVIDE", 0, 2.1)', function () {
        assert.strictEqual(calculateNumber("DIVIDE", 0, 2.1), 0);
    });

    it('should return "Error" for ("DIVIDE", 1, 0)', function () {
        assert.strictEqual(calculateNumber("DIVIDE", 1, 0), "Error");
    });

    it('should return "Error" for ("DIVIDE", 1.5, 0.2)', function () {
        assert.strictEqual(calculateNumber("DIVIDE", 1.5, 0.2), "Error");
    });

    it('should return "Error" for ("DIVIDE", 1, -0)', function () {
        assert.strictEqual(calculateNumber("DIVIDE", 1, -0), "Error");
    });

    it('should return "Error" for ("DIVIDE", 1, -0.5)', function () {
        assert.strictEqual(calculateNumber("DIVIDE", 1, -0.5), "Error");
    });
});
