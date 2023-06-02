import { createAction, createReducer } from "@reduxjs/toolkit"

const addMemo = createAction("ADD")
const deleteMemo = createAction("DELETE")

export const memoReducer = createReducer([{ text: "memo", id: 123 }], {
  [addMemo]: (state, action) => {
    state.push({ text: action.payload, id: Date.now() })
  },
  [deleteMemo]: (state, action) => state.filter((toDo) => toDo.id !== action.payload),
})
