#!/usr/bin/env node

var amqp = require('amqplib/callback_api');

const Order = require('./model/order')
require('dotenv').config({path:'./config.env'});
const mongoose = require('mongoose')
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true , useUnifiedTopology: true })
const db = mongoose.connection
db.on('error', (error) => console.error(error))
db.once('open', () => console.log('Connected to Database'))


amqp.connect('amqp://localhost', function(error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }
    var queue = 'order_queue'; //this is topic

    channel.assertQueue(queue, {
      durable: true
    });
    channel.prefetch(1);
    console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);
    channel.consume(queue, async function(msg) {
        var secs = msg.content.toString().split('.').length - 1;
        console.log(" [x] Received");
        var temp = JSON.parse(msg.content);
        console.log(temp);
        // console.log(JSON.parse(msg.content));
        

        const order = new Order({
          Store_name: temp.Store_name,
          Cart: temp.Cart,
          Client_information: temp.Client_information
          })
          
        const newOrder = await order.save()
        

        // try {
        // const newOrder = await order.save()
        // res.status(201).json(newOrder)
        // } catch (err) {
        // res.status(400).json({ message: err.message })
        // }

        setTimeout(function() {
        console.log(" [x] Done");
        channel.ack(msg);
        }, secs * 1000);
    }, {
    noAck: false
    });
  });
});  
