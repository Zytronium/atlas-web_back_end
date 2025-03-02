export default class Building {
  constructor(sqft) {
    // Type validation
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    // Private attribute
    this._sqft = sqft;
    // Enforce all subclasses have implemented evacuationWarningMessage()
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error("Class extending Building must override evacuationWarningMessage")
    }

  }

  // Getter for sqft
  get sqft() {
    return this._sqft;
  }

  // Setter for sqft
  set sqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    this._sqft = sqft;
  }

}
