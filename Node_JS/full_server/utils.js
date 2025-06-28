#!/usr/bin/node

import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'UTF8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter(line => line.trim() !== '');
      const fieldGroups = {};

      for (const line of students) {
        const [firstname, , , field] = line.split(',');

        if (!fieldGroups[field]) {
          fieldGroups[field] = [];
        }

        fieldGroups[field].push(firstname);
      }

      resolve(fieldGroups);
    });
  });
}
