export default class HolbertonClass {
  constructor(size, location) {
    // I'm not going to keep doing type validation unless it tells me do. I've gotten that down by now

    // private attributes
    this._size = size;
    this._location = location;
  }

  // to number (valueOf()) override to return size as a number
  valueOf() {
    return this._size;
  }

  // to string override to return location as a string
  toString() {
    return this._location;
  }
}
