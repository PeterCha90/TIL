<!--page_number:true-->
<!-- $width: 1059-->
<!-- $height: 1500-->


# Data Structure

#### Teacher: 이준희

## Queue
  * 운영체제에서 **멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현**하기 위해 많이 사용됨 
  * **LifoQueue**, **PriorityQueue**를 Python queue 모듈에서 제공. 
  * **Enqueue, Dequeue**


## Stack 
  * 운영체제에서 **Process가 재귀적으로 함수를 실행하는 방식**
  * **Push, Pop**

## Linked List 
  * Node: (data, next)
  * Doubled linked list 
      * Node: (prev, data, next)


## Hash Table
* **Hash Function**
  ~~~python
  def hash_func(key):
     # 값을 저장 할 위치에 대한 정보가 
     # 고정된 길이로 나오게 하는 것에 
     # hash function의 의의가 있다.
     return key % 8
  ~~~

* **Key 생성**
    * 내장함수 hash(data)가 있다. 

<br>

---
<center><img src="https://www.fun-coding.org/00_Images/hash.png" width500 /></center>

* **장점**
    * 데이터 저장/읽기 속도가 빠르다. (검색 속도가 빠르다. 보통, O(1)
    * 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움
* **단점** 
  * 일반적으로 저장공간이 좀더 많이 필요하다.
  * **여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함**

* **주요 용도**
  * 검색이 많이 필요한 경우
  * 저장, 삭제, 읽기가 빈번한 경우
  * 캐쉬 구현시 (중복 확인이 쉽기 때문에)

* **Hash Collision** - 해시 함수 결과 같은 해시 주소를 가리키는 경우.
  * 해결방법 두가지 
     1. **Chaining (Open Hashing)**
        * 또 다른 데이터 저장 공간을 만든다.
        * 링크드 리스트로 추가적으로 저장.
     2. **Linear Probing (Close Hashing)**
        * 기존 저장공간 중에 빈공간을 찾아 저장
---
* ### SHA (Secure Hash Algorithm)
  * ‘String’.encode(). = b’String’. Bite로 바꾸는 것.
  * SHA-256은 블록체인에서도 쓰고, Hash화 된 값은 추론할 수가 없음.
  
    ~~~python
     def get_key(data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16)
    ~~~
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

---

## Tree
* ### Binary Tree & Binary Search Tree
  * **Binary Tree** - branch가 최대 2개인 tree.
  * **Binary Search Tree** - parent를 기준으로, 왼쪽엔 작은 수, 오른쪽엔 큰 수로 분류해서, 탐색을 하는 시간을 혁신적으로 줄여주는 자료구조.

* ### BST Node Deletion시, Tips
	* **Child Node가 하나일 경우**
 		>  1. 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다. - 이건 쉬움
 	* **Child Node가 두 개인 경우**
      > 1. 삭제할 Node의 **오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키토록** 한다. 
      > 2. 삭제할 Node의 **왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록** 한다.
	* <u>Child Node가 두 개인 경우,</u> a, b 두가지 방법 중, 아무거나 하나를 선택해서 구현하면 되는데, 삭제할 노드를 찾아가는 과정은 **`current_node`, `parent_node`** 로 찾아가고, 삭제할 노드를 발견했을 때, 삭제한 자리에 바꿔서 그 자리를 채워줄 노드는 **`change_node`, `change_node_parent`** 라는 변수를 추가로 생성해서 교통정리를 해주면 된다. (꼭 손으로 써볼 것!)


* ### 이진 탐색 트리의 시간 복잡도와 단점
	*  Depth (트리의 높이)를 h라고 표기한다면 O(h)
	*  n개의 노드를 가진다면, $h = log_2n$에 가까우므로, 시간 복잡도는 $O(logn)$
		* 빅오 표기법에서 $logn$에서의 log의 밑은 2다. 10이 아니다. 왜냐면 한 번 실행 할 때마다, 50%씩 탐색대상에서 제외되니까 당연.
	* Skewed List를 만난 최악의 상황에는 O(n)이 될 수도 있다.  

---
## Heap

* 이진탐색트리가 '탐색'을 가장 잘 하기 위해 최적화된 이진 트리라면, **Heap은 최대값, 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리 (Complete Binary Tree)**
* 여기서 '완전'이라는 말은 이진 트리가 항상 왼쪽부터 채워서, array나 list로 데이터 구조를 이해할 때에 '빈 공간이 없고, 순차적으로,' 완전히 채워져 있다는 의미이다.
* 최대, 최소값을 Heap에서 찾으려면(or 삭제하려면) $O(logn)$이 걸린다. 

	### 특징
  > **1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
  > 2. 완전 이진 트리다.
  > 3. 힙은 왼쪽, 오른쪽 자식 노드 값이 누가 더 큰지 상관없음.**
 
 
* ### 데이터 Insertion
	* 다음과 같은 순서로 데이터를 넣는다. 
      > 1. 가장 마지막 자리에 데이터를 넣는다. 
      > 2. 부모 노드와 비교해서 크기가 더 크면 자리를 바꾼다. 
      > 3. 자리를 바꾼 뒤에도, 2번의 과정을 반복.


* ### 데이터 Deletion
	* Heap에서 Deletion이란, **Root Node를 없애는, 최대값 혹은 최소값을 뽑는 다는 것**을 의미한다. <u>중간에 있는 특정 노드를 뽑는 경우는 없다</u>. 
	* 다만, 없어진 Root Node의 자리를 다음과 같은 순서로 채운다. 
      > 1. 제일 마지막에 들어온 노드를 Root Node로 가져온다. 
      > 2. 자식 노드들 보다 크기가 작다면, 자식 노드들 중 크기가 더 큰 노드와 자리를 바꾼다.
      > 3. 자리를 바꾼 뒤에도 2번을 반복.
      > 