# **What is Machine Learning?** :no_mouth:

  ### Machine Learning definition

  - Arthur Samuel - 1959

      > Field of study that gives computers the ability to learn without being explicitly programmed.

      This is a somewhat informal definition and an older one.

  - Here's a slightly more recent definition by Tom Mitchell who's a friend of Carnegie Melon.
  - Tom Mitchell - 1998

      > Well-posed Learning Problem: A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.

  ### Machine learning algorithms:

  - **Supervised** learning - we're going to teach the computer how to do something.

      In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

      Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories.

      **Example 1:**

      Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

      We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

      **Example 2**:

      **(a) Regression** - Given a picture of a person, we have to predict their age on the basis of the given picture

      **(b) Classification** - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.

  - **Unsupervised** learning - we're going to let it learn by itself.

      Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.

      We can derive this structure by clustering the data based on relationships among the variables in the data.

      With unsupervised learning there is no feedback based on the prediction results.

      **Example:**

      Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

      Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at aÂ [cocktail party](https://en.wikipedia.org/wiki/Cocktail_party_effect)).

  - Others: **Reinforcement** learning, **recommender** **systems**.

