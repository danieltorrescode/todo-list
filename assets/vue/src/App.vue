<template>
<v-app>
    <v-toolbar app>
    <v-toolbar-title class="headline text-uppercase">
        <span>To-do List</span>
    </v-toolbar-title>
    <v-spacer></v-spacer>
        <div id="nav">
            <router-link to="/">Sing Up</router-link> |
            <router-link to="/login">Log In</router-link> |        
            <a href="" v-on:click="logout" >Log out</a> |        
            <router-link to="/todoList">Todo List</router-link>
        </div>        
    </v-toolbar>

    <v-content>
    <router-view/>
    </v-content>

</v-app>
</template>

<script>
    export default {
        name: 'App',
        components: {
        },
        data: () => ({            
        }),
        methods:{
            logout (){
                localStorage.setItem("tkn", '')
                this.$router.push("login")
            }
        }
    }
</script>
