import { createStore } from 'vuex'
import { getAPI } from './axios-api'

const store = createStore({
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
    actions: {
        userLogin(context, usercredential){
            return new Promise((resolve, reject) => {
                getAPI.post('api/token/', {
                    username: usercredential.username,
                    password: usercredential.password
                })
                .then(response => {
                    context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh }) 
                    resolve()
                  })
                .catch(err => {
                    reject(err)
                  })
            })
        }
    }
});

export default store;