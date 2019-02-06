<template>
    <v-form >
    <v-container>
      <v-layout>
        <v-flex xs12 md4 >
          <v-text-field
            v-model="item.name"
            :counter="15"
            label="Name"
            required
            v-bind:disabled="disableUsername"
          ></v-text-field>
        </v-flex>

      <v-flex xs12 md4 d-flex>
        <v-select
          item-value="shortCode"
          item-text="text"
          v-model="item.status"
          :items="options"
          label="Status"
          v-bind:disabled="disableStatus"
        ></v-select>
      </v-flex>

        <v-btn v-if="showBtn" color="success" @click="update" >Done</v-btn>
        <v-btn v-else color="warning" @click="displayBtn" >Edit</v-btn>
        <v-btn color="error" @click="destroy">delete</v-btn>

      </v-layout>
    </v-container>
  </v-form>
</template>

<script>
  export default {
    props: ['index','item'],
    components: {
    },
    data: ()=>({
        showBtn:false,
        disableUsername:true,
        disableStatus:true,
        options:[
          { shortCode:1, text: 'To-do' },
          { shortCode:2, text: 'In-progress' },
          { shortCode:3, text: 'Done' },
        ]
    }),
    methods:{
        displayBtn(){
          this.showBtn = !this.showBtn
          this.disableUsername = !this.disableUsername
          this.disableStatus = !this.disableStatus
        },
        destroy(){
            
            let vm = this
            this.$http({
              method: 'delete',
              url:'http://127.0.0.1:8000/api/tasks/edit/'+vm.item.id+'/',
               headers: {'Authorization': 'jwt '+ localStorage.getItem("tkn") }
            })
            .then(function (response) {
                // handle success
                console.log(response.data)
                vm.$emit('deletedItem',vm.item.id)
            })
            .catch(function (error) {
                // handle error
                console.log(error)
            })
            .then(function () {
                // always executed
            })
        },
        update(){
            this.showBtn = !this.showBtn
            this.disableUsername = !this.disableUsername
            this.disableStatus = !this.disableStatus
            let vm = this
            this.$http({
              method: 'put',
              url:'http://127.0.0.1:8000/api/tasks/edit/'+vm.item.id+'/',
              data:{
                name: vm.item.name,
                status: vm.item.status
              },
               headers: {'Authorization': 'jwt '+ localStorage.getItem("tkn") }
            })
            .then(function (response) {
                // handle success
                console.log(response.data)
                // vm.$emit('refresh')
            })
            .catch(function (error) {
                // handle error
                console.log(error)
            })
            .then(function () {
                // always executed
            })
        },
    }
  }
</script>