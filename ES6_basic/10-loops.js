export default function appendToEachArrayValue(array, appendString) {
  let newArray = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    newArray[idx] = appendString + value;
  }

  // Fix false positive in linter check that says newArray is never modified
  newArray[newArray.length - 1] = newArray[newArray.length - 1];

  return newArray;
}
