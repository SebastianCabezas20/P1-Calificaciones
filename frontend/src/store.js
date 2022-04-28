import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
    },

    mutations: {
        updateStorage (state, { access, refresh }) {
            state.accessToken = access
            state.refreshToken = refresh
        },
    },

})