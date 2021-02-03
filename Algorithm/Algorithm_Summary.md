<!--page_number:true-->
<!-- $width: 1059-->
<!-- $height: 1500-->


# Algorithm

## Bubble Sort

* 앞에서부터 **두 개씩 크기비교를 해서, 두 번째 요소가 더 크면 첫 번째 요소와 자리를 Swap. 아니면 continue. 그렇게 한 번 돌면, 제일 마지막에 가장 큰 값이 위치**하기 때문에 비교대상이 하나씩 줄게 되는 구조. 
* Swap이 한 번도 일어나지 않았다?! $\to$ 이미 정렬이 되어있는 경우! Best Case로 $O(n)$
* 최악의 경우 $O(n^2)$

  ```python
  def bubblesort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        
        if swap == False:
            break
    return data
  ```

<br>

## Selection Sort

* 젤 첫 번째 자리부터 기준점으로 선점해서, 나머지 요소들 중에 **가장 작은 값을 선정(Selection) 젤 첫 번째 자리와 Swap**. 그 다음 두번째 자리가 기준점이 되고, 또 나머지 요소들 중에 가장 작은 값을 찾아서 Swap. 
* 그렇게 가장 작은 값이 순차적으로 오게 만드는 Sorting Algorithm
* 시간 복잡도 $O(n^2)$

---
* Code
  ```python
  def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data
  ```


## Insertion Sort 
* **기준은 두 번째 요소부터 시작**한다. 기준은 **자신의 바로 밑에 있는 요소와 값을 비교하고, 더 큰 요소가 더이상 나오지 않을 때까지 비교를 계속**한다.
* 자신보다 더 작은 요소가 나오면 그 앞이 자기 자리라는 뜻이라서 그 곳으로 삽입(Insertion)한다는 개념. 그렇게 기준을 한 자리씩 옮겨가면서 정리하면 Sorting 완료.
* Best Case - 이미 정렬돼있을 경우, $O(n)$, 최악의 경우 $O(n^2)$

  ```python
  code here

  ```

---
## 공간복잡도 (Space Complexity)

* $S(P) = c + S_p(n)$
	* $c$ : 고정 공간 (변수 개수)
	* $S_p(n)$	: 가변 공간


	> 빅 오 표기법을 생각해 볼 때, 고정 공간은 상수이므로 공간 복잡도는 가변 공간에 좌우됨.

* 아래와 같은 재귀용법의 경우, 재귀함수 호출과 함께 $n$이라는 변수가 계속 생기기 때문에 공간복잡도는 $O(n)$.
  ```python
  def factorial(n):
  if n > 1:
      return n * factorial(n-1)
  else:
      return 1
  ```
  
<br>

## 재귀 용법 (Recursive call)
* **함수가 Input에 따른 Output을 살펴보았을 때, 특정 패턴을 보이는 경우** 재귀함수로 만들기 쉽다.
* 재귀 호출은 **스택의 전형적인 예**. Python에서 재귀 함수는 깊이가(한번에 호출되는) 1000회 이하여야 한다. 
* 재귀 호출의 일반적인 형태

  ```python
  def function(입력):
      if 입력 > 일정값:
          return function(입력 - 1)
      else:
          return 일정값, 입력값, 또는 특정값
  또는,

  def function(입력):
      if 입력 <= 일정값:
          return 일정값, 입력값, 또는 특정값
      return function(입력값보다 작은 값)
  ```
  
  
---
## 동적 계획법(Dynamic Programming)과 분할 정복 (Divide and Conquer)

### 동적계획법. DP.
* **상향식 접근법**. 가장 최하위 해답을 먼저 구한 후, 이를 저장해서 해당 결과값을 이용해서 상위 문제를 풀어가는 방식.
* **핵심은 Memorization 기법** - 프로그램 실행 시 결과를 저장해놔서, 다시 같은 문제를 계산하지 않도록 하여, 전체 실행 속도를 빠르게 하는 기술. 
* 가장 대표적인 예가, 피보나치 수열. 그래서,
	> 1) 구하는 마지막 데이터까지의 개수에 해당하는 공간을 먼저 할당.
	> 2) 제일 밑에서 부터 계산을 해서 각각의 해당 위치에 싹 다 저장
	> 3) 젤 마지막 원하는 결과값 pop.
	
	순서로 진행된다. 

### 분할 정복
* 문제를 나눌 수 없을 때까지 나누어서 각각 풀면서 다시 합병한다. 이 부분은 DP와 같은 개념이다. 
* 하지만 **차이점은 하향식 접근법**이라는 것. <u>상위의 해답을 구하기 위해</u>서 아래로 내려간다. 

### DP와 분할정복의 차이점
* **동적계획법**
	* **부분 문제는 중복되어, 상위 문제 해결 시 재활용**된다. 
	* Memorization 기법 사용 - 중복돼서 재활용해야 할테니까. 
* **분할 정복**
	* **부분 문제는 서로 중복되지 않는다.**
	* Memorization 기법 사용 안함 - 중복되지 않으니까 당연히 그런듯. 
---
## Quick Sort
* 대표적인 Divide-and-Conquer, 분할 정복 알고리즘.
* **Pivot을 정하고, Pivot보다 작으면 왼쪽, 크면 오른쪽으로 다 모은 뒤에 각각 재귀적으로 또 Quick sort를 태우고** 마지막 leaf node부터 return 되는 list를 싹다 모으면 정렬이 완성되는.

	```python
    def qsort(data):
        if len(data) <= 1:
        	return data
        
        pivot = data[0]
        left = [item for item in data if item <= pivot]
        right = [item for item in data if item > pivot]
        return qsort(left) + [pivot] + qsort(right)
    ```
    
* **시간 복잡도**:
	$O(n\text{log}n)$, 최악의 경우: $O(n^2)$
* **공간 복잡도**:
	주어진 데이터 공간 외에 다른 공간은 쓰지 않기 때문에 $O(n)$
    
<br>

---
## Merge Sort

* 받은 데이터의 가운데를 기준으로 좌우를 나누고, 재귀적으로 젤 밑에서부터 Merge를 할 때, 크기가 작은 순서대로 정렬해서 반환하는 형태 

	```python
    def merge_sort(data):
      if len(data) == 1:
          return data
      medium = int(len(data)/2)
      left = merge_sort(data[:medium])
      right = merge_sort(data[medium:])
      return merge(left, right)
      
    def merge(left, right):
      result = []
      left_idx, right_idx = 0, 0

      while(left_idx != len(left) or right_idx != len(right)):
          if left[left_idx] < right[right_idx]:
              result.append(left[left_idx])
              left_idx += 1
              if left_idx == len(left):
                  for idx in range(right_idx, len(right)):
                      result.append(right[idx])
                  break
          else:
              result.append(right[right_idx])
              right_idx += 1
              if right_idx == len(right):
                  for idx in range(left_idx, len(left)):
                      result.append(left[idx])
                  break
      return result
    ```
    
* **시간 복잡도**: 항상 $O(n\text{log}n)$ 보장.
* **공간 복잡도**:
	Depth마다, $2^i$개의 공간이 생기는데, 이 Depth가 $\text{log}n$개기 때문에, 
    $$\sum_{i =1}^{\text{log}n}2^i = 2^{\text{log}n} + \cdots + 2 + 1 $$
    그러니까 $O(n).$
    
---

# BFS, DFS
* **B**readth **F**irst **S**earch - 같은 레벨에 있는 노드들 먼저 순회
* **D**epth **F**irst **S**earch - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 그 다음 노드를 타고 내려가는 방식. 

## BFS

```python
def bfs(graph, start_node):
    visited = []
    need_visit = []
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
```

<br>

## DFS
```python
def dfs(graph, start_node):
    visited, need_visit = [], []
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
```

* 차이점은 **BFS는 need_visit에서 pop을 앞에서 하면서 큐를 구현**하는 것이고 **DFS는 pop을 뒤에서 하면서 스택을 구현**하는 것이다.
* 시간복잡도는 둘다 O(V+E). graph는 Node와 Edge가 key-value로 구성.

---

# Greedy algorithm
- Greedy algorithm 또는 탐욕 알고리즘 이라고 불리움
- 최적의 해에 가까운 값을 구하기 위해 사용됨
- 여러 경우 중 하나를 결정해야할 때마다, **매순간 최적이라고 생각되는 경우를 선택**하는 방식으로 진행해서, 최종적인 값을 구하는 방식

### 2. 탐욕 알고리즘 예
### 문제1: 동전 문제
  - 지불해야 하는 값이 4720원 일 때 1원 50원 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오.
    - 가장 큰 동전부터 최대한 지불해야 하는 값을 채우는 방식으로 구현 가능
    - 탐욕 알고리즘으로 매순간 최적이라고 생각되는 경우를 선택하면 됨
    
      ```python
      coin_list = [500, 100, 50, 1]

      def min_coin_count(value, coin_list):
          total_coin_count = 0
          details = list()
          coin_list.sort(reverse=True)
          for coin in coin_list:
              coin_num = value // coin
              total_coin_count += coin_num
              value -= coin_num * coin
              details.append([coin, coin_num])
          return total_coin_count, details
      ```
      
---

### 문제2: 부분 배낭 문제 (Fractional Knapsack Problem)
  - 무게 제한이 k인 배낭에 최대 가치를 가지도록 물건을 넣는 문제
    - 각 물건은 무게(w)와 가치(v)로 표현될 수 있음
    - 물건은 쪼갤 수 있으므로 물건의 일부분이 배낭에 넣어질 수 있음, 그래서 Fractional Knapsack Problem 으로 부름
    - Fractional Knapsack Problem 의 반대로 물건을 쪼개서 넣을 수 없는 배낭 문제도 존재함 (0/1 Knapsack Problem 으로 부름)
  <img src="https://www.fun-coding.org/00_Images/knapsack.png">
  
#### Example

```python
data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()
    
    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details
```   


---
### 3. 탐욕 알고리즘의 한계
- 탐욕 알고리즘은 근사치 추정에 활용
- 반드시 최적의 해를 구할 수 있는 것은 아니기 때문
- 최적의 해에 가까운 값을 구하는 방법 중의 하나임

### 예
<img src="https://www.fun-coding.org/00_Images/greedy.png" width=300>

- '시작' 노드에서 시작해서 가장 작은 값을 찾아 leaf node 까지 가는 경로를 찾을 시에
  - Greedy 알고리즘 적용시 시작 -> 7 -> 12 를 선택하게 되므로 7 + 12 = 19 가 됨 
  - 하지만 실제 가장 작은 값은 시작 -> 10 -> 5 이며, 10 + 5 = 15 가 답

---
# 최단 경로 알고리즘의 이해
### 1. 최단 경로 문제란?
- 최단 경로 문제란 두 노드를 잇는 가장 짧은 경로를 찾는 문제임
- 가중치 그래프 (Weighted Graph) 에서 간선 (Edge)의 가중치 합이 최소가 되도록 하는 경로를 찾는 것이 목적

### 최단 경로 문제 종류
1. 단일 출발 및 단일 도착 (single-source and single-destination shortest path problem) 최단 경로 문제
  - 그래프 내의 특정 노드 u 에서 출발, 또다른 특정 노드 v 에 도착하는 가장 짧은 경로를 찾는 문제
2. 단일 출발 (single-source shortest path problem) 최단 경로 문제
  - 그래프 내의 특정 노드 u 와 그래프 내 다른 모든 노드 각각의 가장 짧은 경로를 찾는 문제
  > 따지고 보면 굉장히 헷깔릴 수 있으므로 명확히 하자면, 
  > 예를 들어 A, B, C, D 라는 노드를 가진 그래프에서 특정 노드를 A 라고 한다면,
  > A 외 모든 노드인 B, C, D 각 노드와 A 간에 (즉, A - B, A - C, A - D) 각각 가장 짧은 경로를 찾는 문제를 의미함
  
3. 전체 쌍(all-pair) 최단 경로: 그래프 내의 모든 노드 쌍 (u, v) 에 대한 최단 경로를 찾는 문제

### 2. 최단 경로 알고리즘 - 다익스트라 알고리즘
- 다익스트라 알고리즘은 위의 최단 경로 문제 종류 중, 2번에 해당
  - 하나의 정점에서 다른 모든 정점 간의 각각 **가장 짧은 거리**를 구하는 문제

---

### 다익스트라 알고리즘 로직
- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법
- 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사
  - 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트
  
  >  다익스트라 알고리즘의 다양한 변형 로직이 있지만, 가장 개선된 우선순위 큐를 사용하는 방식에 집중해서 설명하기로 함

- 우선순위 큐를 활용한 다익스트라 알고리즘
  - **우선순위 큐는 MinHeap** 방식을 활용해서, **현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨**

  1) 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
     - 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)
     - 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음 


  2) 우선순위 큐에서 노드를 꺼냄
     - 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
     - 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.
     - 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
     - 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.

---
- 우선순위 큐를 활용한 다익스트라 알고리즘
	2) 우선순위 큐에서 노드를 꺼냄 (계속)
       - 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
       - 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음

  3) 2번의 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복한다.

### 3. 예제로 이해하는 다익스트라 알고리즘 (우선순위 큐 활용)
<center><img src="https://www.fun-coding.org/00_Images/dijkstra.png" width=300></center>

### 1단계: 초기화
- 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장
   - 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)
   - 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음
   
 <img src="https://www.fun-coding.org/00_Images/dijkstra_initial.png">
 
---
### 2단계: 우선순위 큐에서 추출한 (A, 0) [노드, 첫 노드와의 거리] 를 기반으로 인접한 노드와의 거리 계산
- 우선순위 큐에서 노드를 꺼냄
     - 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐
     - 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.
     - 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.
     - 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.
       - 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨
       - 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음
       
	> 이전 표에서 보듯이, 첫 정점 이외에 모두 inf 였었으므로, 첫 정점에 인접한 노드들은 모두 우선순위 큐에 들어가고, 첫 정점과 인접한 노드간의 거리가 배열에 업데이트됨

	<img src="https://www.fun-coding.org/00_Images/dijkstra_1st.png">
    
---
### 3단계: 우선순위 큐에서 (C, 1) [노드, 첫 노드와의 거리] 를 기반으로 인접한 노드와의 거리 계산
- 우선순위 큐가 MinHeap(최소 힙) 방식이므로, 위 표에서 넣어진 (C, 1), (D, 2), (B, 8) 중 (C, 1) 이 먼저 추출됨 (pop)
- 위 표에서 보듯이 1단계까지의 A - B 최단 거리는 8 인 상황임
  - A - C 까지의 거리는 1, C 에 인접한 B, D에서 C - B는 5, 즉 A - C - B 는 1 + 5 = 6 이므로, A - B 최단 거리 8보다 더 작은 거리를 발견, 이를 배열에 업데이트
    - 배열에 업데이트했으므로 B, 6 (즉 A에서 B까지의 현재까지 발견한 최단 거리) 값이 우선순위 큐에 넣어짐
  - C - D 의 거리는 2, 즉 A - C - D 는 1 + 2 = 3 이므로, A - D의 현재 최단 거리인 2 보다 긴 거리, 그래서 D 의 거리는 업데이트되지 않음
  <br>
	<img src="https://www.fun-coding.org/00_Images/dijkstra_2nd.png">    
    
### 4단계: 우선순위 큐에서 (D, 2) [노드, 첫 노드와의 거리] 를 기반으로 인접한 노드와의 거리 계산
- 지금까지 접근하지 못했던 E와 F 거리가 계산됨
  - A - D 까지의 거리인 2 에 D - E 가 3 이므로 이를 더해서 E, 5
  - A - D 까지의 거리인 2 에 D - F 가 5 이므로 이를 더해서 F, 7
  <br>
  <img src="https://www.fun-coding.org/00_Images/dijkstra_3rd.png">
  
---

### 5단계: 우선순위 큐에서 (E, 5) [노드, 첫 노드와의 거리] 를 기반으로 인접한 노드와의 거리 계산
- A - E 거리가 5인 상태에서, E에 인접한 F를 가는 거리는 1, 즉 A - E - F 는 5 + 1 = 6, 현재 배열에 A - F 최단거리가 7로 기록되어 있으므로, F, 6 으로 업데이트
  - 우선순위 큐에 F, 6 추가

<img src="https://www.fun-coding.org/00_Images/dijkstra_3-2th.png">


### 6단계: 우선순위 큐에서 (B, 6), (F, 6) 를 순차적으로 추출해 각 노드  기반으로 인접한 노드와의 거리 계산
- 예제의 방향 그래프에서 B 노드는 다른 노드로 가는 루트가 없음 
- F 노드는 A 노드로 가는 루트가 있으나, 현재 A - A 가 0 인 반면에 A - F - A 는 6 + 5 = 11, 즉 더 긴 거리이므로 업데이트되지 않음

<img src="https://www.fun-coding.org/00_Images/dijkstra_4th.png">

---

### 7단계: 우선순위 큐에서 (F, 7), (B, 8) 를 순차적으로 추출해 각 노드  기반으로 인접한 노드와의 거리 계산
- A - F 로 가는 하나의 루트의 거리가 7 인 상황이나, 배열에서 이미 A - F 로 가는 현재의 최단 거리가 6인 루트의 값이 있는 상황이므로, 더 긴거리인 F, 7 루트 기반 인접 노드까지의 거리는 계산할 필요가 없음, 그래서 계산없이 스킵함
  - 계산하더라도 A - F 거리가 6인 루트보다 무조건 더 긴거리가 나올 수 밖에 없음
- B, 8 도 현재 A - B 거리가 6이므로, 인접 노드 거리 계산이 필요 없음. 

> 우선순위 큐를 사용하면 불필요한 계산 과정을 줄일 수 있음
> 

<img src="https://www.fun-coding.org/00_Images/dijkstra_5th.png">

### 우선순위 큐 사용 장점
- 지금까지 발견된 가장 짧은 거리의 노드에 대해서 먼저 계산
- 더 긴 거리로 계산된 루트에 대해서는 계산을 스킵할 수 있음