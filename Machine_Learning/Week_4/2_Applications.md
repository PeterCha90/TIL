# Applications


## Examples and Intuitions I

* A simple example of applying neural networks is by predicting $x_1$ AND $x_2$, which is the logical 'and' operator and is only true if both $x_1$ and $x_2$ are 1.


* The graph of our functions will look like:

	$\begin{bmatrix}x_0 \\ x_1 \\ x_2\end{bmatrix} \rightarrow\begin{bmatrix}g(z^{(2)})\end{bmatrix} \rightarrow h_\Theta(x)$
    

* Remember that $x_0$ is our bias variable and is always 1. 
* Let's set our first theta matrix as:

	$\Theta^{(1)}= [-30\text{ }\text{ } 20 \text{ }\text{ }20]$
    
    
* This will cause the output of our hypothesis to only be positive if both $x_1$ and $x_2$ are 1. In other words:

	$h_\Theta(x) = g(-30 + 20x_1 + 20x_2)$
    $x_1 = 0 \ \ and \ \ x_2 = 0 \ \ then \ \ g(-30) \approx 0$
    $x_1 = 0 \ \ and \ \ x_2 = 1 \ \ then \ \ g(-10) \approx 0$ 
    $x_1 = 1 \ \ and \ \ x_2 = 0 \ \ then \ \ g(-10) \approx 0$ 
    $x_1 = 1 \ \ and \ \ x_2 = 1 \ \ then \ \ g(10) \approx 1$
    
    
* So we have constructed one of the fundamental operations in computers by using a small neural network rather than using an actual AND gate. Neural networks can also be used to simulate all the other logical gates. The following is an example of the logical operator 'OR', meaning either $x_1$ is true or $x_2$ is true, or both:


	<img src="img/2.png">
    
* Where g(z) is the following:

	<img src="img/3.png">
