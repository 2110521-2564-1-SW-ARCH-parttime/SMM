<template>
    <header>
        <h1>{{ title }}</h1>
        <a class="btn btn-success btn-block" href="http://localhost:5048/" role="button">back</a>
        <!-- <Button @btn-click="$emit('back_to_previous_page')"
        text="Back"
        color ='blue' 
        /> -->
        <!-- <Button @btn-click="$emit('toggle-add-task')"
        :text="showAddTask ? 'Close' : 'Add Task'"
        :color ="showAddTask ? 'red' : 'green'" /> -->
    </header>

</template>

<script>


export default {
    name: 'Header',
    props :{
        title :{
            String,
            default : 'Hello World'
        } ,
        showAddTask: Boolean
    },
    
    components: {
        
    }
}
</script>

<style scoped>
header{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
</style>