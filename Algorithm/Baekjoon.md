<!--page_number:true-->
<!-- $width: 1059-->
<!-- $height: 1500-->


# Baekjoon Online Judge

### [음계](https://www.acmicpc.net/problem/2920)

* 문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

	1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

	연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

* 입력
	첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

* 출력
	첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

  예제 1 
  > 1 2 3 4 5 6 7 8 
  > ascending

  예제 2 
  > 8 7 6 5 4 3 2 1
  > descending

  예제 3 
  > 8 1 7 2 6 3 5 4
  mixed
  
---

* Code:

  ```python
  data = list(map(int,input().split()))

  count, temp = 0, 0
  for item in data:
      count = count + 1 if temp < item else count 
      temp = item

  if count == 8:
      print('ascending')
  elif count == 1:
      print('descending')
  else:
      print('mixed')
  ```
  
  <img src="img/1.png" width=100%>
  
  <br><br><br><br><br><br><br><br><br><br><br><br><br>
  
---
### [블랙잭](https://www.acmicpc.net/problem/2798)

* **문제**
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

	한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

	김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

	이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

	N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

* **입력**
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

	합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

* **출력**
	첫째 줄에 M을 넘지 않고 M에 최대한 가까운 카드 3장의 합을 출력한다.

  예제 
  > 10 500
  > 93 181 245 214 315 36 185 138 216 295

  출력: 
  > 497
  > 
---

* Code:

  ```python
  a = list(map(int, input().split(' ')))
  cards = list(map(int, input().split(' ')))
  num_of_cards = a[0]
  maximum = a[1]

  total, result = 0, 0
  # C(n, 3)
  for i in range(0, num_of_cards):
      for j in range(i+1, num_of_cards):
          for k in range(j+1, num_of_cards):
              total = cards[i] + cards[j] + cards[k]
              if total > result and total <= maximum:
                  result = total
  print(result)
  ```
  <img src="img/2.png" width=100%>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

---

### [스택 수열](https://www.acmicpc.net/problem/1874)

* **문제**
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

	1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

* **입력**
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

* **출력**
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.


* **예제 1** - 아래가 세로로 숫자 하나에 한 줄씩 입력됐다고 하면
  ``` shell
  8 4 3 6 8 7 5 2 1
  ```
	 출력 - 얘도 세로로 출력
  ```shell
  + + + + - - + + - + + - - - - - 
  ```
* **예제 2** - 마찬가지
  ``` shell
  5 1 2 5 3 4
  ```
  출력 
  ```shell
  No
  ```
---

* Code:

  ```python
  n = int(input())

  count = 1 
  stack = []
  result = []

  for i in range(n):   # n번 입력을 받을 때 마다, 아래를 수행
      data = int(input())
      while count <= data:
          stack.append(count) # 실제로 숫자를 저장
          count += 1
          result.append('+')
      if stack[-1] == data:# 젤 큰 놈이다 -> 내림차순 pop 가능
          stack.pop()
          result.append('-')
      else:
          print('NO')
          exit(0)

  print('\n'.join(result))
	```
    <img src="img/3.png" width=100%>

    

