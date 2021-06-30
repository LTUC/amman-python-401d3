import axios from 'axios'
import snacks from '../fixtures/snacks.json'
const base_url = 'https://snacks-api-dario.herokuapp.com/'

export async function fetchSnacks(web = true) {
    if (web) {
        return webFetchSnacks();
    } else {
        return snacks
    }
}

export async function fetchSnack(id, web=true) {
    if (web) {
        return webFetchSnack(id);
    } else {
        return snacks[0]
    }
}
async function webFetchSnacks() {
    const tokenResponse = await login('abed', 'Abed123!')
    const { refresh, access: token } = tokenResponse.data;
    const config = {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
    const response = await axios.get(`${base_url}api/v1/snacks/`, config);
    return response.data;
  }
  

export async function webFetchSnack(id) {
    const tokenResponse = await login('abed', 'Abed123!')
    const { refresh, access: token } = tokenResponse.data;
    const config = {
      headers: {
        Authorization: `Bearer ${token}`
      }
    }
    const response = await axios.get(`${base_url}api/v1/snacks/${id}`, config);
    return response.data;
  }

async function login(username, password) {
    return axios.post(`${base_url}api/token/`, {
        username,
        password
      });
}