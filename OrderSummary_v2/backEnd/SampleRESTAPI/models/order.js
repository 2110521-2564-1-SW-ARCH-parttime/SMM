const mongoose = require('mongoose')

const orderSchema = new mongoose.Schema({
  Store_name:{
    type : String,
    required : true
  },
  Cart: [{
    product_id: {
        type : String,
        required: true,
    },
    name:{
      type: String,
      required: true,
    },
    Qty:{
        type: Number,
        required: true,
    },
    price:{
        type: Number,
        required: true,
    },
    image:{
        type: String,
        required: true,
    },
  },],
  Client_information:{
    name:{
      type: String,
      required: true
    },
    telephone:{
      type: String,
      required: true
    },
    address:{
      type: String,
      required: true
    }
  }
})

module.exports = mongoose.model('orderSchema', orderSchema)