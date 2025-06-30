#!/usr/bin/node
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./4-payment.js');

describe('sendPaymentRequestToApi', function () {
    it('should call Utils.calculateNumber with (SUM, 100, 20)', function () {
        const stub = sinon.stub(Utils, 'calculateNumber').callsFake(() => 10);
        const spy = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);

        expect(stub.calledOnce).to.be.true;
        expect(stub.calledWithExactly('SUM', 100, 20)).to.be.true;
        expect(spy.calledWithExactly("The total is: 10")).to.be.true;

        spy.restore()
        stub.restore();
    });
});