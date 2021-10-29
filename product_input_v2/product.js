const mongoose = require('mongoose')
const Schema = mongoose.Schema
const productSchema = new Schema({
    name: String,
    category: String,
    price: Number,
    image: String
})
const ProductModel = mongoose.model('shoptest01', productSchema)
module.exports = ProductModel


// name: String,
// category: String,
// price: Number,
// image: String,
// shop_id: String,
// shop_name: String,
// tags: [String]