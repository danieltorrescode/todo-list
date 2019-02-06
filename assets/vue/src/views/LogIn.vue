<template>
  <v-form 
    ref="form"
    v-model="valid"
    lazy-validation
  >
    <v-container>
      <v-layout row wrap  align-center justify-center>
        <v-flex xs12 md4>
          <v-text-field
            v-model="username"
            :rules="userNameRules"
            :counter="10"
            label="Username"
            required
          ></v-text-field>
        </v-flex>

        <v-flex  xs12 md4>
          <v-text-field
            v-model="password"
            :counter="10"
            label="Password"
            type="password"
            required
          ></v-text-field>
        </v-flex>
        
        <v-btn
          :disabled="!valid"
          color="success"
          @click="validate"
        >
          Submit
        </v-btn>

        <v-btn
          color="error"
          @click="reset"
        >
          Cancel
        </v-btn>
      </v-layout>
    </v-container>
  </v-form>
</template>


<script>
    export default {
        data: () => ({
            valid: false,
            username: '',
            userNameRules: [
                v => !!v || 'Username is required',
                v => v.length <= 10 || 'Username must be less than 10 characters'
            ],
            password:''
        }),
        methods: {
            validate () {
                if (this.$refs.form.validate()) {
                this.snackbar = true
                this.login()
                
                }
            },
            reset () {
                this.$refs.form.reset()
            },
            login: function () {
                let vm = this
                this.$http.post('http://127.0.0.1:8000/api/users/log_in/', {
                    username: this.username.trim(),
                    password: this.password.trim()
                })
                .then(function (response) {
                    // console.log(response)
                    localStorage.setItem("tkn", response.data.token)
                    vm.$router.push("/todoList")
                })
                .catch(function (error) {
                    console.log(error)
                })
            }
        }
    }
</script>