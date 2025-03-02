export default class Currency {
  // constructors
  constructor(code, name) {
    // type validation
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }

    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    // private attributes
    this._code = code;
    this._name = name;
  }

  // getters and setters

  // code
  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = code;
  }

  // name
  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
  }

  // methods

  // Displays the currency name and code. (i.e. "Dollars ($)")
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
