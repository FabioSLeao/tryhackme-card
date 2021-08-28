const express = require('express')
const {spawn} = require('child_process');


const app = express()
const port = 5000

app.get('/card', (req, res) => {

    var dataToSend;
    const id = req.query.id
    const python = spawn('python', ['script1.py', id])
    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...')
        dataToSend = data.toString();
    })
    python.on('close', (code) => {
        console.log('child process close all stdio with code ${code}')
        console.log(dataToSend)
        res.set('Content-Type', 'image/svg+xml; charset=utf-8')
        res.send(dataToSend)
    })

})
app.listen(process.env.PORT || port, () => console.log('Example app listening on port ${port}!'))