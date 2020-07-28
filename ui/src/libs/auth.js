import axios from 'axios'
import Cookies from 'js-cookie'

const ENDPOINT_PATH = 'https://reqres.in/api/'

export default {
  register(email, password) {
    const user = {email, password}
    return axios.post(ENDPOINT_PATH+'register', user)
  },
  login(email, password){
    const user = {email, password}
    return axios.post(ENDPOINT_PATH+'login', user)
  },
  setUserLogged(user){
    Cookies.set('user',user)
  },
  getUserLogged(){
    return Cookies.get('user')
  },
  deleteUserLogged(){
    Cookies.remove('user')
  }
}