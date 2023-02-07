
// commonjs
let express = require('express');
let {router} = require('./statics/js/views');


// Create an Express application
const app = express();
const port = 9003;


// register some urls
app.use('/api', router);
app.use('/static', express.static('statics'));
app.use('/template', express.static('templates'));


let server = app.listen(port, () => {
    console.log(`App is listening on... Host ${server.address().address}, Port ${port}`);
});

