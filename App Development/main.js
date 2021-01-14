const express = require('express')
//const date = require('date-and-time');
const app = express()

const now = new Date();
const port =3001        // Port Number of Nodejs

app.use(express.json({limit:'500tb'}))


app.post('/',async(req,res)=>{
    live_stream_images = req.body.Image
    console.log(typeof(req.body.Image))  
    console.log("================================================================")
    console.log("================================================================")
    res.send(req.body.Image)
})


app.get('/sending',async(req,res)=>{

  a=req.body
  b={new:'1',old:'2'} 
  console.log(a.Forward,typeof(a.Forward))
  res.send(b)
})

app.listen(port,()=>{
    console.log("Starting on port: "+port)
})
