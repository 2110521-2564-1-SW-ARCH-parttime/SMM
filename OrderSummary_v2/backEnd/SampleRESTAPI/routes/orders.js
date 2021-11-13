const express = require('express')
const router = express.Router()
const Order = require('../models/order')


// Getting all
router.get('/', async (req, res) => {
  try {
    const orders = await Order.find()
    res.json(orders)
  } catch (err) {
    res.status(500).json({ message: err.message })
  }
})

// app.get("/set_cookie", (req, res) => {
//   var a = 'pp'
//   res.cookie('token_cookie', a, { maxAge: oneDay / 48 });
//   console.log('set_cookie')
//   res.send('keep_cookie')
// })

// Getting One
router.get('/Store_name/:store_name', getStore, (req, res) => {
  res.json(res.order)
})

router.get('/:_id', getOrder, (req, res) => {
  res.json(res.order)
})

// Creating one
router.post('/', async (req, res) => {
  const order = new Order({
    products: req.body.products,
  })
  try {
    const newOrder = await order.save()
    res.status(201).json(newOrder)
  } catch (err) {
    res.status(400).json({ message: err.message })
  }
})



// Updating One
// router.patch('/:id', getOrder, async (req, res) => {
//   if (req.body.name != null) {
//     res.subscriber.name = req.body.name
//   }
//   if (req.body.subscribedToChannel != null) {
//     res.subscriber.subscribedToChannel = req.body.subscribedToChannel
//   }
//   try {
//     const updatedSubscriber = await res.subscriber.save()
//     res.json(updatedSubscriber)
//   } catch (err) {
//     res.status(400).json({ message: err.message })
//   }
// })

// Deleting One
router.delete('/:_id', getOrder, async (req, res) => {
  try {
    await res.order.remove()
    res.json({ message: 'Deleted Order' })
  } catch (err) {
    res.status(500).json({ message: err.message })
  }
})

async function getOrder(req, res, next) {
  let order
  try {
    order = await Order.findById(req.params._id)
    if (order == null) {
      return res.status(404).json({ message: 'Cannot find order' })
    }
  } catch (err) {
    return res.status(500).json({ message: err.message })
  }

  res.order = order
  next()
}

async function getStore(req, res, next) {
  let order
  const store_name = req.params.store_name
  try {
    order = await Order.find({"Store_name":store_name})
    if (order == null) {
      return res.status(404).json({ message: 'Cannot find Store' })
    }
  } catch (err) {
    return res.status(500).json({ message: err.message })
  }

  res.order = order
  next()
}



module.exports = router