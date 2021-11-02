import re
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

  
# Replace your URL here. Don't forget to replace the password.
connection_url = 'mongodb+srv://mike01:admin1234@lllmikelll.snklj.gcp.mongodb.net/mikeshop?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)
  
# Database
Database = client.get_database('mikeshop')
# Table
Shop = Database.shoptest02_with_owners

  
@app.route("/catalog/<shop>", methods=["GET"])
def login(shop):
    query = Shop.find({"owner":shop})
    output = []
    i = 0
    for x in query:
        output.append(x)
        output[i].pop('_id')
        i += 1
    # print(output)
    return render_template("catalog.html", productData=output, shop=shop)

@app.route("/cart", methods=["GET","POST"])
def order():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(debug=True)