<template>
  <div class="text-xs-center">
    <v-bottom-sheet v-model="sheet">
      <v-btn
        slot="activator"
        color="green"
        dark
      >
        Add
      </v-btn>

      <v-list>
        <v-form >
          <v-container>
            <v-layout>
              <v-flex xs12 md4 >
                <v-text-field
                  v-model="name"
                  :counter="15"
                  label="Name"
                  required
                ></v-text-field>
              </v-flex>

            <v-flex xs12 md4 d-flex>
              <v-select
                item-value="shortCode"
                item-text="text"
                v-model="status"
                :items="options"
                label="Status"
              ></v-select>
            </v-flex>

              <v-btn color="success" @click="saveNewItem" >Submit</v-btn>


            </v-layout>
          </v-container>
        </v-form>
      </v-list>
    </v-bottom-sheet>
  </div>
</template>


<script>
  export default {
    data: () => ({
      sheet: false,
      name: '',
      status: 1,
      options:[
        { shortCode:1, text: 'To-do' },
        { shortCode:2, text: 'In-progress' },
        { shortCode:3, text: 'Done' },
      ]
    }),
    methods:{
      saveNewItem (){
        this.sheet = false

        let vm = this
        this.$http({
          method: 'post',
          url:'http://127.0.0.1:8000/api/tasks/',
          data:{
            name: vm.name.trim(),
            status: vm.status
          },
          headers: {'Authorization': 'jwt '+ localStorage.getItem("tkn") }
        })
        .then(function (response) {
            console.log(response)            
            vm.$emit('addedItem',response.data)
        })
        .catch(function (error) {
            console.log(error)
        })
      }
    }
  }
</script>