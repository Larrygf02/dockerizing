const mongoose = require('mongoose')
console.log('hola')
const DB_USER = "root"
const DB_PASS = "123"
const DB_HOST = "mongo"
const DB_PORT = "27018"
const DB_NAME = "mydatabase"
mongoose.connect(`mongodb://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?authSource=admin`, { useNewUrlParser: true })
        .then(db => console.log('Db is conect', db.connection.host))
        .catch(err => console.log("Ocurrio un error con la conexion"))