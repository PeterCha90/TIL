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

<br>

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