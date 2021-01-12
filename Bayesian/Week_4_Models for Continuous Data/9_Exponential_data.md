<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->



## Bayesian Statistics:

# 9. Exponential data

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>



## 9.1. Exponential data

*  지수 분포 데이터의 경우를 생각해보자. 예를 들어, 당신은 버스를 기다리고 있는데, 생각하기를 평균적으로 매 10분마다 온다고 생각한다. 하지만 사실은 정확히 얼마나 자주 오는지는 확신할 수 없다. $\lambda$는 waiting time rate다. 

	$$ Y \thicksim \text{Exp}(\lambda)$$
    $$E[X] = \frac{1}{\lambda},\text{  } Var(X) = \frac{1}{\lambda^2}$$
    
* 그렇다면, 당신은 '평균적으로' 라고 생각했기 때문에, Prior expectation으로 $\frac{1}{\lambda} = \frac{1}{10}$이 된다.

* 대충 예상은 했겠지만, Gamma 분포는 지수분포 likelihood의 Conjugate 분포다. 사실, 감마는 엄청나게 다양한 것들의 Conjugate다. 
* 자, 우리는 이제 Prior를 명시할 필요가 있는데, 이 경우에는 특정 Gamma가 어떻게 되느냐이다. 이미 언급했듯이 평균적으로 10분에 한 대씩 버스가 온다고 한다면 Prior Mean = $\frac{1}{\lambda} = \frac{1}{10}$이다.  

#### Prior Mean
* 이 말은 즉, Gamma 분포로 생각하면, $\frac{\alpha}{\beta}$이라는 말이 되니까, $\alpha = 1$, $\beta = 10$이 되는 각인데, 좀더 다양하게 생각해보면 비율만 같으면 되니까 $\Gamma(100, 1000)$이라고 생각해도 되겠다. $\to$ Effective Sample Size를 엄청 크게 가져가서, Prior(믿음)이 Posterior에 미치는 영향을 크게 가져가겠다.
---
#### Prior std.dev.
* Prior 표준편차는 지수분포 분산을 구하는 식에 의해서, $\frac{1}{100}$이 된다. 
* 그렇다면, **평균에서 $\pm$ 2*표준편차** 정도가 Prior의 러프한 구간이라고 볼 수 있다고 하면, $0.1 \pm 0.02$가 rate parameter($\lambda$)이 존재가능한 구간이라고 생각할 수 있겠다. 


### Update Posterior

* 만약 버스를 기다렸는데 이 버스가 12분만에 왔다고 할 때, 얼마나 자주 버스가 도착할 것인가에 대한 $\lambda$에 대한 당신의 Posterior Update해보도록 하자. 수식의 전개는 이전 과에서 해온 과정의 반복이다. 


	$$Y = 12$$
    $$f(\lambda|y) \propto f(y|\lambda)f(\lambda)$$
    $$\propto \lambda e^{-\lambda y}\lambda^{\alpha-1}e^{-\beta \lambda}$$
    $$\propto \lambda^{(\alpha +1) -1}e^{-(\beta + y)\lambda}$$
    $$\to \lambda|y \thicksim \Gamma(\alpha +1, \beta+y)$$
   그래서 이 공식에 위에 Prior Mean 에서 구한 $\alpha$, $\beta$와, $y=12$를 대입하면, 아래와 같다. 
   $$\lambda|y \thicksim \Gamma(101, 1012)$$
   그래서, **Posterior Mean**은 $\frac{101}{1012}=.0998 = \frac{1}{10.02}$가 된다. 
* 이는, 위에서 Effective Sample Size($\alpha$)를 100이라는 큰 숫자로 가져갔기 때문에, 한 번 12분만에 온 버스를 관찰한 likelihood 데이터가 Posterior에 미치는 영향이 아주 미미해서, $\lambda$가 10에서, 10.02정도로 아주 작게 변하게 됐다고 해석할 수 있다. 

---

### Generalization 
* 우리는 하나 이상의 관측데이터에 대해서 좀 더 일반화 할 수 있다. 

* $Y_1, ..., Y_n$의 데이터가 iid이고, 
평균값을 $\frac{1}{\lambda}$를 가지는 지수함수를 따른다. 
$\lambda$의 Prior로 $\text{Gamma}(\alpha, \beta)$
 likelihood는 $f(y|\lambda) = \lambda^ne^{-\lambda\sum y_i}$

	그러면, 비례식에 따라, Likelihood와 Prior식을 곱하면, 
Posterior는 $\lambda|y \thicksim Gamma(\alpha + n, \beta + \sum y_i)$가 된다. 

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>