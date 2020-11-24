# Solving the Problem of Overfitting 

## The Problem of Overfitting

* Consider the problem of predicting y from $x \in R$. The leftmost figure below shows the result of fitting a $y = \theta_0 + \theta_1x$ to a dataset. We see that the data doesn’t really lie on straight line, and so the fit is not very good. 

	<img src="img/5.png">
    
    
* Instead, if we had added an extra feature $x^2$, and fit $y = \theta_0 + \theta_1x+ \theta_2x^2$, then we obtain a slightly better fit to the data (See middle figure). Naively, it might seem that the more features we add, the better. However, there is also a danger in adding too many features: The rightmost figure is the result of fitting a 5^{th}
  order polynomial y =
 . We see that even though the fitted curve passes through the data perfectly, we would not expect this to be a very good predictor of, say, housing prices (y) for different living areas (x). Without formally defining what these terms mean, we’ll say the figure on the left shows an instance of underfitting—in which the data clearly shows structure not captured by the model—and the figure on the right is an example of overfitting.