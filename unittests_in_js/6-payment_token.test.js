#!/usr/bin/node
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
    it('should resolve with correct response when success is true', (done) => {
        getPaymentTokenFromAPI(true)
          .then((response) => {
              expect(response).to.be.an('object');
              expect(response).to.have.property('data', 'Successful response from the API');
              done();
          })
          .catch((err) => done(err));
    });

    it('should return undefined when success is false', (done) => {
        Promise.resolve(getPaymentTokenFromAPI(false))
          .then((response) => {
              expect(response).to.be.undefined;
              done();
          })
          .catch(done);
    });
});
