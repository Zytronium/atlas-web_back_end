#!/usr/bin/node
const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi', function () {
    it('should call Utils.calculateNumber with (SUM, 100, 20)', function () {
        const spy = sinon.spy(Utils, 'calculateNumber');

        sendPaymentRequestToApi(100, 20);

        expect(spy.calledOnce).to.be.true;
        expect(spy.calledWithExactly('SUM', 100, 20)).to.be.true;

        spy.restore();
    });
});