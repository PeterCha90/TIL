import { createAction, createReducer } from "@reduxjs/toolkit"

const addToDo = createAction("ADD")
const deleteToDo = createAction("DELETE")

export const todoReducer = createReducer([{ text: "todo", id: 234 }], {
  [addToDo]: (state, action) => {
    state.push({ text: action.payload, id: Date.now() })
  },
  [deleteToDo]: (state, action) => state.filter((toDo) => toDo.id !== action.payload),
})
