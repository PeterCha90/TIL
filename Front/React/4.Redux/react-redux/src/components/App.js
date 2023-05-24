import React from "react"
import Home from "../routes/Home"
import Detail from "../routes/Detail"
import { HashRouter as Router, Route, Routes, BrowserRouter } from "react-router-dom"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          exact
          path="/"
          element={<Home />}
        ></Route>
        <Route
          path="/:id"
          element={<Detail />}
        ></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
