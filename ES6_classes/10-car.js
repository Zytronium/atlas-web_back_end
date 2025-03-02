export default class car {
  constructor(brand, motor, color) {
    // private attributes
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Returns a new object of the same class
  cloneCar() {
    return new this.constructor();
  }
}
