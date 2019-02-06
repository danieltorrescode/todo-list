<template>
<v-container align-center>    
    <v-layout row wrap  align-center justify-center>
    <v-flex xs6>
        <v-card>
            <v-toolbar color="cyan" dark>
                <v-toolbar-title>Tasks</v-toolbar-title>
                <v-spacer></v-spacer>
                <AddItem v-on:addedItem="addToDOM($event)" />
            </v-toolbar>
            <v-list two-line>
                <template v-for="(item, index) in items">
                    <Item
                    v-on:deletedItem="removeFromDOM($event)"
                    v-bind:item="item"
                    v-bind:index="index"
                    :key="index"
                    ></Item>
                </template>
            </v-list>  

        </v-card>
    </v-flex>
    </v-layout>
</v-container>
</template>

<script>
import Item from '../components/Item.vue'
import AddItem from '../components/AddItem.vue'

export default {
    components: {
        Item,
        AddItem
    },
    data: () =>({
        items: []
    }),
    created () {
        this.getTasks()
    },
    methods:{
        getTasks () {
            this.items=null
            let vm = this
            this.$http.get(
                'http://127.0.0.1:8000/api/tasks/',
                {
                    headers: { 
                        'Authorization': 'jwt '+ localStorage.getItem("tkn") 
                    }
                }
            )
            .then(function (response) {
                // handle success
                // console.log(response.data)
                vm.items = response.data
            })
            .catch(function (error) {
                // handle error
                console.log(error)
            })
            .then(function () {
                // always executed
            })
        },
        removeFromDOM(id_event){
            this.items = this.items.filter( item =>  item.id != id_event)            
        },
        addToDOM(id_event){
            this.items.push(id_event)           
        }
    }
}
</script>