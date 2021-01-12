<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->


## Bayesian Statistics:

# 2. Bayes' Theorem

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>

<br>

## 2.1. Conditional probability


* 조건부 확률은 우리가 서로 관계가 있는 두 사건을 고려하고자 했을 때의 상황을 말한다. 그래서, <u>이벤트 B가 발생했다는 것을 전재로 이벤트 A가 발생할 확률</u> (= $P(A|B)$)을 물어볼 수도 있다. 이것은 아래식과 같이, B가 일어 났을 확률로 A와 B가 동시에 발생할 확률을 나누는 것으로 이해할 수 있다.
 
 $$P(A|B) = \frac{P(A\cap B)}{P(B)}$$
 
 
 ## Independence
 * 어떠한 사건이 다른 사건과 상관없이 일어나는 경우 **`독립`** 이라고 한다. 수식으로 표현하면 아래와 같다. 
 
 $$P(A|B) = P(A)$$
 * 두 사건이 독립이라면, 아래와 
 
 $$\text{if A and B are indepent, then}$$
 $$P(A \cap B) = P(A)P(B)$$
 
 
---

## 2.2. Bayes' theorem
* Bayes' 이론은 우리가 베이지안 통계라는 틀 안에서 하는 모든 것들의 이론적 뒷받침이 되어준다. **Bayes' Theorem은 조건의 방향을 역으로 바꿀 때 사용**된다. 
* <u>**$P(B|A)$와 $P(B|A^c)$.그리고 $P(A)$라는 제한적인 정보만 알고 있을 때, $P(A|B)$를 알고 싶다**</u>면 아래와 같은 식을 사용 할 수 있다. 

$$P(A|B) = \frac{P(B|A)P(A)}{P(B|A)P(A) + P(B|A^c)P(A^c)} = \frac{A \cap B}{P(B)}$$

<br>

## Supplementary material for Lesson 2

<br>

* 가능한 결과물이 $A_1, A_2, A_3$ 세 가지가 되고, 무조건 셋 중 하나는 일어난다고 한다면, Bayes Theorem은 아래와 같이 확장될 수 있다. ($A_1^c$ 인 경우의 나열)

$$P(A_1|B) = \frac{P(B|A_1)P(A_1)}{P(B|A_1)P(A_1) + P(B|A_2)P(A_2)+ P(B|A_3)P(A_3)}$$

<br>

* 만약 이벤트가 $A_1,...,A_m$으로 **A partition of the space**를 구성한다면, Bayes Theorem을 다음과 같이 다시 쓸 수 있다. 

$$P(A_1|B) = \frac{P(B|A_1)P(A_1)}{\sum_{i=1}^m P(B|A_i)P(A_i)}$$


* **연속확률분포에서는 Sum이 Integral로 바뀐다**. 