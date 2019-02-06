import Vue from 'vue'
import Router from 'vue-router'
import Register from './views/Register.vue'
import LogIn from './views/LogIn.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/todoList',
      name: 'todoList',
      // route level code-splitting
      // this generates a separate chunk (todoList.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "todoList" */ './views/TodoList.vue')
    }
  ]
})
