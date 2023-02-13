# Pure Redux

### Install

---

- 아래 명령어로 설치 및 실행.

```bash
$ npx create-react-app vanilla-redux
$ yarn add redux
or
$ npm install redux
$ yarn start
```

### Simple Counter

> **Keywords:** `createStore` , `.getState()` , `.subscribe()`

---

- public 폴더 안에 index.html을 아래처럼 수정해보자.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <title>Vanilla Redux</title>
  </head>
  <body>
    <button id="add">Add</button>
    <span>0</span>
    <button id="minus">Minus</button>
  </body>
</html>
```

- 그 다음으로 src 폴더 아래에 index.js만 아래와 같이 수정해보자. Redux에서 핵심이 되는 개념 중 하나인 `Store` 를 이해할 수 있는 예시다.

**index.js**

- **Reducer 함수인 countModifier를 `createStore()`에 전달**하면, 반환받게 되는 값은 `**.dispatch()`를 통해 설정한 값에 유일하게 접근할 수 있는 요소\*\*가 된다는게 핵심.
  - `.getState()` 통해서 count 값을 반환 받을 수 있다.
  - `.subscritbe()` 에 onChange함수를 등록함으로써, count의 상태(status)에 변화가 생겼을 때마다, onChange를 호출해, number에도 바뀐 값을 반영해준다.

```jsx
import { createStore } from 'redux'

const add = document.getElementById('add')
const minus = document.getElementById('minus')
const number = document.querySelector('span')

const ADD = 'ADD'
const MINUS = 'MINUS'

const countModifier = (count = 0, action) => {
  switch (action.type) {
    case 'ADD':
      return count + 1
    case 'MINUS':
      return count - 1
    default:
      return count
  }
}

const countStore = createStore(countModifier)

const onChange = () => {
  number.innerText = countStore.getState()
}

countStore.subscribe(onChange)

const handleAdd = () => {
  countStore.dispatch({ type: ADD })
}

const handleMinus = () => {
  countStore.dispatch({ type: MINUS })
}

add.addEventListener('click', handleMinus)
minus.addEventListener('click', handleAdd)
```
