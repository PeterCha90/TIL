# Rogistic Regression Model

## Cost function

* We cannot use the same cost function that we use for linear regression because the Logistic Function will cause the output to be wavy, causing many local optima. In other words, it will not be a convex function.

* Instead, our cost function for logistic regression looks like:
	<hr>
    
	$J(\theta)=\frac{1}{m}\displaystyle\sum^m_{i=1}\text{Cost}(h_\theta(x^{(i)},y^{(i)}))$
    $\text{Cost}(h_\theta(x), y) = -\text{log}(h_\theta(x))$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\text{if }y =1$ 
    $\text{Cost}(h_\theta(x), y) = -\text{log}(1-h_\theta(x))$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\text{if }y =0$ 
    
    <hr>
	
* When y = 1, we get the following plot for $J(\theta)$ vs $h_\theta(x)$:

	<img src="img/2.png">
    
* Similarly, when y = 0, we get the following plot for $J(\theta)$ vs $h_\theta(x)$:

	<img src="img/3.png">
    
    $\text{Cost}(h_\theta(x), y) = 0$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\text{ if }h_\theta(x) = y$
    $\text{Cost}(h_\theta(x), y) \to \infty$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\text{ if }y = 0 \text{ and }h_\theta(x) \to 1$
    $\text{Cost}(h_\theta(x), y) \to \infty$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\text{ if }y = 1 \text{ and }h_\theta(x) \to 0$
    

* If our correct answer 'y' is 0, then the cost function will be 0 if our hypothesis function also outputs 0. If our hypothesis approaches 1, then the cost function will approach infinity.
* If our correct answer 'y' is 1, then the cost function will be 0 if our hypothesis function outputs 1. If our hypothesis approaches 0, then the cost function will approach infinity.
* **Note that writing the cost function in this way guarantees that $J(\theta)$ is convex for logistic regression**.

<br>

## Simplified Cost Function and Gradient Descent 

* We can compress our cost function's two conditional cases into one case:
	<hr>
    
	$\text{Cost}(h_\theta(x), y) = -y \text{log}(h_\theta(x)) - (1-y)\text{log}(1-h_\theta(x))$
    <hr>
    
* Notice that when y is equal to 1, then the second term $(1-y)\text{log}(1-h_\theta(x))$ will be zero and will not affect the result. If y is equal to 0, then the first term $-y \text{log}(h_\theta(x))$ will be zero and will not affect the result.

* We can fully write out our entire cost function as follows:
	<hr>
    
    $J(\theta) = -\frac{1}{m}\displaystyle\sum^m_{i=1}[y^{(i)}\text{log}(h_\theta(x^{(i)})) + (1-y^{(i)})\text{log}(1-h_\theta(x^{(i)}))]$
    <hr>
    
* A vectorized implementation is:
	<hr>
    
	$h = g(X\theta)$
    
    $J(\theta) = \frac{1}{m}\cdot (-y^T\text{log}(h) - (1-y)^T\text{log}(1-h))$
    
    <hr>

<br>

### Gradient Descent

* Remember that the general form of gradient descent is:

	<hr>
    
    $\text{Repeat } \{$
    
    $\theta_j := \theta_j - \alpha\frac{\alpha}{m}\displaystyle\sum^m_{i=1}(h_\theta(x^{(i)}) - y^{(i)})x_j^{(i)}$
    
    $\}$
    
    <hr>
    
* Notice that this algorithm is identical to the one we used in linear regression. We still have to simultaneously update all values in theta.

* A vectorized implementation is:

	$\theta := \theta - \frac{\alpha}{m}X^T(g(X\theta) - \vec{y})$
    
<br>    
    
## Advanced Optimization

* "Conjugate gradient", "BFGS", and "L-BFGS" are more sophisticated, faster ways to optimize θ that can be used instead of gradient descent. We suggest that you should not write these more sophisticated algorithms yourself (unless you are an expert in numerical computing) but use the libraries instead, as they're already tested and highly optimized. Octave provides them.

* We first need to provide a function that evaluates the following two functions for a given input value $\theta$:

	$J(\theta)$
    
    $\dfrac{\partial}{\partial \theta_j}J(\theta)$
    
* We can write a single function that returns both of these:
	~~~matlab
    function [jVal, gradient] = costFunction(theta)
      jVal = [...code to compute J(theta)...];
      gradient = [...code to compute derivative of J(theta)...];
	end
    ~~~
    
* Then we can use **octave's "fminunc()"** optimization algorithm along with the **"optimset()"** function that creates an object containing the options we want to send to "fminunc()". 
(Note: the value for MaxIter should be an integer, not a character string - errata in the video at 7:30)

	~~~matlab
    options = optimset('GradObj', 'on', 'MaxIter', 100);
    initialTheta = zeros(2,1);
       [optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta, options);    
    ~~~
    
* We give to the function "fminunc()" our cost function, our initial vector of theta values, and the "options" object that we created beforehand.


<br>

## Multiclass Classification: One-vs-all

* Now we will approach the classification of data when we have more than two categories. Instead of y = {0,1} we will expand our definition so that y = {0,1...n}.

* Since y = {0,1...n}, we divide our problem into n+1 (+1 because the index starts at 0) binary classification problems; in each one, we predict the probability that 'y' is a member of one of our classes.

	<hr>
    
    $y \in \{0, 1, ...,n\}$
    
    $h_\theta^{(0)}(x) = P(y=0|x;\theta)$
    $h_\theta^{(1)}(x) = P(y=1|x;\theta)$
    ...
    $h_\theta^{(n)}(x) = P(y=n|x;\theta)$
   	
    $\text{prediction}  = \text{max}(h_\theta^{(i)}(x))$
    
    <hr>
    
 * We are basically choosing one class and then lumping all the others into a single second class. We do this repeatedly, applying binary logistic regression to each case, and then use the hypothesis that returned the highest value as our prediction.

* The following image shows how one could classify 3 classes: 

	<img src="img/4.png">
    
* **To summarize:**
	 
	Train a logistic regression classifier $h_\theta(x)$ for each class￼ to predict the probability that ￼ ￼$y = i$￼￼. 

	To make a prediction on a new $x$, pick the class ￼that maximizes  $h_\theta(x)$