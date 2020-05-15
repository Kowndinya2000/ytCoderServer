var express = require('express')
var path = require('path')
var PORT = process.env.PORT || 5000
var bodyParser = require("body-parser")
var cors = require('cors')
express()
  .use(express.static(path.join(__dirname, 'public')))
  .set('views', path.join(__dirname, 'views'))
  .set('view engine', 'ejs')
  .use(bodyParser.urlencoded({ extended: false }))
  .use(bodyParser.json())
  .use(cors({
      credentials: true,
  }))
  .get('/', (req, res) => {
    res.header('Acess-Control-Allow-Credentials','true')
    res.header('Access-Control-Allow-Origin', '*');
    res.render('pages/index',{message:""})
    })
  .post('/',(req, res) => {
    req.header('Access-Control-Allow-Origin', '*');
    let {PythonShell} = require('python-shell') 
    let pyshell = new PythonShell('ocr.py')
    var url = req.body.link.split("--")[0];
    var timeStamp = req.body.link.split("--")[1]
    var t1 = parseInt(timeStamp.split(":")[0])
    var t2 = parseInt(timeStamp.split(":")[1])
    t1 = (t1*60.0) + t2
    var timeLength = req.body.link.split("--")[2]
    var a1 = parseInt(timeLength.split(":")[0])
    var a2 = parseInt(timeLength.split(":")[1])
    a1 = (a1*60.0) + a2 
    pyshell.send(url+"--"+t1+"--"+a1)
    pyshell.on('message',function(message){
    console.log(message)
    })
  
  pyshell.end(function (err,code,signal) {
    if(err) throw err 
    console.log('The exit code was: '+ code)
    console.log('The exit signal was: '+signal)
    console.log('finished')    
    res.json({message: "Done Reading!"})
  })
  })
  .listen(PORT, () => console.log(`Listening on ${ PORT }`))