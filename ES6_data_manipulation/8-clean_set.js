export default function cleanSet(set, startString) {
  let cleanString = '';

  if (startString === '' || startString === undefined) {
    return '';
  }

  set.forEach((item) => {
    if (item.startsWith(startString)) {
      cleanString += `-${item.replace(startString, '')}`;
    }
  });

  return cleanString.replace('-', '');
}
