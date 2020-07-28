import axios from 'axios'

const URL = 'http://localhost:5555'

export default {
  save(url) {
    return axios.post(URL+'bookmark', {url})
  },
  list(){
    return axios.get(URL+'bookmark')
  }
}