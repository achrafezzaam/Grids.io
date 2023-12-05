import { useState, useEffect } from 'react'

function App() {

  useEffect(()=> {
    const url = import.meta.env.VITE_API_URL;
    console.log(url+'grids');
  }, [])
  return (
    <>
    </>
  )
}

export default App
