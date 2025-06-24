#!/usr/bin/node
const express = require('express');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter(line => line.trim() !== '');

      let output = `Number of students: ${students.length}\n`;

      const fields = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      for (const [field, names] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

const dbFile = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  if (!dbFile) {
    res.status(500).type('text/plain').send('Database filename not provided');
    return;
  }
  try {
    const report = await countStudents(dbFile);
    res.type('text/plain').send(`This is the list of our students\n${report}`);
  } catch (err) {
    res.status(500).type('text/plain').send(err.message);
  }
});

app.listen(1245);

module.exports = app;
