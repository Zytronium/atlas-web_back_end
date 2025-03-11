export default function cleanSet(set, startString) {
  let cleanString = '';

  // Return empty string if startString is empty or set is no all strings
  if (startString === '') {
    return '';
  }
  for (const item of set) {
    if (typeof item !== 'string') {
      return '';
    }
  }

  // Find all strings in the set that start with the startString
  set.forEach((item) => {
    if (item.startsWith(startString)) {
      cleanString += `-${item.replace(startString, '')}`;
    }
  });

  return cleanString.replace('-', '');
}
