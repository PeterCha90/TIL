import App from "./App"
import React from "react"
import store from "./allReducer"
import { Provider } from "react-redux"
import ReactDOM from "react-dom/client"

const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(
  <Provider store={store}>
    <App />
  </Provider>,
)
