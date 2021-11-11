<template>
  <div>
    <div :key="product.product_id" v-for="product in products">
      <Product
        @delete-task="$emit('delete-Product', product.id)"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import Product from "./Product";

export default {
  name: "Products",
  props: {
    products: Array,
  },
  components: {
    Product,
  },
  emits: ["delete-Product"],
};
</script>
