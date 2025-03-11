export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const int8DataView = new DataView(buffer);

  // check if adding the value is not possible due to invalid position
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // set the Int8 value at the specified position
  int8DataView.setInt8(position, value);
  return int8DataView;
}

/*
*
* returns: new ArrayBuffer with an Int8 value at a specific position
*
* params:
* length - number
* position - number
* value - number
*/
