import React from "react"
import store from "./store"
import App from "./components/App"
import ReactDOM from "react-dom/client"
import { Provider } from "react-redux"

const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <Provider store={store}>
    <App />
  </Provider>,
)
