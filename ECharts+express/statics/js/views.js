
// commonjs
let express = require('express');
let router = express.Router();  // router object


router.get('/', (req, res, next) => {
    // return a json to client
    //res.send({ name: 'frances', age: 23, gender: 'female' });

    // throw an error to client
    setTimeout(() => {
        try {
            throw new Error('Invalid URL');
        }
        catch (e) {
            next(e);
        }
    }, 1000);
});

router.get('/user', function(req, res) {
    // get the query argument passed by user
    // By default, req.query is empty.
    console.log(req.query);
    res.send(req.query);
});

// :id here is a dynamic argument
router.get('/user/:id/:username', function(req, res) {
    // req.params: the URL matches dynamically, which is empty by default
    console.log(req.params);
    res.send(req.params);
});



// commonjs
module.exports = {router};