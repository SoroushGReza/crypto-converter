import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://crypto-converter-app-372f4b2b2eda.herokuapp.com/api/',
});

export default instance;
