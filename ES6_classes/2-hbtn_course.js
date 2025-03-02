export default class HolbertonCourse {
  // constructors
  constructor(name, length, students) {
    // type validation
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }

    if (!(Array.isArray(students) && students.every((student) => typeof student === 'string'))) {
      throw new TypeError('Students must be an array of strings');
    }

    // private attributes
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // getters and setters

  // Name
  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;
  }

  // Length
  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length;
  }

  // Students
  get students() {
    return this._students;
  }

  set students(students) {
    if (!(Array.isArray(students) && students.every((student) => typeof student === 'string'))) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = students;
  }
}
