<!--page_number:true-->
<!-- $width: 1150-->
<!-- $height: 1500-->



## Bayesian Statistics:

# 12. Linear regression

### Herbert Lee

### Univerrsity of California Santa Cruz

<hr>



## Background for Lesson 12

### 1. Brief Review of Regression 

* 회귀식을 기대값으로 표현하면 다음과 같다.
	$$E[y]=\beta_0 + \beta_1x, \text{ } Y \thicksim N(\beta_0 + \beta_1x, \sigma^2)$$
    데이터 $(x_1, y_1),...,(x_n, y_n)$의 coefficients 값들을 $\hat \beta_0, \hat \beta_1$으로 표기할 수 있고, 이 값들은 SSE인 $\sum_{i=1}^n(y_i - \hat y_i)^2$의 값을 최소화하도록 하는 값들로, 예측값은 $\hat y = \hat \beta + \hat \beta_1 x$가 된다.
    
* 이 모델은 multiple covariates로 확장 될 수 있으며, 각 $\beta_k$는 k번째 covariate에 해당된다. 

	$$E[y_i] = \beta_0 + \beta_1x_{i1} + ... + \beta_kx_{ik}$$
    선택적으로는, 우리는 Multivariate case를 벡터-매트릭스 표현법으로 나타낼 수도 있다. 
    

### 2. Conjugate Modeling

* 
  






---

## 12.1. Linear regression in R

*


---

## Course conclusion