export default function updateUniqueItems(groceryListMap) {
  groceryListMap.forEach((value, key) => {
    if (value === 1) {
      groceryListMap.set(key, 100);
    }
  });
}
