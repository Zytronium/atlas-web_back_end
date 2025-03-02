export default class Airport {
  constructor(name, code) {
    // type validation
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }

    // private attributes
    this._name = name;
    this._code = code;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
