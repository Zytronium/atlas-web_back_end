export default function appendToEachArrayValue(array, appendString) {
  for (const value of array) {
    let idx = array.indexOf(value);
    array[idx] = appendString + value;
  }

  return array;
}
