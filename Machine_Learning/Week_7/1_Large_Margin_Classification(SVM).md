# Large Margin Classification

## Optimization Objective (Cost Function)

### Support vector machine

* The cost function of Logistic regression is:
	
<img src="img/1.png" width="100%">

* Similarly, the **`cost function of SVM`** is like below:

	<img width="100%" src="img/2.png">
    
	* $\text{cost}_1(\theta^Tx^{(i)})$ and $\text{cost}_0(\theta^Tx^{(i)})$ replace $-\text{log}h_\theta(x^{(i)})$ and $-\text{log}(1-h_\theta(x^{(i)}))$ each. 
	* Both cost function in case 0 or 1, look like following,
		<img src="img/3.png">
    * If $y =1,$ we want $\theta^Tx \geq 1$ (not just $\geq0$)
    * If $y =0,$ we want $\theta^Tx \leq -1$ (not just $\lt0$)
     
* The main difference between logistic regression and SVM is **the position of the balance part**, $\lambda$ and $C$. Both are basically trying to balance out the portions of cost and regularization term.

* Basically, the **`hypothesis`** of SVM:

	$h_\theta(x) = \begin{cases} 
      1 & \text{if }\Theta^TX\geq 0 \\ 
      0                 & \text{otherwise}
	\end{cases}$    
    
   
### Large Margin Intuition

