const express = require('express');

const app = express();

app.get('/', (req,res) => {
    res.send("Hello World from the other side!");
})

module.exports = app;
