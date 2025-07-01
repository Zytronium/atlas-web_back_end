const express = require('express');
const app = express();
const PORT = 7865

// GET / route
app.get('/', function (req, res) {
  return res.send("Welcome to the payment system");
})

app.listen(PORT, function () {
  console.log(`API available on localhost port ${PORT}`);
});
