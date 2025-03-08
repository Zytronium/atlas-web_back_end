export default function getStudentIdsSum(students) {
  return students.reduce((sum, student) => { return student.id + sum; }, 0);
}
