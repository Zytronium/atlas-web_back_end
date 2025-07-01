const express = require('express');
const app = express();
const PORT = 7865

// GET / route
app.get('/', function (req, res) {
  return res.send("Welcome to the payment system");
});

// GET /cart/:id route
app.get('/cart/:id', function (req, res) {
  if (isNaN(req.params.id)) {
    return res.status(404).send("Not Found");
  }
  const id = parseInt(req.params.id);
  return res.send(`Payment methods for cart ${id}`);
});

app.listen(PORT, function () {
  console.log(`API available on localhost port ${PORT}`);
});
