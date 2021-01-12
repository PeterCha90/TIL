<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->



## Bayesian Statistics:

# 4. Frequentist inference

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>


 
## Background for Lesson 4
 
## 1. Products and Exponents


$$ \prod_{i=1}^n x_i = x_1 \cdot x_2 \cdot \cdots \cdot x_n$$
 
 * $n! = \Pi_{i=1}^n i$ for $n \ge 1.$
 * $f(x) = 3x +1$일 때, 이산형 변수만 취할 수 있어서, $x \in \{-1,2,4\}$이면, 

$$\prod_x f(x) = (3 \cdot(-1) +1) \cdot (3\cdot (2) +1) \cdot(3\cdot(4)+1) = -182$$

 

* $a^x \cdot a^y = a^{x+y}$
* $(a^x)^y = a^{x \cdot y}$


<br>

## 2. Natural Logarithm
* 지수함수의 역산으로 볼 수 있는 로그. 그래서 $y = a^x$이면, $\text{log}_a(y)$
* **자연로는 밑을 $e$로 가진다.** 밑 없이 표기하기도 한다. $\text{log}_e(y) = \text{log}(y)$.
* 모든 $x$에 대해 $e^x > 0$이기 때문에, $\text{log}(y)$는 오직 $y >0$에 대해서만 정의된다. 

---


* 항상, $\text{exp}(\text{log}(y)) = \text{log}(\text{exp}(y)) = y$.


<center>

1. $\text{log}(x \cdot y) = \text{log}(x) + \text{log}(y)$


2. $\text{log}(\frac{x}{y}) = \text{log}(x) - \text{log}(y)$

3. $\text{log}(x^b) = b\text{log}(x)$

4. $\text{log}(1) = 0$

</center>
<br>

### 작은 꿀팁
* **자연로그는 1:1 함수로 단조증가**하기 때문에, <u>$f(x)$를 최대화하는 $x$는 $log(f(x))$를 최대화 하는 값</u>과 같다. 

* 이 성질은 미분을 취할 때 아주 유용한데, f(x)가 곱셈의 형태이면, $\text{log}(f(x))$를 취하는 순간, 훨씬 더 미분을 취하기 좋은 덧셈의 형태로 변하기 때문이다. 

**Example:** $\text{log}\Big(\frac{5^2}{10}\Big) = 2\text{log}(5) - \text{log}(10)\approx 0.916$

<br>

## 3. Argmax

* 함수 $f(x)$를 최대화하고 싶다고 하면, 우리가 관심을 가지게 되는 것은 아래 두가지.

1. $f(x)$가 최대를 찍었을 때 값은 우리는 $max_xf(x)$라고 표기한다. 
2. $f(x)$를 최대값을 가지게 하는 $x$값을 우리는 $\hat x = \text{arg max}_xf(x)$

  	**그러니까 $\text{max}_xf(x) = f(\hat x)$임.**
    
**Example:** 
* $f(x) = \text{exp}(-x^2)$고, 그러면,  $\text{log}(f(x)) = -x^2$다. $x=0$에서 최대값을 가진다. 그렇기 때문에, $\text{arg max}_xf(x)=\hat x = 0$이고, $\text{max}_xf(x) = f(\hat x)  = f(0) = 1$이다.

---


## 4.1. Confidnece intervals

* 먼저 베이지안 접근법과 대조적인, 빈도주의자들의 추론을 위한 접근법에 대해 간략히 살펴보자. 
* frequentist들의 패러다임에서는 데이터를 바라볼 때, 그 **데이터는, 잠재적으로 가정된 아주 큰 모집단에서 추출된 램덤으로 추출된 표본이라고 생각**한다. 
* 그렇다면 우리는, 예를 들어 이 큰 모집단을 근거로 긴 시간 동안 발생하게 되는 확률에 대한 전제를 깔 수 있다. 
* 예를 들어 동전을 100번 던진다고 했을때, 앞면이 44번 나오고 뒷면이 56번 나왔다고 하자. 이 경우 우리는 각 동전 던지기는 확률 $p$인 베르누이 분포를 따른다고 할 수 있다.


* 그렇다면 CLT - Central Limit Theorem에 의해서($n$ > 30이면 충분히 크다고 표현한다.) 정규분포를 따른다고 했을 때, 평균이 100p이고 분산이 100p(1-p)인, 그리고 $n$이 100인 이항분포로 이해할 수 있다. 

$$\sum_{i = 1}^{100}X_i \approx N(100p, 100p(1-p))$$

* 정규분포에서 95%이상의 구간에 의해서, 실제 모집단의 $p$는 

	$$100\hat p-1.96\sqrt{100\hat  p(1-\hat p)} < p < 100\hat  p + 1.96\sqrt{100\hat  p(1-\hat  p)}$$ 
	라고 할 수 있다. :)
    따라서, 결과는 $44\pm 1.96\sqrt{44(0.56)} =44 \pm 9.7$로, 
    CI (Confidence Interval) - (34.3, 53.7) 사이에 위치할 것이라고 가정한다

* 자, 여기까지는 빈도주의자들의 가정과 생각이 말이 된다. 우리가 연속적으로 무한대, 혹은 충분히 많이 실험을 반복한다면, 실제로 평균적으로 만들어질 95% 범위 IC 안에 실제 $p$값이 존재함을 관찰할 수 있다. 

---

### Limitation Frequentist

* 하지만, 만약 우리가 **'그 범주' 안에, 실제 true $p$가 존재할 가능성**을 알고싶다면? 
* 그 범주 안에 존재하거나, 존재하지 않거나. frequentist들은 0 or 1의 대답을 할 수 밖에 없다. 이것은 충분히 만족스러운 설명이 아니다. 
* 하지만 베이지안으로 접근하게 된다면, 실제로 우리는 interval을 계산하고 실제 $p$가 그 interval 안에 존재할 확률이 **알려지지 않은 매개변수의 랜덤 해석(?)** 에 의해서 95%라고 말할 수 있게된다. 

<br>

## 4.2. Likelihood function and Maximum likelihood

* 또 다른 예시로, 심장마비로 한  달 동안 400명의 환자들이 입원한 병원이 있다고 하자. 그리고 한 달뒤 그 중 72명은 죽었고, 328명은 살았다. 그렇다면 사망률에 대한 우리 예측은 무엇일까?
* Frequentist의 개념에서는 우리는 먼저 reference population, 기준집단을 세워야한만다. 우리는 기준집단이 이 지역에 있다고 생각할 수 있는가? 한가지 가능성은 이 지역 안에 있는 심장질환 환자들로 생각해보는 것이다. 또 다르게는, 한 병원에 오랜 기간에 걸쳐 심장질환으로 입원한 환자들에 대해 생각해볼 수도 있다. 
* 둘 다 합리적인 시도일 수 있다. 하지만, 이 경우에는 우리의 실제 데이터는 그런 데이터들로 부터의 랜덤 선정된 표본이라고 볼 수가 없다. 
* 만약 이 지역 안에 있는 사람들이 표본인척하고 진행하기에는, 이 지역 사람들 중에, 심장 질환이 올 확률과, 그렇게 병원에 입원할 확률까지 우리는 생각해야한다.
* 그래서 이 경우는 조금은 이상한 가상의 상황이다. 그래서 frequentist들의 관점으로 전체 문제를 바라보기에는 좀 철학적인 이슈 - 실제 환자들이 퇴원을더 빨리 한다거나, 이 지역에 다른 병원들에 있는 환자들의 분포가 다 다르다거나하는- 가 있다. 


---

* 자, 추정을 계속해보도록 하자. 우리는 각 환자들은 알 수 없는 parameter $\theta$를 가진 **베르누이 분포를 따른다**고 할 수 있다. 

	$$Y_i \thicksim B(\theta)$$
	이 경우, $P(Y_i = 1) = \theta$가 의미하는 것은 환자가 사망했을 때(Success)를 의미한다. 이 때, 전체 데이터에 대한 PDF를 우리는 벡터형태로 써볼 수 있다. 
    $Y_i$는, $\theta$라는 전제 아래 $y_i$를 취할 수 있고, 이것은 아래와 같이 표현된다. 
    $$P(Y = y|\theta) = P(Y_i = y_i, Y_2=y_2, \cdots , Y_n = y_n|\theta)$$
    또 , 각각의 이벤트는 독립이기 때문에,
    $$P(Y_1 =y_1|\theta)\cdots P(Y_n =y_n|\theta)$$
    이 식은 또, $\prod$와 베르누이 분포의 확률을 사용하면,
    $$\prod_{n=1}^n P(Y_i = y_i|\theta) = \prod_{y=1}^n \theta^{y_i}(1-\theta)^{1-y_i}$$
    라고 표현 할 수 있다. 이 식은 우리가 수집한, **"실제 데이터를 관찰할 수 있는, $\theta$ 조건 확률 = $P(y_i|\theta)$"** 이다. 
* 우리는 이 식을 바꿔표현해서($=P(\theta |y$)로 생각) $\theta$에 관한 함수로 이해할 수 있는데, 이것이 **Likelihood**의 개념이다. 우리가 **관찰한 데이터를 토대로 $\theta$를 생각해보자는 역발상**이다. 우리가 알고 싶은것은 $\theta$니까. 

## Likelihood, 우도

$$L(\theta|y) = \prod_{i=1}^n \theta^{y_i}(1-\theta)^{1-y_i}$$

* 이 식은 더이상 베르누이 분포가 아니라, $\theta$에 관한 함수다. 


---

## MLE - Maximum Likelihood Estimate

* 이 $\theta$를 추정하는 한가지 방법은 **가장 큰 값을 Likelihood로 주는 $\theta$를 고르는 것**이다. 이것이 **우리가 관찰한 특정 데이터가 실제로 일어날 가능성을 가장 많이 가지게 해준다는 개념**이다. 
$$\hat\theta = \text{argmax L}(\theta|y)$$

* 실용적으로는, 자연로그 likelihood를 최대화하는 것이 더 쉽다. 

$$l(\theta) = \text{log L}(\theta|y)$$
* 로그는 단조증가함수이기 때문에, 우리는 로그함수를 최대화하면, 본래 함수를 최대하는 것이 된다. 로그를 취하면 곱셈이 덧셈이 되기 때문에 훨씬 더 계산이 쉬워진다. 

$$l(\theta) =  log\Big[\prod \theta^{y_i}(1-\theta)^{1-y_i}\Big]$$
$$=\sum log\Big[\ \theta^{y_i}(1-\theta)^{1-y_i}\Big]$$
$$=\sum \Big[y_i \text{log}\theta + (1-y_i)\text{log}(1-\theta)\Big]$$
$$=(\sum y_i)\text{log}\theta + \Big(\sum(1-y_i)\Big)\text{log}(1-\theta)$$
* 어떻게 하면 이 식을 가장 크게 만드는 $\theta$를 구할 수 있을까? 미적분을 떠올려보면, 우리는 미분해서 0이 되게하면 (기울기가 0) 그것이 함수로 최대값을 가지게 해준다는 것을 알 수 있다.

---

## 4.3. Computing the MLE

$$\text{MLE} =(\sum y_i)\text{log}\theta + \Big(\sum(1-y_i)\Big)\text{log}(1-\theta)$$

* 위의 식의 미분을 취하고 0으로 두면, 아래와 같이 계산이 가능하다.

$$l'(\theta) = \frac{1}{\theta}\sum y_i - \frac{1}{1-\theta}\sum (1-y_i) = 0$$
$$\to \frac{\sum y_i}{\hat \theta} = \frac{\sum(1-y_i)}{1-\hat \theta}$$
$$\to \hat \theta = \frac{1}{n}\sum y_i = \hat p = \frac{72}{400} = 0.18$$

* 이처럼 MLE는 다양한 좋은 성질들을 가지고 있는데, **편향되지 않았고, 일관적이며, 변동성이 없다- 한결같다(?).**  CI, 95% 신뢰구간은 아래와 같다. 
$$\text{Approx CI }= \hat \theta \pm 1.96\sqrt{\frac{\theta(1-\theta)}{n}}$$

## Summary
* MLE는 다음과 같은 순서를 따른다. 

	> 1. 각 문제의 **PDF을 $n$번에 대해 계산($\int$)** 을 한다. 그 식이 MLE
	> 2. 그 식에 곱셉이 있는 경우, **$\text{log}$를 취해서 계산을 간편하게** 한다. 
	> 		* 주의할 점) Uniform Distribution - 균일분포의 경우 로그를 취하지 않는 것이 더 계산이 쉬운 예외의 경우다.  
	> 3. **미분을 취해서, $l'(\theta)=0$으로 세팅**하면, $\hat \theta$에 대한 MLE 계산 결과를 구할 수 있다!
	> 
* In fact, if the data are independent and identically distributed from a **Bernoulli($p$), Poisson($\lambda$), or Normal($\mu$, $\sigma^2$ ), then $\bar x$ is the MLE for $p$, $\lambda$, and $\mu$** respectively.