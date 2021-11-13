import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from "vue-router"


// const routes = [
//     {
//         path: "/" , component: App, props: ($route) => ({ name: $route.query }) 
//     }
// ]
const routes = [
    {
        path: "/:name" , component: App 
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

const myApp = createApp(App)
myApp.use(router)

myApp.mount('#app')

// createApp(App).mount('#app')
