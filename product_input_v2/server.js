const PROTO_PATH = "./product.proto";

var grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");

var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});

var shopProto = grpc.loadPackageDefinition(packageDefinition);

const { v4: uuidv4 } = require("uuid");

const server = new grpc.Server();
// const product = [{
//     id: "a68b823c-7ca6-44bc-b721-fb4d5312cafc",
//     name: "Tomyam Gung",
//     image: "image",
//     price: 500,
//     shop_id: "1234",
//     shop_name: "mike"

// }];

// connect monggose
const mongoose = require('mongoose')
mongoose.connect("mongodb+srv://mike01:admin1234@lllmikelll.snklj.gcp.mongodb.net/mikeshop?retryWrites=true&w=majority", { useNewUrlParser: true })
const Product = require('./product')
const products = [{}]
const db = mongoose.connection
db.once('open', () => console.log('connected to database'))



server.addService(shopProto.ShopService.service, {
    getAllProduct: getAllProduct,
    insert: insertProduct,
    update: updateProduct,
    remove: removeProduct
});

async function getAllProduct(call, callback) {
    const product = await Product.find()
    console.log(product)
    callback(null, { product });
}

async function insertProduct(call, callback) {
    const ProductItem = call.request;
    console.log(ProductItem)
    const product = new Product(ProductItem)
    await product.save()
    callback(null, ProductItem)
}

async function updateProduct(call, callback) {
    const product_id = { _id: call.request._id }
    const ProductItem = {
        name: call.request.name,
        category: call.request.category,
        price: call.request.price,
        image: call.request.image
    }
    await Product.findOneAndUpdate(product_id, { $set: ProductItem })
    console.log(product_id)
    console.log(ProductItem)
    callback(null, ProductItem);

    // const ProductItem = call.request;
    // console.log(ProductItem)
    // callback(null, { ProductItem });
}

async function removeProduct(call, callback) {
    const ProductId = call.request._id
    console.log(ProductId)
    try {
        await Product.findByIdAndDelete(ProductId)
        callback(null, {})
    } catch (err) {
        callback({
            code: grpc.status.NOT_FOUND,
            details: "Not Found"
        })
    }
}

server.bind("127.0.0.1:30043", grpc.ServerCredentials.createInsecure());
console.log("Server running at http://127.0.0.1:30043");
server.start();





// getAllMenu: (_,callback)=>{
//     callback(null, {menu});
// },
// get: (call,callback)=>{
//     let menuItem = menu.find(n=>n.id==call.request.id);

//     if(menuItem) {
//         callback(null, menuItem);
//     }else {
//         callback({
//             code: grpc.status.NOT_FOUND,
//             details: "Not found"
//         });
//     }
// },
// insert: (call, callback)=>{
//     let menuItem=call.request;

//     menuItem.id=uuidv4();
//     menu.push(menuItem);
//     callback(null,menuItem);
// },
// update: (call,callback)=>{
//     let existingMenuItem = menu.find(n=>n.id==call.request.id);

//     if(existingMenuItem){
//         existingMenuItem.name=call.request.name;
//         existingMenuItem.price=call.request.price;
//         callback(null,existingMenuItem);
//     } else {
//         callback({
//             code: grpc.status.NOT_FOUND,
//             details: "Not Found"
//         });
//     }
// },
// remove: (call, callback) => {
//     let existingMenuItemIndex = menu.findIndex(n=>n.id==call.request.id);

//     if(existingMenuItemIndex != -1){
//         menu.splice(existingMenuItemIndex,1);
//         callback(null,{});
//     } else {
//         callback({
//             code: grpc.status.NOT_FOUND,
//             details: "NOT Found"
//         });
//     }
// }