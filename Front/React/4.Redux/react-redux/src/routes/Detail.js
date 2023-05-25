import React from "react"
import { connect } from "react-redux"
import { useParams } from "react-router-dom"

function Detail({ toDos }) {
  // given by the react-router-dom
  const id = useParams().id
  const toDo = toDos.find((toDo) => toDo.id === parseInt(id))

  return (
    <>
      <h1>{toDo?.text}</h1>
      <h3>Created at: {toDo?.id}</h3>
    </>
  )
}

function mapStateToProps(state, ownProps) {
  return { toDos: state }
}

export default connect(mapStateToProps)(Detail)
