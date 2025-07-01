#!/usr/bin/node
const request = require('request');
const { expect } = require('chai');

describe('Index page', () => {
  const baseURL = 'http://localhost:7865';

  it('should return status code 200', (done) => {
    request.get(baseURL, (err, res) => {
      expect(res.statusCode).to.equal(200);
      done(err);
    });
  });

  it('should return the correct response body', (done) => {
    request.get(baseURL, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done(err);
    });
  });

  it('should not return error 500', (done) => {
    request.get(baseURL, (err, res) => {
      expect(res.statusCode).to.not.equal(500);
      done(err);
    });
  });
});