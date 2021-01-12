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
---

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

