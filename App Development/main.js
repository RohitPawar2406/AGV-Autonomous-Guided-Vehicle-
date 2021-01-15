const express = require('express')
const path = require('path')

//const date = require('date-and-time');
const app = express()
const server=require('http').Server(app)
const io= require('socket.io')(server)
const now = new Date();
const port =5005       // Port Number of Nodejs

app.use(express.json({limit:'500tb'}))

app.post('/',async(req,res)=>{
    live_stream_images = req.body.Image
    console.log(typeof(req.body.Image))  
    io.emit('image',live_stream_images)
    console.log("================================================================")
    console.log("================================================================")
    //res.send(req.body.Image)
    res.sendFile(path.join(__dirname,'index1.html'))
})


app.get('/sending',async(req,res)=>{

  a=req.body
  b={new:'1',old:'2'} 
  console.log(a.Forward,typeof(a.Forward))
  res.send(b)
})
/*app.get('/liveonHTML',(req,res)=>{
  res.sendFile(path.join(__dirname,'index1.html'))
})*/

/*setInterval(()=>{
  image = 
  io.emit('image','some data')
},1000)*/

server.listen(port,()=>{
    console.log("Starting on port: "+port)
})
