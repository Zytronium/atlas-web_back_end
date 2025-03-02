import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);

    // type validation
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }

    // private attributes
    this._floors = floors;
  }

  // Getters
  get floors() {
    return this._floors;
  }

  get sqft() {
    return this._sqft;
  }

  // override method for evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
