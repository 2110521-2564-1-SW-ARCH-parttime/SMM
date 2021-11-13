<template>
  <div>
    <div :key="order._id" v-for="order in orders">
      <div class="container">
        Order {{ order._id }}
        <ClientInfo :Client_information="order.Client_information" />
        <Products :products="order.Cart" />
         <Button @btn-click="$emit('accept-order',order._id)"
        text="Accept"
        color ='green' 
        />
        <Button @btn-click="$emit('cancle-order',order._id)"
        text="Cancle"
        color ='red' 
        />
      </div>
    </div>   
  </div>
    
</template>


<script>
import Products from './Products'
import Button from './Button'
import ClientInfo from './ClientInfo'

export default {
    name: 'Orders ',
    props: {
        orders: Array,
    },
    components: {
        Products,
        Button,
        ClientInfo,
    }
}
</script>

<style scope>
.fas {
  color: red;
}
.task {
  background: #f4f4f4;
  margin: 5px;
  padding: 10px 20px;
  cursor: pointer;
}
.task.reminder {
  border-left: 5px solid green;
}
.task h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
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
</style>