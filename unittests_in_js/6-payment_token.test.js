#!/usr/bin/node
const { expect } = require('chai');
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const spy = sinon.spy(console, 'log');

describe('sendPaymentRequestToApi', function () {
    beforeEach(function () {
        spy.resetHistory();
    });
    afterEach(function () {
        expect(spy.calledOnce).to.be.true;
    });

    it('should call Utils.calculateNumber with ("SUM", 100, 20)', function () {
        sendPaymentRequestToApi(100, 20);

        expect(spy.calledWithExactly("The total is: 120")).to.be.true;
    });
    it('should call Utils.calculateNumber with ("SUM", 10, 10)', function () {
        sendPaymentRequestToApi(10, 10);

        expect(spy.calledWithExactly("The total is: 20")).to.be.true;

        spy.restore();
    });
});
