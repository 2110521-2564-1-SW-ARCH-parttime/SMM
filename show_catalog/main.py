import os
from flask import Flask, jsonify, request, render_template, url_for, session, redirect, flash, json
from flask_cors import CORS
import pymongo
import pika

  
# Replace your URL here. Don't forget to replace the password.
connection_url = 'mongodb+srv://mike01:admin1234@lllmikelll.snklj.gcp.mongodb.net/mikeshop?retryWrites=true&w=majority'
app = Flask(__name__)
app.secret_key = "secret key"
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('mikeshop')
# Table
Shop = Database.shoptest02_with_owners

  
@app.route("/catalog/<shop>", methods=["GET"])
def catalog(shop):
    query = Shop.find({"owner":shop})
    session['shop'] = shop
    output = []
    i = 0
    # print(query[0])
    for x in query:
        output.append(x)
        i += 1
    # print(output)
    return render_template("catalog.html", productData=output, shop=shop)

@app.route("/cart", methods=["GET","POST"])
def cart():
    prodName = request.form.get('name')
    prodID = request.form.get('id')
    prodAmount = int(request.form.get('amount'))
    prodPrice = int(request.form.get('price'))

    if 'cart_list' in session:
        prodIds = [prod.get('id') for prod in session['cart_list']]
        if prodID in prodIds:
            # print(session['cart_list'][prodIds.index(prodID)])
            session['cart_list'][prodIds.index(prodID)]['amount'] += prodAmount
            # print(prodIds.index(prodID))
        else:
            session['cart_list'] += [{'id':prodID,'product':prodName ,'amount':prodAmount,'price':prodPrice}]
    else:
        session['cart_list'] = [{'id':prodID,'product':prodName ,'amount':prodAmount,'price':prodPrice}]
    # flash(f'You added Product ID:{prodID} Product Name:{prodName} Amount:{prodAmount} to cart {cart_id}')
    # flash(session['cart_list'])

    return redirect('catalog/'+session.get('shop'))

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/cancel")
def cancel():
    if 'cart_list' in session:
        session.pop('cart_list')
    return redirect('catalog/'+session.get('shop'))

@app.route("/sendOrder", methods=["GET","POST"])
def sendOrder():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    # channel.queue_declare(queue='order_queue')
    
    carts = []
    for data in session['cart_list']:
        cart = {"product_id":data["id"], "name":data["product"], "amount":data["amount"], "price":data["price"]}
        carts.append(cart)
    msg_dict = {
        "Store_name":session['shop']
        , "Cart":carts
        , "Client_information":{"name":request.form.get('name'),"telephone":request.form.get('tel'),"address":request.form.get('address')}
    }
    msg_str = json.dumps(msg_dict, indent=3)
    channel.basic_publish(exchange='',
                        routing_key='order_queue',
                        body=msg_str)
    connection.close()
    session.pop('cart_list')
    # flash(msg_str)
    # print(msg_str)

    return render_template("sendOrder.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)