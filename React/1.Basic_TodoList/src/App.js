import React from 'react'
import List from './components/List'
import Create from './components/Create'
import TodoHead from './components/Head'
import Template from './components/Template'
import { createGlobalStyle } from 'styled-components'
import { TodoProvider } from './components/Context'

const GlobalStyle = createGlobalStyle`
  body {
    background: #e9ecef;
  }
`

function App() {
  return (
    <>
      <TodoProvider>
        <GlobalStyle />
        <Template>
          <TodoHead />
          <List />
          <Create />
        </Template>
      </TodoProvider>
    </>
  )
}

export default App
