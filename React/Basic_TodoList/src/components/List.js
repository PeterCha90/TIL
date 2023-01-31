import React from 'react'
import Item from './Item'
import styled from 'styled-components'
import { useTodoState } from './Context'

const ListBlock = styled.div`
  flex: 1;
  padding: 20px 32px;
  padding-bottom: 48px;
  overflow-y: auto;
`

function List() {
  const todos = useTodoState()

  return (
    <ListBlock>
      {todos.map((todo) => (
        <Item key={todo.id} id={todo.id} text={todo.text} done={todo.done} />
      ))}
    </ListBlock>
  )
}

export default List
