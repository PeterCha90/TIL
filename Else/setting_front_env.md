# How to set front-end environment

### for React & NextJS

- **node.js**(필수) - [node 설치](https://nodejs.org/ko/download)
- **yarn** (설치:`npm install -g yarn` 추천), **vscode**(추천)
- npx (설치: `npm install npx -g`)
- Project를 `npx create-reate-app` 으로 만들면, 폴더가 생기고 그 폴더 안에서
  `yarn start` / `npm start`

* React App 개발 시작하기.
  ```Shell
  $ npx create-react-app project-name
  $ cd project-name
  $ yarn start
  // localhost:3000 에 브라우저가 뜸
  ```
  * typescript를 사용하고 싶다면,
    ```Shell
    $ npx create-react-app my-app --template typescript
    ```
  
* NextJS App 개발 시작하기
  ```Shell
  $ npx create-next-app@latest --typescript
  ```
  - 위 명령어를 치면, 프로젝트 생성과정에서 프로젝트 명을 알려달라고 하고 그 폴
    더로 들어가서 npm run dev 를 하면 http://localhost:3000 이 열릴 것이다. 클릭
    해보면 Next.js 화면을 볼 수 있다!
  - `--typescript`는 타입스크립트로 작업하고 싶을 때 옵션으로 사용.
