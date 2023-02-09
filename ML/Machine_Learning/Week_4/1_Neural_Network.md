# Non-Linear Hypotheses. Neural Network


## Model Representation I

* Let's examine how we will represent a hypothesis function using neural networks. At a very simple level, neurons are basically computational units that take inputs (**dendrites**) as electrical inputs (called "spikes") that are channeled to outputs (**axons**). 
*  In our model, our dendrites are like the input features $x_1\cdots x_n$, and the output is the result of our hypothesis function. In this model our $x_0$ input node is sometimes called the "bias unit." It is always equal to 1. 
*  In neural networks, we use the same logistic function as in classification, $\frac{1}{1 + e^{-\theta^Tx}}$, yet we sometimes call it a sigmoid (logistic) **activation** function. In this situation, our "theta" parameters are sometimes called "weights".

* Visually, a simplistic representation looks like:

	$[x_0x_1x_2] \to [ \ ] \to h_\theta(x)$
    
* Our input nodes (layer 1), also known as the **"input layer"**, go into another node (layer 2), which finally outputs the hypothesis function, known as the **"output layer"**.

* We can have intermediate layers of nodes between the input and output layers called the "**hidden layers.**" In this example, we label these intermediate or "hidden" layer nodes $a^2_0 \cdots a^2_n$and call them "activation units."

	$a_i^{(j)} = \text{"activation" of unit } i \text{ in layer }j$ 
    $\Theta^{(j)} = \text{matrix of weights controlling function mapping from layer } j \text{to layer }j+1$
    
*  If we had one hidden layer, it would look like:

	$[x_0x_1x_2x_3] \to [a_1^{(2)}a_2^{(2)}a_3^{(2)}]\to h_\theta(x)$
    
* The values for each of the "activation" nodes is obtained as follows:

	$a_1^{(2)} = g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3)$
    $a_2^{(2)} = g(\Theta_{20}^{(1)}x_0 + \Theta_{21}^{(1)}x_1 + \Theta_{22}^{(1)}x_2 + \Theta_{23}^{(1)}x_3)$
    $a_3^{(2)} = g(\Theta_{30}^{(1)}x_0 + \Theta_{31}^{(1)}x_1 + \Theta_{32}^{(1)}x_2 + \Theta_{33}^{(1)}x_3)$
    
    $h_\Theta(x) = a_1^{(3)} = g(\Theta_{10}^{(2)}a_0^{(2)} + \Theta_{11}^{(2)}a_1^{(2)} + \Theta_{12}^{(2)}a_2^{(2)} + \Theta_{13}^{(2)}a_3^{(2)})$
    
    
* This is saying that we compute our activation nodes by using a 3Ã—4 matrix of parameters. We apply each row of the parameters to our inputs to obtain the value for one activation node. 
* Our hypothesis output is the logistic function applied to the sum of the values of our activation nodes, which have been multiplied by yet another parameter matrix $\Theta^{(2)}$containing the weights for our second layer of nodes.

* Each layer gets its own matrix of weights, $\Theta^{(j)}$.The dimensions of these matrices of weights is determined as follows:

	$\text{If network has }s_j \text{ units in layer }j \text{ and }s_{j+1} \text{ units in layer } j+1,$ 
    $\text{then }\Theta^{(j)} \text{ will be of dimension }s_{j+1} \times (s_j+1).$
    
* The +1 comes from the addition in $\Theta^{(j)}$ of the "bias nodes," $x_0$ and $\Theta_0^{(j)}$. In other words the output nodes will not include the bias nodes while the inputs will. The following image summarizes our model representation: 

	<img src="img/1.png">
    
* Example: If layer 1 has 2 input nodes and layer 2 has 4 activation nodes. Dimension of $\Theta^{(1)}$is going to be 4Ã—3 where $s_j = 2$ and $s_{j+1} = 4$, so $s_{j+1} \times (s_j + 1)=4 \times 3$.


## Model Representation II

* To re-iterate, the following is an example of a neural network:
	<hr>
    
	$a_1^{(2)} = g(\Theta_{10}^{(1)}x_0 + \Theta_{11}^{(1)}x_1 + \Theta_{12}^{(1)}x_2 + \Theta_{13}^{(1)}x_3)$
    $a_2^{(2)} = g(\Theta_{20}^{(1)}x_0 + \Theta_{21}^{(1)}x_1 + \Theta_{22}^{(1)}x_2 + \Theta_{23}^{(1)}x_3)$
    $a_3^{(2)} = g(\Theta_{30}^{(1)}x_0 + \Theta_{31}^{(1)}x_1 + \Theta_{32}^{(1)}x_2 + \Theta_{33}^{(1)}x_3)$
    
    $h_\Theta(x) = a_1^{(3)} = g(\Theta_{10}^{(2)}a_0^{(2)} + \Theta_{11}^{(2)}a_1^{(2)} + \Theta_{12}^{(2)}a_2^{(2)} + \Theta_{13}^{(2)}a_3^{(2)})$
    <hr>

* In this section we'll do a vectorized implementation of the above functions. We're going to define a new variable $z_k^{(j)}$that encompasses the parameters inside our g function. In our previous example if we replaced by the variable z for all the parameters we would get:

	$a_1^{(2)} = g(z_1^{(2)})$
    $a_2^{(2)} = g(z_2^{(2)})$
    $a_3^{(2)} = g(z_3^{(2)})$
    
* In other words, for layer j=2 and node k, the variable z will be:
	$z_i^{(2)}= \Theta_{k,0}^{(1)}x_0 + \Theta_{k,1}^{(1)}x_1 + \cdots + \Theta_{k,n}^{(1)}x_n$
    
* The vector representation of x and $z^j$ is:
	<hr>
	
    $x = \begin{bmatrix}x_0 \\ x_1 \\ \cdots \\ x_n\end{bmatrix}\text{, } z^{(j)} = \begin{bmatrix}z_1^{(j)} \\ z_2^{(j)} \\ \cdots \\ z_n^{(j)}\end{bmatrix}$ 
    
    <hr>
* Setting $x = a^{(1)}$, we can rewrite the equation as:
	
	$z^{(j)} = \Theta^{(j-1)}a^{(j-1)}$
    
* We are multiplying our matrix $\Theta^{(j-1)}$ with dimensions $s_j\times (n+1)$ (where $s_j$ is the number of our activation nodes) by our vector $a^{(j-1)}$ with height (n+1). 

* This gives us our vector $z^{(j)}$with height $s_j$. Now we can get a vector of our activation nodes for layer j as follows, where our function g can be applied element-wise to our vector $z^{(j)}$.

	$a^{(j)} = g(z^{(j)})$
    
* We can then add a bias unit (equal to 1) to layer j **after we have computed $a^{(j)}$**. This will be element $a_0^{(j)}$ and will be equal to 1. To compute our final hypothesis, let's first compute another z vector:

	$z^{(j+1)} = \Theta^{(j)}a^{(j)}$
    
* We get this final z vector by multiplying the next theta matrix after $\Theta^{(j-1)}$ with the values of all the activation nodes we just got. This last theta matrix $\Theta^{(j)}$ will have only **one row** which is multiplied by one column $a^{(j)}$ so that our result is a single number. We then get our final result with:

	$h_\Theta (x) = a^{(j+1)} = g(z^{(j+1)})$
    
    
* Notice that in this **last step**, between layer j and layer j+1, we are doing **exactly the same thing** as we did in logistic regression. Adding all these intermediate layers in neural networks allows us to more elegantly produce interesting and more complex non-linear hypotheses.
