# Cost Function and Backpropagation

## Cost Function
* Let's first define a few variables that we will need to use:

  $L$ = total number of layers in the network
  $s_l$ = number of units (not counting bias unit) in layer l
  $K$ = number of output units/classes

* Recall that in neural networks, we may have many output nodes. We denote $h_\Theta(x)_k$as being a hypothesis that results in the $k^{th}$ output. 
* Our cost function for neural networks is going to be a generalization of the one we used for logistic regression. Recall that the cost function for regularized logistic regression was:

	$J(\Theta) = -\frac{1}{m}\displaystyle\sum^m_{i=1}\sum^K_{i=1}[y^{(i)}_k \text{log}((h_\theta(x^{(i)}))_k+ (1-y^{(i)}_k)\text{log}(1-(h_\Theta(x^{(i)}))_k)] + \frac{\lambda}{2m}\displaystyle\sum^{L-1}_{l=1}\sum^{sl}_{i=1}\sum^{sl+1}_{j=1}(\Theta^{(l)}_{j,i})^2$
    
    
* We have added a few nested summations to account for our multiple output nodes. In the first part of the equation, before the square brackets, we have an additional nested summation that loops through the number of output nodes.

* In the regularization part, after the square brackets, we must account for multiple theta matrices. The number of columns in our current theta matrix is equal to the number of nodes in our current layer (including the bias unit). The number of rows in our current theta matrix is equal to the number of nodes in the next layer (excluding the bias unit). As before with logistic regression, we square every term.

* Note:

	* the double sum simply adds up the logistic regression costs calculated for each cell in the output layer

	* the triple sum simply adds up the squares of all the individual $\Theta$s in the entire network.
	
    * the i in the triple sum does **not** refer to training example i