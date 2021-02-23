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

---

* Dijkstra algorithm

  ```python
  import heapq
  
  def dijkstra(graph, start, end):
      
      distances = {vertex: [float('inf'), start] for vertex in graph}
      distances[start] = [0, start]
      queue = []
      heapq.heappush(queue, [distances[start][0], start])

      while queue:
          current_distance, current_vertex = heapq.heappop(queue)
          if distances[current_vertex][0] < current_distance:
              continue

          for adjacent, weight in graph[current_vertex].items():
              distance = current_distance + weight
   
              if distance < distances[adjacent][0]:
                  distances[adjacent] = [distance, current_vertex]
                  heapq.heappush(queue, [distance, adjacent])

      path = end
      path_output = end + '<-'
      while distances[path][1] != start:
          path_output += distances[path][1] + '<-'
          path = distances[path][1]
      path_output += start
      print (path_output, "Shortest cost: "+ str(distances[end][0]))
      return distances
  # 방향 그래프
  mygraph = {
      'A': {'B': 8, 'C': 1, 'D': 2},
      'B': {},
      'C': {'B': 5, 'D': 2},
      'D': {'E': 3, 'F': 5},
      'E': {'F': 1},
      'F': {'A': 5}
  }

  print(dijkstra(mygraph, 'A', 'C'))
  ```    
* Output 
	> C<-A Shortest cost: 1
{'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 'E']}

---

### 5. 시간 복잡도
- 위 다익스트라 알고리즘은 크게 다음 두 가지 과정을 거침
  - 과정1: 각 노드마다 인접한 간선들을 모두 검사하는 과정
  - 과정2: 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop)하는 과정
  
- 각 과정별 시간 복잡도
  - 과정1: 각 노드는 최대 한 번씩 방문하므로 (첫 노드와 해당 노드간의 갈 수 있는 루트가 있는 경우만 해당), 그래프의 모든 간선은 최대 한 번씩 검사
    - 즉, 각 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E) 시간이 걸림, E 는 간선(edge)의 약자

  - 과정2: 우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 경우, 우선순위 큐에 노드/거리 정보를 넣고, 삭제하는 과정이 최악의 시간이 걸림
    - 우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 시나리오는 그래프의 모든 간선이 검사될 때마다, 배열의 최단 거리가 갱신되고, 우선순위 큐에 노드/거리가 추가되는 것임
    - 이 때 추가는 각 간선마다 최대 한 번 일어날 수 있으므로, 최대 O(E)의 시간이 걸리고, O(E) 개의 노드/거리 정보에 대해 우선순위 큐를 유지하는 작업은 $O(log{E})$ 가 걸림
      - 따라서 해당 과정의 시간 복잡도는 $O(Elog{E})$ 
    
### 총 시간 복잡도
  - 과정1 + 과정2 = O(E) + $O(Elog{E})$  = $O(E + Elog{E}) = O(Elog{E})$
  
### 참고: 힙의 시간 복잡도
- depth (트리의 높이) 를 h라고 표기한다면,
- n개의 노드를 가지는 heap 에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로  h=log2n  에 가까우므로, 시간 복잡도는  O(logn)

---

# 최소 신장 트리의 이해

### 1. 신장 트리 란?
- Spanning Tree, 또는 신장 트리 라고 불리움 (Spanning Tree가 보다 자연스러워 보임)
- 원래의 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프
- 신장 트리의 조건
  - 본래의 그래프의 모든 노드를 포함해야 함
  - 모든 노드가 서로 연결
  - 트리의 속성을 만족시킴 (사이클이 존재하지 않음)
  
  <img src="https://www.fun-coding.org/00_Images/spanningtree.png">
  
### 2. 최소 신장 트리 
- Minimum Spanning Tree, MST 라고 불리움
- 가능한 Spanning Tree 중에서, 간선의 가중치 합이 최소인 Spanning Tree를 지칭함

<img src="https://www.fun-coding.org/00_Images/mst.png" width=400>

---

### 3. 최소 신장 트리 알고리즘
- 그래프에서 최소 신장 트리를 찾을 수 있는 알고리즘이 존재함
- 대표적인 최소 신장 트리 알고리즘
  - Kruskal’s algorithm (크루스칼 알고리즘), Prim's algorithm (프림 알고리즘)

### 4. 크루스칼 알고리즘 (Kruskal's algorithm)
1. 모든 정점을 독립적인 집합으로 만든다.
2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
3. **두 정점의 최상위 정점을 확인하고**, 서로 다를 경우 두 정점을 연결한다. (최소 신장 트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임)

> 탐욕 알고리즘을 기초로 하고 있음 (당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)
> 
<img src="https://www.fun-coding.org/00_Images/kruscal_internal1.png" width=650>

---

<img src="https://www.fun-coding.org/00_Images/kruscal_internal2.png" width=800>

### 5. Union-Find 알고리즘
- **Disjoint Set을 표현할 때 사용하는 알고리즘**으로 트리 구조를 활용하는 알고리즘
- 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 (합칠 때) 사용
- Disjoint Set이란
  - 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
  - 공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
  - Disjoint Set = 서로소 집합 자료구조

1. 초기화
   - n 개의 원소가 개별 집합으로 이뤄지도록 초기화
<img src="https://www.fun-coding.org/00_Images/initial_findunion.png" width=400>

---

2. Union
   - 두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬
<img src="https://www.fun-coding.org/00_Images/union_findunion.png" width=600>

3. Find
   - 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소 (즉, 루트 노드)를 확인
<img src="https://www.fun-coding.org/00_Images/find_findunion.png" width=500>

### Union-Find 알고리즘의 고려할 점
- Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수 있음.
- 이 때는 Find/Union 시 계산량이 O(N) 이 될 수 있으므로, 해당 문제를 해결하기 위해, **union-by-rank, path compression 기법을 사용**함 

	<center><img src="https://www.fun-coding.org/00_Images/worst_findunion.png" width=200></center>

---
### union-by-rank 기법
- 각 트리에 대해 높이(rank)를 기억해 두고,
- Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임 (즉, 높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 함)
<img src="https://www.fun-coding.org/00_Images/unionbyrank_findunion.png" width=700>

- 높이가 h - 1 인 두 개의 트리를 합칠 때는 한 쪽의 트리 높이를 1 증가시켜주고, 다른 쪽의 트리를 해당 트리에 붙여줌
<img src="https://www.fun-coding.org/00_Images/unionbyranksame_findunion.png" width=700>

- 초기화시, 모든 원소는 높이(rank) 가 0 인 개별 집합인 상태에서, 하나씩 원소를 합칠 때, union-by-rank 기법을 사용한다면,
  - 높이가 h 인 트리가 만들어지려면, 높이가 h - 1 인 두 개의 트리가 합쳐져야 함
  - 높이가 h - 1 인 트리를 만들기 위해 최소 n개의 원소가 필요하다면, 높이가 h 인 트리가 만들어지기 위해서는 최소 2n개의 원소가 필요함
  - 따라서 union-by-rank 기법을 사용하면, union/find 연산의 시간복잡도는 O(N) 이 아닌, $O(log{N})$ 로 낮출 수 있음
---

### path compression
- Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
- Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음

<center><img src="https://www.fun-coding.org/00_Images/pathcompression_findunion.png" width=400></center>

- union-by-rank 와 path compression 기법 사용시 시간 복잡도는 다음 계산식을 만족함이 증명되었음
  - $O(M log^*{N})$
  - $log^*{N}$ 은 다음 값을 가짐이 증명되었음
    - N이 $2^{65536}$ 값을 가지더라도, $log^*{N}$ 의 값이 5의 값을 가지므로, 거의 O(1), 즉 상수값에 가깝다고 볼 수 있음

  <center>
  
  <div style="text-align:left">
  <table>
    <tr>
      <th style="text-align:center">N</th>
      <th style="text-align:center"> log*N</th>
    </tr>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">0</td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">1</td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">2</td>
    </tr>
    <tr>
      <td style="text-align:left">16</td>
      <td style="text-align:left">3</td>
    </tr>
    <tr>
      <td style="text-align:left">65536</td>
      <td style="text-align:left">4</td>
    </tr>
    <tr>
      <td style="text-align:left">2^{65536}</td>
      <td style="text-align:left">5</td>
    </tr>
  </table>
  </div>
  </center>