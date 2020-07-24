const mongoose = require('mongoose')

mongoose.connect('mongodb://mongo/mydatabase')
        .then(db => console.log('Db is conect', db.connection.host))
        .catch(err => console.log(err))