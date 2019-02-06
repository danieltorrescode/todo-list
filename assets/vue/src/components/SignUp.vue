<template>
<v-form
    ref="form"
    v-model="valid"
    lazy-validation
>
    <v-text-field
    v-model="username"
    :counter="10"
    :rules="usernameRules"
    label="Username"
    required
    ></v-text-field>

    <v-text-field
    v-model="email"
    :rules="emailRules"
    label="E-mail"
    required
    ></v-text-field>

    <v-text-field
    v-model="password"
    :counter="10"
    label="Password"
    type="password"
    required
    ></v-text-field>

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

</v-form>
</template>

<script>
    export default {
        data: () => ({
            valid: true,
            username: '',
            usernameRules: [
                v => !!v || 'Name is required',
                v => (v && v.length <= 10) || 'Name must be less than 10 characters'
            ],
            email: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+/.test(v) || 'E-mail must be valid'
            ],
            password:''
        }),
        methods: {
            validate () {
                if (this.$refs.form.validate()) {
                this.snackbar = true
                this.signup()
                
                }
            },
            reset () {
                this.$refs.form.reset()
            },
            signup: function () {
                let vm = this
                this.$http.post('http://127.0.0.1:8000/api/users/', {
                    username: this.username.trim(),
                    password: this.password.trim(),
                    email:this.email.trim()
                })
                .then(function (response) {
                    // console.log(response)
                    localStorage.setItem("tkn", response.data.token)
                    vm.$router.push("/TodoList")
                })
                .catch(function (error) {
                    console.log(error)
                })
            }
        }
    }
</script>

<style>

</style>
