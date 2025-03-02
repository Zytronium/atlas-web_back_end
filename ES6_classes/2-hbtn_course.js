export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }

    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }

    if (!(Array.isArray(students) && students.every(student => typeof student === 'string'))) {
      throw new TypeError('students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }
}