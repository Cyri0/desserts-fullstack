import React, { useEffect, useState } from 'react'
import DessertCard from './DessertCard'

const App = () => {
  const [desserts, setDesserts] = useState([])
  
  useEffect(()=>{
    fetch("/desserts/all/")
    .then(res => res.json())
    .then(data => {
      console.log(data);
      setDesserts(data);
    })
  }, [])

  return (
    <div className='red'>
      { desserts.map(dessert => <DessertCard {... dessert}/>) }
    </div>
  )
}

export default App