  <template>
  <div class="container">
  
    <Header
      @back_to_previous_page="backToPreviousPage"
      title="Order summary"
    />

    <Orders
    @accept-order='acceptOrder'
    @cancle-order='cancleOrder'
    :orders="orders"
    />

  </div>
</template>

<script>
import Header from "./components/Header";
import Orders from './components/Orders'

export default {
  name: "App",
  components: {
    Header,
    Orders
  },
  data() {
    return {
      orders: [],
    };
  },
  
  methods: {
    backToPreviousPage(){
      console.log('pom be back')
      console.log("this router", this.$route.params.name)
      this.$router.push('http://localhost:5048/') 
    },
    async acceptOrder(id){
      console.log(id)
    },
    async cancleOrder(id){
      if( confirm("Are you sure?")){
        const res = await fetch(`api/orders/${id}`, {
          method: "DELETE",
        });
      
      res.status === 200
          ? (this.orders = this.orders.filter((order) => order.id !== id )) 
          : alert("Error deleteing task");
      }
      location.reload(true);
    },
    async fetchOrder(store){
      // const res = await fetch('api/orders/')
      const res = await fetch(`api/orders/Store_name/${store}`)

      const data = await res.json()

      return data;
    }
  },
  watch : {
     async '$route' (to) {
     this.orders = await this.fetchOrder(to.params.name)
    }
  },
  async created() {

    this.orders = await this.fetchOrder(this.$route.params.name)
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  font-family: "Poppins", sans-serif;
}
.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}
.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
