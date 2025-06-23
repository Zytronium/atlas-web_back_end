#!/usr/bin/node
process.stdout.write("Welcome to Holberton School, what is your name?\n");

process.stdin.on('end', () => {
  console.log("This important software is now closing");
});

process.stdin.on("data", function (data) {
  process.stdout.write(`Your name is: ${data}`);
  process.stdin.pause();
});
