export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const grade = newGrades.find((grd) => grd.studentId === student.id);
    return {
      ...student, grade: grade ? grade.grade : 'N/A',
    };
  });
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
