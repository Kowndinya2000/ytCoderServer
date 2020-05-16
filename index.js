var express = require('express')
var path = require('path')
var PORT = process.env.PORT || 5000
var bodyParser = require("body-parser")
var cors = require('cors')
var result_text = [];
const corsOptions = {
  origin: 'https://youtube.com'
}
express()
  .use(express.static(path.join(__dirname, 'public')))
  .set('views', path.join(__dirname, 'views'))
  .set('view engine', 'ejs')
  .use(bodyParser.urlencoded({ extended: false }))
  .use(bodyParser.json())
  .use(cors({
      credentials: true,
  }))
  .use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", '*');
    res.header("Access-Control-Allow-Credentials", true);
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header("Access-Control-Allow-Headers", 'Origin,X-Requested-With,Content-Type,Accept,content-type,application/json');
    next();
    })
  .get('/', cors(corsOptions), (req, res) => {
    res.render('pages/index',{message:""})
    })
  .post('/', cors(corsOptions),(req, res) => {
    res.header("Access-Control-Allow-Origin", '*');
    res.header("Access-Control-Allow-Credentials", true);
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header("Access-Control-Allow-Headers", 'Origin,X-Requested-With,Content-Type,Accept,content-type,application/json');
    let {PythonShell} = require('python-shell') 
    let pyshell = new PythonShell('ocr.py')
    pyshell.send(req.body.link)
    pyshell.on('message',function(message){
    console.log(message)
    result_text.push(message)
    })
  
  pyshell.end(function (err,code,signal) {
    if(err) throw err 
    console.log('The exit code was: '+ code)
    console.log('The exit signal was: '+signal)
    console.log('finished')    
    res.json({message: result_text})
  })
  })
  .listen(PORT, () => console.log(`Listening on ${ PORT }`))