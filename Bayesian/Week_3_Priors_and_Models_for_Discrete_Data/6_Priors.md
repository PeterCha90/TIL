<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->



## Bayesian Statistics:

# 6. Priors

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>
<br>

 
## 6.1. Priors and prior predictive distributions

* 사전확률인 Prior를 어떻게 정할 것인가. Prior는 우리의 주관적인 관점, 믿음, 그리고 불확실성을 대표한다. 
* 이론적으로는 우리는 매개변수에 해당하는 누적 분포 함수를 정한다. 보통 모든 가능한 실수에 대해서 실수 $c$보다 작거나 같다고 설정한다. 

	$$P(\theta \le c) \text{ for all c}\in R$$

* 이 경우 너무나 많은 대상들이 $\theta$일 수 있기 때문에, 실제로는 우리의 믿음을 잘 표현할 수 있는 충분히 유연한 **통계 분포들을 사용해서 표현**한다. 그 다음에, 이전의 실험들과 같은 정보들이 있다면, 외부정보들을 세워나갈 수 있다. 
* 보통 너무 많은 데이터가 있을 경우, Prior로 무엇을 선정하든, 비슷한 Posterior를 낼 수 있기 때문에 그다지 중요하지 않을 수 있다. 하지만 주의해야할 경우는 있다. 
* 예를들어 $P(\theta =\frac{1}{2}) = 1$이라고 생각해서, 나머지 $\theta$에 대한 확률은 0이라고 생각을 해버린다면,  Posterior를 구할 때, $f(\theta|y) \propto f(y|\theta)f(\theta) = f(\theta)$가 돼버리고 만다. ($\theta$가 $\frac{1}{2}$인 경우를 제외하고는 다 0이기 때문에, $f(\theta)$가 1/2이 될때의 $f(\theta|y)$가 무조건 1)
* 우리가 하나의 Point를 1이라고 생각해버리는 이런 경우에는 우리가 가지고 있는 데이터가 변수로 들어갈 수가 없다.


---
### Dirac Delta Function
* 그래서 **베이지안의 문맥에서는 Prior가 0이면 Posterior도 0이고, Prior가 1이면 Posterior도 1**''이다. 그래서 좋은 베이지안은 0이나 1과 같은 확률을 이미 일어난 사건이나, 일어나지 않을 것이라 알려진 어떠한 사건에도 배정하지 않는다. 
* 위의 예시같은 경우를 **Dirac delta function(디락 델타 함수)라고 표기**한다. $\delta(\frac{1}{2})$. 

### Calibration
* Prior를 고르는 유용한 개념은 **`Calibration`** 이다. 예측 범위의 측정을 뜻한다. 
* 만약 우리가 새로운 데이터의 95%가 이 구간 안에서 일어난다고 말할 수 있는 구간을 설정하고 싶다고 한다면, 실제로 새로운 데이터의 95%가 그 구간 안에서 일어난 적이 있다면 좋을 것이다. 
* 그러면 우리는 **실제로 일어난 실제상황(prior)을 어떻게 측정**할 것인가? 우리가 만들 구간이 95%의 새로운 관찰된 데이터들이 이 범위 안에 들어오게 되는 구간이라고 한다면, 이 구간은 데이터 그 자체($y$)에 대한 범위다. 그동안 우리가 찾아왔던 $\theta$ 범위를 말하는 것이 아니다. 특히, 우리는 $P(A|B) = \frac{P(A \cap B)}{P(B)}$이라는, 조건부확률을 다시 떠올려 보면, 

	$$f(y|\theta) = \frac{f(y, \theta)}{f(\theta)}$$
	$$f(y, \theta)=f(y|\theta)\cdot f(\theta)$$
    이기 때문에, $\text{likelihood} \times \text{prior}$는, 데이터와 파라미터에 대한 Joint Distribution이라고도 생각할 수 있다. 그렇기 때문에, 아래와 같이 Joint function(교집합 함수)으로도 표현할 수 있다.
$$f(y) = \int f(y|\theta)f(\theta)d\theta = \int f(y, \theta)d\theta$$
* 이것, $f(y)=\int f(y, \theta)d\theta$을 **Prior Predictive Intervals**라고 하는데, **관측되는 데이터의 수준에서 Prior의 연속성을 드러내기 때문에 유용**하다. 

---

## 6.2. Prior predictive: binomial example

* 우리는 동전을 열번 뒤집어서 앞면이 나온 경우를 센다고 생각해보자. 잠깐, 우리는 실제로 동전을 던지기 전에 이 것에 대해 생각을 해보자, 즉, **Predictive Distribution**에 관심이 있다고 하자. 그러면 우리는 **얼마나 많은 앞면을 우리가 보게 될 것이라 예측하는가?**
* 물론 이것은 앞면을 보일 확률이 얼마인지 동전에게 달린 문제다. 그래서 우리는 그저 Prior를 고르기만 하면된다. 
* $X$를 앞면의 갯수라고 하면, 

$$X = \sum_{i=1}^{10} Y_i$$

* 동전이 앞면이 나올 확률을 모르기 때문에 Uniform Distribution이라고 생각하면, 

	$$f(\theta) = I_{\{0 \le \theta \le 1\}} $$
	라고 하고, 우리가 구하고 싶은 $f(X)$를 계산을 해본다고 하면,
    
    $$f(X) = \int f(x|\theta)f(\theta)d\theta = \int_0^1\frac{10!}{x!(10-x)!}\theta^x(1-\theta)^{10-x}(1)d(\theta)$$
   가 된다. 

* 그럼 이 식을 다 계산해야할까? 이 복잡한 식을 계산하기 쉽게 하려면,  $n! = \Gamma(n+1)$이라는 점과 ($\Gamma$함수는 정수가 아닌 수에 대해 사용할 수 있는 factorial의 일반화 함수다.), Beta 분포를 사용해서 할 수 있다.
$$z \thicksim Beta(\alpha, \beta)$$

$$f(z) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)}z^{\alpha-1}(1-z)^{\beta-1}$$

---
$$ \int_0^1\frac{10!}{x!(10-x)!}\theta^x(1-\theta)^{10-x}(1)d(\theta)$$

$$=\int_0^1\frac{\Gamma(11)}{\Gamma(x+1)\Gamma(11-x)}\theta^{(x+1)-1}(1-\theta)^{(11-x)-1}d\theta$$

$$=\frac{\Gamma(11)}{\Gamma(12)}\int_0^1\frac{\Gamma(12)}{\Gamma(x+1)\Gamma(11-x)}\theta^{(x+1)-1}(1-\theta)^{(11-x)-1}d\theta$$

* 이렇게 되면, $\frac{\Gamma(11)}{\Gamma(12)}$를 제외한$\int$이하 오른쪽 전체식은 완벽히 Beta분포의 일반식의 형태이고, 확률에서$\int_0^1$은 총합 1이 될 수 밖에 없으므로, 이 복잡한 식을 굳이 계산할 필요가 없다. 그래서 그냥 $\frac{\Gamma(11)}{\Gamma(12)}$만 남게 된다는 것이다. 

	$$=\frac{\Gamma(11)}{\Gamma(12)}(1) = \frac{10!}{11!} = \frac{1}{11} \text{ for }X \in {\{0, 1,2,..., 10\}}$$
    이 된다. 
    

<br><br><br><br><br><br><br><br><br><br><br>

---

## 6.3. Posterior Predictive Distribution 

* 데이터를 관찰한 다음은? 우리의 **Posterior Predictive Distribution**은 어떻게 되는가? 동전을 던졌을 때 앞면이 나올 확률이 어떻게 되는지 모른다고 할 때, 던져보는 동전에 대해 생각해보자. 
* 한 번 던져서 한 번의 앞면이 나온 데이터를 관찰했다고 가정한다면, **첫 번째 시도에서 앞면이 나왔다는 것을 전제로 우리의 두번째 시도에 대한 예측분포는 어떻게 될 것인가** 물어 볼 수 있다. 

* 앞서 배운 **Prior Predictive Distribution에서 Prior자리에 Posterior를 넣어서**, 첫 번째 시도에서 앞면이 나왔다는 것을 전제로 우리의 두 번째 시도에 대한, **Posterior Predictive distribution**를 다음과 같이 생각해 볼 수 있다.
	$$f(y_2|y_1) =  \int f(y_2|\theta_1 y_1)f(\theta|y_1)d\theta$$
    대부분의 경우 $Y_2 \perp Y_1$(독립)라고 생각할 수 있기 때문에, 그냥
    $$=\int f(y_2|\theta)f(\theta|y_1)d\theta$$
    라고 생각할 수도 있다. Prior Distribution자리에 Posterior Distribution을 썼다는 것만 빼면, 아주 Prior Predictive와 비슷하다.
    
* 자, 다시 본론으로 돌아가서, 우리는 $\theta$에 대해 Uniform Distribution이라고 생각하고, 첫 번째 시도에서 앞면을 관찰했다고 생각하면, 두 번째 시도에 대해 우리는 무엇을 예측할 수 있는가?
	* 이제는 더이상 첫 번째 시도 때와처럼 Uniform Distribution이 아니다. 왜냐하면 우리는 (첫 번째 시도에서 앞면이 나왔다는)데이터를 좀 가지고 있거든!! 이것 자체로 우리에게 동전에 대해 정보를 주고 있다. 
	* 첫 번째 시도에서 앞면이 나왔기 때문에 이제는 두 번째 시도에서 앞면이 나올 $\theta$가 적어도 1/2보다는 크겠다고 생각할 수 있다. 

---
* 방금까지 설명한 내용을 식으로 쓰면 아래와 같다.
	$$f(y_2|Y_1=1) = \int f(y_2|\theta)f(\theta|y_1)d\theta $$
    $$= \int_0^1\theta^{y_2}(1-\theta)^{1-y_2}2\theta d\theta = \int_0^1 2\theta^{y_2+1}(1-\theta)^{1-y_2}d\theta$$
    까지 정리할 수 있다. 
    
* 그래서 두 번째 시도에도 앞면이 나올 확률가 그렇지 않을 확률을 계산하면 아래와 같이 구할 수 있다. 

	$$P(Y_2=1|Y_1=1) = \int_0^12\theta^2d\theta = \frac{2}{3}$$
    $$P(Y_2=0|Y_1=1) =\int_0^1 2\theta d\theta = \frac{1}{3}$$
    
* 여기까지 살펴 봄을로써, 우리는 **Posterior란, Prior(믿음)에 있는 정보와 우리가 관찰한 데이터에 있는 정보의 조합**이라는 것을 알 수 있다.
	* 이번 예시의 경우 우리의 Prior는 두가지, 앞면과 뒷면이라는 data points를 가지고 있고, 그렇기에 두 가지 경우가 발생해왔다는 것을 전제(믿음)로 그 정보를 이용하고.
	* 또한, 우리가 앞에서 한 번의 앞면을 관찰했다는 정보를 사용해서.
	*  두 번째 시도에도 앞면이 나올 것에 대한 **Posterior Predictive Distribution**을 구해보면, 한 번더 앞면을 관찰할 경우에는 2/3, 그렇지 않을 경우 1/3이라는 분포를 가지는 것을 알 수 있다. 

<br><br><br>

