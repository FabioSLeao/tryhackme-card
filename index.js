const express = require('express')
const {spawn} = require('child_process');
const xml = require('xml');

const app = express()
const port = 5000
app.get('/card', (req, res) => {
 
 var dataToSend;
 var doc;
 const id = req.query.id
 
 // spawn new child process to call the python script
 const python = spawn('python', ['script1.py', id]);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  dataToSend = data.toString();
 });
 // in close event we are sure that stream from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 console.log(dataToSend)
 res.set('Content-Type', 'image/svg+xml; charset=utf-8')
 res.send(dataToSend)
 });
 
})
app.listen(process.env.PORT || port, () => console.log(`Example app listening on port 
${port}!`))