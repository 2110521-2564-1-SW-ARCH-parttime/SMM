  <template>
  <div class="container">
    <!-- <Orders
      title="Order Summary"
    /> -->
    <Header
      @toggle-add-task="toggleAddTask"
      title="Order summary"
      :showAddTask="showAddTask"
    />
    <!-- <div v-if="showAddTask">
      <AddTask @add-task="addTask" />
    </div> -->

    <!-- <Tasks
      @toggle-reminder="toggleReminder"
      @delete-task="deleteTask"
      :tasks="tasks"
    /> -->

    <!-- <Products
    :products="products"
    /> -->

    <Orders
    @accept-order='acceptOrder'
    @cancle-order='cancleOrder'
    :orders="orders"
    />

  </div>
</template>

<script>
// import Orders from "./components/Orders"
import Header from "./components/Header";
// import Tasks from "./components/Tasks";
// import AddTask from "./components/AddTask";
// import Products from './components/Products'
import Orders from './components/Orders'

export default {
  name: "App",
  components: {
    // Orders,
    Header,
    // Tasks,
    // AddTask,
    // Products,
    Orders
  },
  data() {
    return {
      tasks: [],
      showAddTask: false,
      products: [],
      orders: [],
    };
  },
  methods: {
    toggleAddTask() {
      this.showAddTask = !this.showAddTask;
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
    async addTask(task) {
      const res = await fetch("api/tasks", {
        method: "POST",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(task),
      });
      const data = await res.json();

      this.tasks = [...this.tasks, data];
    },
    async deleteTask(id) {
      if (confirm("Are you sure?")) {
        const res = await fetch(`api/tasks/${id}`, {
          method: "DELETE",
        });

        res.status === 200
          ? (this.tasks = this.tasks.filter((task) => task.id !== id ))
          : alert("Error deleteing task");
      }
    },
    async toggleReminder(id) {
      const taskToToggle = await this.fetchTask(id);
      const updTask = { ...taskToToggle, reminder: !taskToToggle.reminder };

      const res = await fetch(`api/tasks/${id}`, {
        method: "PUT",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(updTask),
      });

      const data = await res.json();

      this.tasks = this.tasks.map((task) =>
        task.id === id ? { ...task, reminder: data.reminder } : task
      );
    },
    async fetchTasks() {
      const res = await fetch("api/tasks");

      const data = await res.json();

      return data;
    },
    async fetchTask(id) {
      const res = await fetch(`api/tasks/${id}`);

      const data = await res.json();

      return data;
    },
    async fetchProducts(){
      const res = await fetch("api/products")

      const data = await res.json()

      return data;
    },
    async fetchOrder(){
      const res = await fetch("api/orders")

      const data = await res.json()

      return data;
    }
  },
  async created() {
    // this.tasks = await this.fetchTasks();
    // this.products = await this.fetchProducts();
    this.orders = await this.fetchOrder()
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
