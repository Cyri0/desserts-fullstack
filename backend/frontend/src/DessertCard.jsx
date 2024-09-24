import React from 'react'

const DessertCard = (props) => {
  return (
    <div>
        <h1>Az elem ID-je:{props.id}</h1>
        <img width="400px" src={props.image} />
        <h2>{props.name}</h2>
        <h3>{props.price}$</h3>
    </div>
  )
}

export default DessertCard