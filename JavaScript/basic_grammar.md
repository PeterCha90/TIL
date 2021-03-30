<!--page_number:true-->
<!-- $width: 1059-->
<!-- $height: 1500-->


# Template Literal
* Code

  ```js
  // Template Literal
  function hello(name) {
    return `Hello ${name}!`; // Using backtick.
  }

  console.log(hello("Peter c"));
  ```
* Output

	```
    Hello Peter c! 
	```
<br>

# Arrow Function 

* Code 

	```javascript
    const add = (a, b) => {
      return a + b;
    }

    console.log(add(1,2));

    const add2 = (a, b) => a + b;

    console.log(add2(2,3));
    ```
    
* Output

	```
    3
    5
    ```
---
# Object
* Code

  ```javascript
  const dog = {
    name: '멍멍이',   // key: value
    age: 2, 
    cute: true
  }

  console.log(dog);
  console.log(dog.name);
  console.log(dog.cute);
  ```
* Output

	```
    {name: "멍멍이", age: 2, cute: true}
    멍멍이 
    true
	```
* 필수암기 Object functions, `Object.entries()`, `Object.keys()`
`Object.values()`

  ```javascript
  console.log(Object.entries(dog)); // Array Tree
  console.log(Object.keys(dog)); // ["name", "sound", "age"]
  console.log(Object.values(dog)); // ["멍멍이", 2, true]
  ```

# Destructuring assignment

* Code

  ```javascript
  function print(animal) {
    const {name, age, cute} = animal; // destructuring
    const text = `${name}'s age is ${age} years old, and cute ${cute}ly`
    console.log(text);
  }

  print(dog)
  ```
* Output

	```
    멍멍이's age is 2 years old, and cute truely
	```
    
---
# Function in Object
* Code

  ```javascript
  const dog = {
    name: 'doggy',
    sound: 'bow-wow!',
    say: function say() {
      console.log(this.sound); // this means dog object
    },
    say2(){ // this also works
      console.log(this.sound);
    },
    say3: () => { // this doesn't work. 
                  // arrow-function can't find 'this' operator
      console.log(this.sound);
    }
  }

  const cat = {
    name: 'kitty', 
    sound: 'meow'
  };

  cat.say = dog.say; // cat.say is registered.
  dog.say();
  cat.say(); // this also works
  dog.say2();
  dog.say3();
  ```
* Output

	```
    bow-wow! 
  meow 
  bow-wow! 
  Error in sandbox: 
  TypeError: Cannot read property 'sound' of undefined
	```

---

# Getter

* Code: `get`

  ```javascript
  const numbers = {
    a: 1, 
    b: 2,
    get sum() {
      console.log('sum 함수가 실행됩니다!');
      return this.a + this.b;
    }
  };
  numbers.b = 5;
  console.log(numbers.sum);
  ```
* Output

	```
  sum 함수가 실행됩니다! 
  6
	```
    

# Setter
* Code: `set`
  ```javascript
  const dog = {
    _name: 'doggy',

    set name(value) {
      console.log('이름이 바뀝니다..' + value);
      this._name = value;
    }
  } 
  console.log(dog._name);
  dog.name = '뭉뭉이';
  console.log(dog._name);
  ```
* Output

	```
  doggy 
  이름이 바뀝니다..뭉뭉이 
  뭉뭉이 
	```
    
---

# array - 1

* Code: `[]`, `push`, `length`
  ```javascript
  // array can contain variaus elements
  const array = [1,'g',{},4,5]; 
  const objects = [
    { name: 'doggy'},
    { name: 'kitty'}
  ];

  console.log(array[0]);
  console.log(objects[1])
  console.log(objects.length);

  objects.push({   // add new objects
    name: '멍뭉이'
  })   

  console.log(objects.length);
  ```
* Output

	```
  1
  {name: "kitty"}
  2
  3
	```
    
# for
* Code: `for( ; ; ){} `
  ```javascript
  for (let i =0; i <10; i++){
    console.log(i);
  }
  ```
* Output

	```
    (print 1 to 9)
	```
    
---
# while
* Code: `while (condition) {}`

# for ... of ... 
* Python의 comprehension 같은 느낌
* Code:
	```javascript
    const numbers = [10, 20, 30, 40, 50];
  
  for (let number of numbers) {
        console.log(number);
  }
  // 10, 20, 30, 40, 50
    ```
    
# for ... in ...
* 객체에 대한 반복에 주로 사용
* Code:

  ```javascript
  const dog = {
      name: '멍멍이',
      sound: '멍멍',
      age: 2
  };

  for (let key in dog) {
      console.log(key)
  } // 'name', 'sound', 'age'
 
  // with template literal
  for (let key in dog) {
      console.log(`${key}: ${dog[key]}`);
  }
  ```