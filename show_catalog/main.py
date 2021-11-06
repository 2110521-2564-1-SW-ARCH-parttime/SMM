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

    if 'cart_id' not in session:
        session['cart_id'] = request.remote_addr+"_"+session.get('shop')
    
    cart_id = session.get('cart_id')

    if 'cart_list' in session:
        session['cart_list'] += [{'id':prodID,'product':prodName ,'amount':prodAmount,'cost':prodPrice*prodAmount}]
    else:
        session['cart_list'] = [{'id':prodID,'product':prodName ,'amount':prodAmount,'cost':prodPrice*prodAmount}]

    # flash(f'You added Product ID:{prodID} Product Name:{prodName} Amount:{prodAmount} to cart {cart_id}')
    flash(session['cart_list'])

    return redirect('catalog/'+session.get('shop'))

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/sendOrder", methods=["GET","POST"])
def sendOrder():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    # msg = session['shop']
    # msg = msg + "," + request.form.get('name')
    # msg = msg + "," + request.form.get('tel')
    # msg = msg + "," + request.form.get('address')

    # for data in session['cart_list']:
    #     msg = msg + "," + data["id"]
    #     msg = msg + "," + data["product"]
    #     msg = msg + "," + str(data["amount"])
    #     msg = msg + "," + str(data["cost"])
    
    carts = []
    for data in session['cart_list']:
        cart = {"product_id":data["id"], "name":data["product"], "amount":data["amount"], "cost":data["cost"]}
        carts.append(cart)

    msg_dict = {
        "Store_name":session['shop']
        , "Cart":carts
        , "Client_information":{"name":request.form.get('name'),"telephone":request.form.get('tel'),"address":request.form.get('address')}
    }

    msg_str = json.dumps(msg_dict, indent=3)

    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=msg_str)

    connection.close()

    flash(msg_str)

    return render_template("sendOrder.html")

if __name__ == '__main__':
    app.run(debug=True)