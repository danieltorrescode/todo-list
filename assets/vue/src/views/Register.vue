<template>
    <v-container align-center>    
        <v-layout row wrap  align-center justify-center>
        <v-flex xs6>
            <SignUp />
        </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import SignUp from '../components/SignUp'

    export default {
        components: {
            SignUp
        }
    }
</script>
