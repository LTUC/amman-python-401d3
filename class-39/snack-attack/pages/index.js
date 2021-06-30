import {useEffect, useState} from 'react'

import Layout from '../components/Layout';
import SnackCounter from '../components/SnackCounter'
import SnacksList from '../components/SnacksList'
import { fetchSnacks } from '../services/snacksAPI';

export default function Home() {
  const [snacks, setSnacks] = useState([])

  const handleClick = async () => {
    setSnacks(await fetchSnacks())
  }

  const effect = () => {
    async function getSnacks() {
      setSnacks(await fetchSnacks());
    }
    getSnacks()
  }
  // Side Effect 
  useEffect(effect, []) // on Mount  Mount -> Update -> Destroy
  // useEffect(effect) // on each update
  // useEffect(effect, [snacks]) // on snack update


  return (
    <Layout>
      <SnackCounter snacks={snacks.length}/>
      <SnacksList snacks={snacks} />
      <button onClick={handleClick} className={`bg-blue-200`}>Check For Snacks</button>
    </Layout>
  )
}
