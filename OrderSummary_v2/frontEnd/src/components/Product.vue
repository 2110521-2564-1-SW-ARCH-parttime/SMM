<template>
    <div class="product">
        <h3>
            {{ product.product_id }}
        </h3>    
        <p> product name : {{ product.name}}</p>
        <p> price : {{ product.price}}</p>
        <p> amount : {{ product.amount}}</p>
        <!-- <img :src=product.image class="img-circle" alt="Services" />  -->
        
     </div>    
</template>



<script>
export default {
    name: 'Product ',
    props: {
        product: Object
    },
}
</script>

<style scope>
.fas {
  color: red;
}
.product {
  background: #f4f4f4;
  margin: 5px;
  padding: 10px 20px;
  cursor: pointer;
}
.product.reminder {
  border-left: 5px solid green;
}
.product h3 {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>