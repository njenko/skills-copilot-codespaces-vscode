// Create web server
const express = require('express');
const app = express();
const port = 3000;
const fs = require('fs');
const path = require('path');

// Create route for GET request
app.get('/comments', (req, res) => {
  // Get the comments from the file
  fs.readFile(path.join(__dirname, 'comments.json'), 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).send('An error occurred');
      return;
    }

    // Send the comments as a response
    res.send(data);
  });
});

// Start the server on port 3000
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});