import React from 'react'
import { Routes, Route } from 'react-router-dom'
import SignIn from './components/SignIn/SignIn'
import SignUp from './components/SignUp/SignUp'

function App() {
  return (
    <Routes>
      <Route path="/signin" element={<SignIn />} />
      <Route path="/auth" element={<SignUp />} />
      <Route path="/" element={<div>Home Page</div>} />
    </Routes>
  )
}

export default App 