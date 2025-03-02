export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments: (allEmployees) => Object.keys(allEmployees).length,
  };
}
