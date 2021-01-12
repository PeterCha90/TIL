<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->



## Bayesian Statistics:

# 8. Poisson data

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>
<br>


## 8.1. Poisson data

* 포아송의 경우를 위해 초코칩쿠키 예시를 생각해보자. 정말 큰 부피의 도우에 초코칩을 겁나 때려넣고 정말 잘 저어서 섞은 뒤에, 쿠키를 하나하나 만든다고 하자.
* 그렇다면 쿠키에 들어있는 초코칩의 개수는 대략적으로 포아송 분포를 따르게 된다. 만약 초코칩의 부피가 0이라고 한다면 정확히 포아송분포를 따르게 된다. 근데 뭐, 실제로는 초코칩이 그렇게 크지는 않으니까 **대략적으로 쿠키마다 가지고 있는 초코칩의 개수($Y_i$)가 포아송 분포를 따른다**고 하자. 

$$Y_i \thicksim \text{Pois}(\lambda), \text{ } P(X =x|\lambda) = \frac{\lambda^x\text{exp}(-\lambda)}{x!} \text{ for }x = 0,1,2,..$$

$$f(y|\lambda) = \frac{\lambda^{\sum y_i}e^{-n\lambda}}{\prod_{i=1}^n y_i!}\text{ for}\lambda >0$$

* 자, 그렇다면 어떤 종류의 Prior를 우리는 $\lambda$로 사용해야할까? 우리가 Conjugate prior를 사용할 수 있다면 편리할 것 같은데.....?! 가만 ~~ 히 살펴보고 이 포아송분포랑 비슷하게 생긴 친구를 생각해 보니, Gamma 분포가 있다!!

#### Gamma Distribution
* $$Y \thicksim \Gamma(\alpha, \beta), \text{ }f(y|\alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)}y^{\alpha-1}e^{-\beta y}I_{\{y \ge0\}}(y)$$
    
---
* **Gamma Prior**는 다음과 같이 $Y$대신에 $\lambda$를 사용해서, 다움과 같이 전개할 수 있다.
  $$\lambda \thicksim \Gamma(\alpha, \beta), \text{ } f(\lambda) = \frac{\beta^\alpha}{\Gamma(\alpha)}\lambda^{\alpha-1}e^{-\beta\lambda}$$

* **Posterior**는, 비례식으로 계산하면 $\text{likelihood}\times \text{Prior}$이기 때문에,  
	$$f(\lambda|y) \propto f(y|\lambda)f(\lambda)$$
    이 되고, 이 식은 또 비례식으로 계산하게되면, 각 likelihood와 Prior식의 상수부분$\Big(\frac{1}{\prod_{i=1}^n  y_i!}, \frac{\beta^{\alpha}}{\Gamma(\alpha)}\Big)$는 상관이 없기 때문에 무시하고 아래와 같이 단순하게 계산할 수 있다. 
    
    $$\propto \lambda^{\sum y_i}e^{-n\lambda}\cdot \lambda^{\alpha-1}e^{-\beta\lambda}$$
    $$\propto \lambda^{(\alpha + \sum y_i)-1}e^{-(\beta + n)\lambda}$$
    $$\Gamma(\alpha + \sum y_i, \beta + n)$$
    
 * **Mean of Gamma**가, $\frac{\alpha}{\beta}$인 것을 상기해보면, Posterior Mean 또한, 아래와 같이 표현할 수 있고, 이것도, Likelihood와, Prior의 Weighted Sum으로 표현할 수 있다. 
 	$$\text{Posterior Mean}$$
    $$=\text{Prior Weight}\cdot\text{Prior Mean} + \text{Data Weight}\cdot\text{Data Mean} $$
 	$$\frac{\alpha + \sum y_i}{\beta + n} = \frac{\beta}{\beta + n}\cdot\frac{\alpha}{\beta} + \frac{n}{\beta+n}\cdot \frac{\sum y_i}{n}$$
    
    따라서, 두 Weights는 더해서 1이 되고, 자연스럽게 Effective Sample Size도, $\beta$가 된다. 
    
---
## How to choose our hyper parameterrs
* 그럼 우리는 이제 Parameter, Hyperparameter인, $\alpha$와 $\beta$를 어떻게 고를 것인가 질문할 수 있다. 초콜릿칩 쿠키와 같이 **현실에 근거한, 구체적인(concrete) 문제**의 경우, 우리의 Prior가 무엇이 되어야 하는지, Prior에 대한 정보를 어떻게 명시할지 대충 감을 잡을 수 있다. 
*  가지고 있는 정보를 사용하기 위한 **어떤 방식의 전략**을 우리가 사용하는가에 따라 정보를 수집하고, Posterior를 얻기 위해 Update하기만 하면 된다. **두 가지 전략**을 알려주도록 하겠다. 


#### 1. Prior Mean $\frac{\alpha}{\beta}$

* 우리는 정보를 우리의 개인적인 지식에 근거해서, Prior에 넣을 것이다. 
    
* 먼저 Prior Mean이 무엇인가 생각을 해보면서 시작해보자. 위의 경우, Prior mean은, $\frac{\alpha}{\beta}$였다. **평균적으로 쿠키마다 가지는 초코칩의 숫자를 무엇이라 생각**할까? 그것이 **Prior Mean**이다. 여기서는 $\alpha$와 $\beta$두가지 변수가 있으니, 추가 적으로 두 변수를 계산해야하는 두번째 식이 필요하다. 

* 두 번째 식을 구하기 위해서는, 
	* 첫 번째로 **Prior std. dev. $\frac{\sqrt{\alpha}}{\beta}$**
	 Prior 표준편차(std.dev.)에 대해서 생각할 때 나오는 식 $\frac{\sqrt{\alpha}}{\beta}$를 쓰고, 평균을 12라고 우리가 믿는(Prior)다면, 그에 따른 표준편차 또한 3, 4, 혹은 6이 될 수 있을 것이라 또 가정하고, 두 식을 전개하면, 그 Prior(믿음)에 따른 $\alpha$, $\beta$를 알아서 계산을 잘 해주시면 되겠다. 
	* 두 번째로는 **Effective sample size $\beta$**
	Effective sample size에 대해서 생각해보면 된다. 위에서 이 Prior에 해당하는 Effective sample size는 $\beta$라고 말했다. 그렇기 때문에, 데이터의 Sample Size인 $n$과 비교해서, 적당한 Prior 정보 갯수는 어느정도여야 할지 생각하고 대입하면, 나머지 $\alpha$에 대해서 풀어낼 수 있다. 


---

#### 2. Vague Prior (모호한 Prior)

* **아리까리한 우리의 Prior에 대한 무지를 표현하는 접근법**이 또 있다. 
* 베이지안 통계에서 Vague Prior란, 많은 차원에 걸쳐서 비교적 Flat하다는 뜻(= 분산이 엄청나다라는 뜻)이다. 이 경우에는 정말 작은 숫자를 뜻하는 Epsilon에 대해 생각해볼 수 있다. 

*	Small $\epsilon > 0$, 이라고 하면, 우리는 $\Gamma(\epsilon, \epsilon)$ Prior를 가질 수 있다. 이렇게 전제를 하는 이유는, 이렇게 전제를 하게 되면,
    평균값은, $\frac{\epsilon}{\epsilon}=1$이 되지만, 분산은 $\frac{\epsilon}{\epsilon^2}=\frac{1}{\epsilon}$라는 말이고, $\epsilon$은 엄청나게 작은 값이기 때문에, $\frac{1}{\epsilon}$의 계산 값은 엄청나게 커지게 된다. 그래서 결과적으로 우리는 모든 공간에 걸쳐 엄청나게 퍼져있는(diffused) Prior를 우리는 가지게 된다. 
    

* 자, 그러면 이런 Prior를 가질 때의 Posterior Mean은 어떻게 되겠는가? 계산해보면,

	$\frac{\epsilon + \sum y_i}{\epsilon + n}$이 될텐데, 사실상, $\epsilon$은 너무 작은 숫자다 보니, $\approx \frac{\sum y_i}{n}$과 다름이 없는 데이터 평균값이므로, 이것은 그냥 우리의 믿음인 Prior의 영향력은 매우 미미하고, Posterior는 거의 전적으로 관측되는 실측 데이터에 크게 좌지우지 된다는 뜻이 된다. 
    
    
<br><br><br><br><br><br><br><br><br><br><br><br>