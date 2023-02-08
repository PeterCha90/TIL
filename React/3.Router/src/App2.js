import React from 'react'
import Home from './pages/Home'
import About from './pages/About'
import Profile from './pages/Profile'
import Article from './pages/Article'
import Articles from './pages/Articles'
import { Route, Routes } from 'react-router-dom'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/profiles/:username" element={<Profile />} />
        <Route path="/articles" element={<Articles />} />
        <Route path="/articles/:id" element={<Article />} />
      </Routes>
    </div>
  )
}

export default App
