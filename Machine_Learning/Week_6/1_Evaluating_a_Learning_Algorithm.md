# Evaluating a Learning Algorithm

## Evaluating a Hypothesis

* Once we have done some trouble shooting for errors in our predictions by: 

	* Getting more training examples
	* Trying smaller sets of features
	* Trying additional features
  * Trying polynomial features
  * Increasing or decreasing $\lambda$
  * We can move on to evaluate our new hypothesis. 

* A hypothesis may have a low error for the training examples but still be inaccurate (because of overfitting). Thus, to evaluate a hypothesis, given a dataset of training examples, we can split up the data into two sets: a training set and a test set. Typically, the training set consists of 70 % of your data and the test set is the remaining 30 %. 

* The new procedure using these two sets is then:

	1. Learn $\Theta$ and minimize $J_{train}(\Theta)$ using the training set

	2. Compute the test set error $J_{test}(\Theta)$


### The test set error

1. For linear regression: $J_{test}(\Theta) = \dfrac{1}{2m_{test}} \sum_{i=1}^{m_{test}}(h_\Theta(x^{(i)}_{test}) - y^{(i)}_{test})^2$ 

2. For classification ~ Misclassification error (aka 0/1 misclassification error):

	$err(h_\Theta(x),y) = \begin{matrix} 1 & \text{if } h_\Theta(x) \geq 0.5\ and\ y = 0\ or\ h_\Theta(x) < 0.5\ and\ y = 1\\ 0 & \text otherwise \end{matrix}$
    

* This gives us a binary 0 or 1 error result based on a misclassification. The average test error for the test set is:

	$\text{Test Error} = \dfrac{1}{m_{test}} \sum^{m_{test}}_{i=1} err(h_\Theta(x^{(i)}_{test}), y^{(i)}_{test})$
    
    
* This gives us the proportion of the test data that was misclassified.

<br>

## Model Selection and Train/Validation/Test Sets

* Just because a learning algorithm fits a training set well, that does not mean it is a good hypothesis. It could over fit and as a result your predictions on the test set would be poor. 
* The error of your hypothesis as measured on the data set with which you trained the parameters will be lower than the error on any other data set. 

* Given many models with different polynomial degrees, we can use a systematic approach to identify the 'best' function. In order to choose the model of your hypothesis, you can test each degree of polynomial and look at the error result.

* One way to break down our dataset into the three sets is:
  * Training set: 60%
  * Cross validation set: 20%
  * Test set: 20%

* We can now calculate three separate error values for the three different sets using the following method:

	* Optimize the parameters in $\Theta$ using the training set for each polynomial degree.
	* Find the polynomial degree d with the least error using the cross validation set.
	* Estimate the generalization error using the test set with $J_{test}(\Theta^{(d)})$, (d = theta from polynomial with lower error); 

* This way, the degree of the polynomial d has not been trained using the test set.