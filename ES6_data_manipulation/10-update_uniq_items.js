export default function updateUniqueItems(groceryListMap) {
  if (!(groceryListMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  groceryListMap.forEach((value, key) => {
    if (value === 1) {
      groceryListMap.set(key, 100);
    }
  });
}
