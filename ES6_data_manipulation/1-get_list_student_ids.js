export default function getListStudentIds(objects) {
  // return empty array if objects is not an array
  if (!Array.isArray(objects)) {
    return [];
  }

  // return an array of all ids of matching students in the given array of objects
  return objects.map((student) => student.id);
}
