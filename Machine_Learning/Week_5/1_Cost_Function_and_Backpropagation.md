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
	
    * the i in the triple sum does **not** refer to training example


## Backpropagation Algorithm


* "Backpropagation" is neural-network terminology for minimizing our cost function, just like what we were doing with gradient descent in logistic and linear regression. Our goal is to compute:

	$\text{min}_\Theta J(\Theta)$
    
* That is, we want to minimize our cost function J using an optimal set of parameters in theta. In this section we'll look at the equations we use to compute the partial derivative of J(Î˜):

	$\frac{\partial}{\partial\Theta_{i,j}^{(l)}}J(\Theta)$
    
* To do so, we use the following algorithm:

	<img src="img/1.png">
    
    
#### Back propagation Algorithm

* Given training set $\lbrace (x^{(1)}, y^{(1)}) \cdots (x^{(m)}, y^{(m)})\rbrace$

	* Set $\Delta^{(l)}_{i,j}$:= 0 for all (l,i,j), (hence you end up having a matrix full of zeros)

* For training example t =1 to m:

	1. Set $a^{(1)}:= x^{(t)}$
	2. Perform forward propagation to compute $a^{(l)}$ for l=2,3, ... ,L

	<br>

	<img src="img/2.png">

	<br>
    <br>
    
	3. Using $y^{(t)}$, compute $\delta^{(L)} = a^{(L)} - y^{(t)}$
	<br>
		* Where L is our total number of layers and $a^{(L)}$ is the vector of outputs of the activation units for the last layer. So our "error values" for the last layer are simply the differences of our actual results in the last layer and the correct outputs in y. To get the delta values of the layers before the last layer, we can use an equation that steps us back from right to left:

	<br>

	4. Compute $\delta^{(L-1)}, \delta^{(L-2)},\cdots,\delta^{(2)}$ using $\delta^{(l)} = ((\Theta^{(l)})^T \delta^{(l+1)})\ .*\ a^{(l)}\ .*\ (1 - a^{(l)})$

		* The delta values of layer l are calculated by multiplying the delta values in the next layer with the theta matrix of layer l. We then element-wise multiply that with a function called **g', or g-prime, which is the derivative of the activation function g evaluated with the input values given by $z^{(l)}$**.

		* The g-prime derivative terms can also be written out as:
			
			$g'(z^{(l)}) = a^{(l)}\cdot* (1-a^{(l)})$
            
	5. $\Delta^{(l)}_{i, j}:= \Delta^{(l)}_{i, j} + a_j^{(l)}\delta_i^{(l+1)}$ or with vectorization, $\Delta^{(l)} := \Delta^{(l)} + \delta^{(l+1)}(a^{(l)})^T$ Hence we update our new $\Delta$ matrix.

		* $D^{(l)}_{i, j} := \frac{1}{m}(\Delta_{i,j}^{(l)} + \lambda\Theta_{i, j}^{(l)}),$ $\text{if j}$ $\neq$ $\text{0}$
		* $D^{(l)}_{i, j} := \frac{1}{m}\Delta_{i,j}^{(l)}$ $\text{if j}$ $=$ $\text{0}$

	<br>
    
	* The capital-delta matrix D is used as an "accumulator" to add up our values as we go along and eventually compute our partial derivative. Thus we get $\frac \partial {\partial \Theta_{ij}^{(l)}} J(\Theta) = D_{ij}^{(l)}$




## Backpropagation Intuition

* Recall that the cost function for a neural network is:
	
    $J(\Theta) = - \frac{1}{m} \displaystyle\sum_{t=1}^m\sum_{k=1}^K \left[ y^{(t)}_k \ \log (h_\Theta (x^{(t)}))_k + (1 - y^{(t)}_k)\ \log (1 - h_\Theta(x^{(t)})_k)\right] + \frac{\lambda}{2m}\sum_{l=1}^{L-1} \sum_{i=1}^{s_l} \sum_{j=1}^{s_l+1} ( \Theta_{j,i}^{(l)})^2$ 


* If we consider simple non-multiclass classification (k = 1) and disregard regularization, the cost is computed with:

	$\text{cost}(t) = y^{(t)} \text{log}(h_\Theta(x^{(t)})) + (1- y^{(t)}) \text{log}(1-h_\Theta(x^{(t)}))$


* **Intuitively, $\delta_j^{(l)}$ is the "error" for $a^{(l)}_j$  (unit j in layer l).** More formally, **the delta values are actually the derivative of the cost function**:

	$\delta^{(l)}_j = \frac{\partial}{\partial z^{(l)}_j \text{cost}(t)}$
    
* Recall that our derivative is the slope of a line tangent to the cost function, so the steeper the slope the more incorrect we are. Let us consider the following neural network below and see how we could calculate some $\delta_j^{(l)}$:

	<img src="img/3.png">


* In the image above, to calculate $\delta_2^{(2)}$, we multiply the weights $\Theta_{12}^{(2)}$ and $\Theta_{22}^{(2)}$ by their respective $\delta$ values found to the right of each edge. So we get $\delta_2^{(2)}=\Theta_{12}^{(2)}*\delta_1^{(3)}+\Theta_{22}^{(2)}*\delta_2^{(3)}$.

* To calculate every single possible $\delta_j^{(l)}$, we could start from the right of our diagram. We can think of our edges as our $\Theta_{ij}$. Going from right to left, to calculate the value of $\delta_j^{(l)}$, you can just take the over all sum of each weight times the $\delta$ it is coming from. Hence, another example would be $\delta_2^{(3)}=\Theta_{12}^{(3)}*\delta_1^{(4)}$.
