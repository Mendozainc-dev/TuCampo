import React from 'react'

const navbar = () => {
  return (
    <div>
      <label htmlFor="">USUARIO</label>
      <input type="text" name="username" id="username" />
      <label htmlFor="">Contraseña</label>
      <input type="password" name="password" id="password" />
    </div>
    
  )
}

export default navbar