# Rogistic Regression Model

## Cost function

* We cannot use the same cost function that we use for linear regression because the Logistic Function will cause the output to be wavy, causing many local optima. In other words, it will not be a convex function.

* Instead, our cost function for logistic regression looks like:

	$J(θ)=1m∑i=1mCost(hθ(x(i)),y(i))Cost(hθ(x),y)=−log(hθ(x))$
	
* When y = 1, we get the following plot for $J(\theta)$ vs $h_\theta(x)$:

	<img src="img/2.png">