<template>
  <div>
        
        <p> Client name : {{ Client_information.name}}</p>
        <p> Telephone : {{ Client_information.telephone}}</p>
        <p> address : {{ Client_information.address}}</p>
      
  </div>
    
</template>


<script>

export default {
    name: 'ClientInfo',
    props: {
        Client_information: Object,
    },
    components: {
        
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