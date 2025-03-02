import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    // type validation
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }

    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency');
    }

    // private attributes
    this._amount = amount;
    this._currency = currency;
  }

  // getters and setters

  // Amount
  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = amount;
  }

  // Currency
  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency');
    }
    this._currency = currency;
  }

  // Displays the currency amount in the following format: Amount Name (Code)
  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  // Converts a value from one currency to another using the given conversion rate
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
