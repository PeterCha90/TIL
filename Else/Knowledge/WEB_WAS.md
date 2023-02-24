# WEB과 WAS(feat. CGI, WSGI)

Source:
[jimin_lee](https://velog.io/@jimin_lee/Nginx%EC%99%80-Gunicorn-%EB%91%98-%EC%A4%91-%ED%95%98%EB%82%98%EB%A7%8C-%EC%8D%A8%EB%8F%84-%EB%90%A0%EA%B9%8C),
[규도자](https://this-programmer.tistory.com/345),
[pxd-fed-blog](https://pxd-fed-blog.web.app/webserver-was/),
[enujekim](https://www.clien.net/service/board/cm_app/13584876)

- **WEB**은 그냥 Web Server. **WAS**는 Web Application Server.
- 결국 명칭, 이름을 이렇게 붙이는 것에는 다 이유가 있는데 WAS는 왜 Application,
  즉 “웹 서버를 응용”했다고 표현하는지를 이해하면 된다. **핵심은 정적이나 동적이
  나 차이.**

### Web Server

---

- Web Server는 아래와 같이 이렇게 동작한다. 그냥 요청 오면 HTML과 같은 **정적인
  (Static)** 컨텐츠를 사용자에게 전달해준다. 그냥. 딱딱 그 자체. 클라이언트와 채
  팅을 하거나하는 이런 동적인거 절대 불가능하고 그냥 페이지만 띡. 스켈레톤 코드
  같은 느낌.

    <img src="./img/web_1.png" />

- 이런 Web Server들의 종류가 Apache, Nginx, IIS(윈도우 전용 웹서버) 등이 있다.
- 일단 Web Server는 그러니까 약간 단순한 처리만 할 수 있어서, “상황에 따라 변하
  는 정보를 제공할 수는 없다.” 그게 가능한 친구가 WAS. 그래서 보통 Web Server는,
  1.  HTTP Request 요청만 받고
  2.  WAS에게 “도움!!”을 외치고
  3.  WAS가 주는 데이터 돌려주는
  용도로 사용한다.

### Web Application Server

---

- WAS는 WEB과 비교에서 동적이고 유연한 반응을 해줄 수 있다. 어떻게? 들어오는 요
  청에 맞게 실행할 Logic(코드!)을 넣어서 변화는 상황에 대처한 response를 할 수
  있게! 그래서 DB 조회 등 다양한 로직은 WAS가 처리한다.
- 그니까 단순무식한 **Web을 응용(Application)해서 더 유연한 Server를 만들어** 줬
  으니까. → WAS라고 부른다고 이해해도 되겠다.
    <img src="./img/web_2.png" />

- 익숙한 Flask, FastAPI, express 등이 이런 친구들인데, 옛날 거로는 톰캣.

### CGI, Common Gateway Interface

---

- 자 근데, 그럼 여기서 질문/궁금증이 생긴다. 가만생각해보면, 모든 Client의 요청
  은 HTTP로 오는데..? `GET /home.html HTTP/1.1`**과 같은 텍스트로 요청이오는데
  이걸 Flask, Django, FastAPI 같은 Python Framework들은 어떻게 Python으로 이해를
  하며, Node.js Express, Bun.js같은 친구들은 또 어떻게 JS로 이해를 한다는 걸까
  ?**
- 👉🏻 **누군가 변역을 해줄 통역사가 필요한 상황**이다. 이렇게 클라이언트와 서버를
  둘 다 이해할 수 있는 공통된(Common) 영역/관문(Gateway)으로써 통역사 역할을 해
  주는 Interface를 Common Gateway Interface. 줄여서, CGI라고 부른다.
- 요약하면 CGI는 아래 역할을 해주는 진정한 의미에서의 Middleware라고 할 수 있겠
  다.
  - HTTP request → Python/JS 로 서버에 전달.
  - Python/JS response → HTTP로 클라이언트에게 전달.
- 근데 CGI는 요청이 올 때마다, 전체 Python 코드를 다 처음부터 다 실행시켜버린다!
  → 서버가 너무 느리고 효율이 좋지 않다. 그래서 나온게 WSGI

### WSGI, Web Server Gateway Interface.

---

- CGI와 WSGI의 하고자 하는 바는 똑같다! 다만, 위에서 언급한 문제를 해결하기 위해
  서 **WSGI는 Web Server Side와 Application Side 코드를 분리해서, Web Server가
  받은 요청을 건네받아 요청에 따라 필요한 로직만 실행하고 결과를 리턴**하는 방식
  으로 작동한다.
- 알고 있어야할 것은 **WSGI는, Python 통역만 가능한 미들웨어라는 것이다**! 보통
  Gunicorn을 사용하고 uWSGI라는 것도 있다고 한다. Node.js는 node-cgi / fastcgi
  같은 모듈을 express에 설치해서 사용한다!

 <img src="./img/web_3.png" />

### 결론

---

- 그래서 django로 WAS를 구성했다고 하면 아래와 같이 보통 구조를 가져간다.
    <img src="./img/web_4.png" />
    
    - `Web Server`: nginx proxy server, load balancer 역할 
                            (안쓰면 트래픽 많을 경우 터짐)
    - `WAS`: gunicorn - WSGI Middleware 역할 + django

### 그외 알아놓기

---

1. django나 flask는 정확하게 표현하면 Web Application “Framework” 라서, 자체적으
   로 wsgi를 제공해주는 기능도 포함하고 있기 때문에 gunicorn을 따로 사용하지 않
   고도 서비스가 가능! → **Q:** 그럼 굳이 gunicorn은 왜씀? **A:** **session,
   cookie, routing, authentication** 등의 기능을 수행해주기 위해서.(쓰면 개고생
   을 덜할 수 있다)

1. 하나의 Web Server를 띄우고(ex: nginx) 뒤에 여러개의 WAS를 붙이고 Load
   Balancing을 통해서 안정적인 서비스를 할 수도 있다!
