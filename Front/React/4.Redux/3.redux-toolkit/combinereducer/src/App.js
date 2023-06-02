import { useSelector } from "react-redux"

function App() {
  const data = useSelector((state) => state)
  console.log(data)
  console.log(data.memoReducer)
  console.log(data.todoReducer)
  return <div>HI</div>
}

export default App
