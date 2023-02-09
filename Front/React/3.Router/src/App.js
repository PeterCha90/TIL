import React from 'react'
import Layout from './Layout'
import Home from './pages/Home'
import About from './pages/About'
import Login from './pages/Login'
import MyPage from './pages/MyPage'
import Profile from './pages/Profile'
import Article from './pages/Article'
import Articles from './pages/Articles'
import NotFound from './pages/NotFound'
import { Route, Routes } from 'react-router-dom'

const App = () => {
  return (
    <div>
      <Routes>
        <Route path="*" element={<NotFound />} />
        <Route path="/login" element={<Login />} />
        <Route path="/mypage" element={<MyPage />} />
        <Route element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/profiles/:username" element={<Profile />} />
        </Route>
        <Route path="/articles" element={<Articles />}>
          <Route path=":id" element={<Article />} />
        </Route>
      </Routes>
    </div>
  )
}

export default App
