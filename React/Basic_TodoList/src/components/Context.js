import React, { useReducer, createContext, useContext, useRef } from 'react'

const initialTodos = [
  {
    id: 1,
    text: '프로젝트 생성하기',
    done: true,
  },
  {
    id: 2,
    text: '컴포넌트 스타일링하기',
    done: true,
  },
  {
    id: 3,
    text: 'Context 만들기',
    done: false,
  },
  {
    id: 4,
    text: '기능 구현하기',
    done: false,
  },
]

// Reducer 함수 만들기
function Reducer(state, action) {
  switch (action.type) {
    case 'CREATE':
      return state.concat(action.todo)
    case 'TOGGLE':
      return state.map((todo) =>
        todo.id === action.id ? { ...todo, done: !todo.done } : todo,
      )
    case 'REMOVE':
      return state.filter((todo) => todo.id !== action.id)
    default:
      throw new Error(`Unhandled action type: ${action.type}`)
  }
}

const TodoStateContext = createContext()
const TodoDispatchContext = createContext()
const TodoNetIdContext = createContext()

export function TodoProvider({ children }) {
  const [state, dispatch] = useReducer(Reducer, initialTodos)
  const nextId = useRef(5)
  return (
    <TodoStateContext.Provider value={state}>
      <TodoDispatchContext.Provider value={dispatch}>
        <TodoNetIdContext.Provider value={nextId}>
          {children}
        </TodoNetIdContext.Provider>
      </TodoDispatchContext.Provider>
    </TodoStateContext.Provider>
  )
}

// 이렇게 export를 해버려서 useContext를 코드에서 쓸 필요도 없이
// Context를 사용할 수 있게 해주구나.
// 이 것도 Custom Hook이라면 Custom Hook이지!
export function useTodoState() {
  const context = useContext(TodoStateContext)
  // 해당 context.Provider로 감싸지 않았을 경우 에러 발생.
  if (!context) {
    throw new Error('Cannot find TodoProvider')
  }
  return context
}

export function useTododispatch() {
  const context = useContext(TodoDispatchContext)
  if (!context) {
    throw new Error('Cannot find TodoProvider')
  }
  return context
}

export function useTodoNextId() {
  const context = useContext(TodoNetIdContext)
  if (!context) {
    throw new Error('Cannot find TodoProvider')
  }
  return context
}
