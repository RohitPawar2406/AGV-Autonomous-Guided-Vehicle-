const express = require('express')
const path = require('path')
const http=require('http')
const socketio = require('socket.io')

const port =process.env.PORT || 3000
const app = express()
const server = http.createServer(app)
const io = socketio(server)
app.use(express.json({limit:'500tb'}))
const publicDirectoryPath = path.join(__dirname,'../public')
app.use(express.static(publicDirectoryPath))

let images_live=''
app.all('/',(req,res)=>{
    images_live = req.body.Image
    console.log(typeof(images_live))
    io.emit('Sending',images_live)
    console.log('==============================')
    res.send('hello')
})  

let count =0
let socket=''
io.on('connection', (socket)=>{
    console.log('New WebSocket Connection!!')

    socket.emit('Sending',images_live)

    socket.on('input', input=>{
        //console.log('VtAxis='+input);
    })

    /* Testing Simple Data
    socket.emit('Count-Updated',count)

    socket.on('Incrementing',()=>{
        count = count + 1

        //socket.emit('Count-Updated',count) This method only emits on single connection.
        io.emit('Count-Updated',count)
    })
    */
})

server.listen(port,()=>{
    console.log(`application running on ${port} !`)
})