export default function hasValuesFromArray(set, array) {
  let result = true;
  array.forEach((item) => {
    if (!set.has(item)) {
      result = false;
    }
  });
  return result;
}
