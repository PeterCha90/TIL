import { combineReducers } from "redux"
import { todoReducer } from "./modules/todo"
import { memoReducer } from "./modules/memo"
import { configureStore } from "@reduxjs/toolkit"

const allReducers = combineReducers({
  todoReducer,
  memoReducer,
})

const store = configureStore({ reducer: allReducers })

export default store
