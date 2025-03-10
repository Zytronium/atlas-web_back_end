export default function updateStudentGradeByCity(students, city, newGrades) {
  const newList = students.filter((student) => student.location === city);
  const updateIds = newGrades.map((grade) => grade.studentId);

  newList.forEach((student) => {
    if (updateIds.includes(student.id)) {
      student.grade = newGrades.find((grade) => grade.studentId === student.id).grade;
    } else {
      student.grade = 'N/A';
    }
  });

  return newList;
}

/*
* params:
* students - list of students (from getListStudents)
* city - a city (String)
* newGrades - array of “grade” objects
*
* newGrades format: array of objects, as seen below
* [
*   {
      studentId: 31,
      grade: 78,
    },
* ]
*
* Final grade should be "N/A" if the student doesn't have a grade in newGrades.
*
* returns:
* array of students for a given city with their new grade
*
* Must use filter() and map() combined.
*
* expected output for main.js:
*
[
  {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
    grade: 86
  },
  { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 97 }
]
[
  {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
    grade: 'N/A'
  },
  { id: 5, firstName: 'Serena', location: 'San Francisco', grade: 97 }
]
*
*/
