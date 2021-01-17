const express = require('express')
const path = require('path')

//const date = require('date-and-time');
const app = express()
//const server=require('http').Server(app)
//const io= require('socket.io')(server)
const now = new Date();
const port =3000       // Port Number of Nodejs

app.use(express.json({limit:'500tb'}))
app.set('view engine','ejs')

let images_live = '' 

/*app.get('/',async(req,res)=>{
  res.render('index')
})*/
app.all('/',async(req,res)=>{
    live_stream_images = req.body.Image
    images_live =live_stream_images
    console.log(typeof(req.body.Image)) 
    
    console.log("================================================================")
    //res.send(req.body.Image)
    res.render('index')
})

app.get('/data',async(req,res)=>{

  a=req.body
  b={new:'1',old:'2'} 
  console.log(typeof(images_live))
  res.render('stream',{data:{imageData:images_live,number:'12'}})
})

app.listen(port,()=>{
    console.log("Starting on port: "+port)
})
