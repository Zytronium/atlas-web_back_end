#!/usr/bin/node
process.stdout.write("Welcome to Holberton School, what is your name?\n");
process.stdout.write("Your name is: ");
process.stdin.on("data", function () {
  process.stdin.write("This important software is now closing\n");
  process.exit();
});
