# machine-learning-class

To run, load a jupyter notebook, point `dataset_roots` at your local copy of the datasets, run all cells


# Logistic Regression

Parameters:

    learning_rate = .01  # Natural learning rate constant
    penalty = 0.001  # penalty (lambda) constant
    epochs = 10  # Number of iterations
    penalty_rates_to_try = [0, 0.001, .01, .02, .003, .02, 0, .025, .04, .7, .8, .9]

Dataset 1 
Best lambda is 0.001 with an accuracy of 91.42857142857143
Correct predictions:	421/478
Accuracy:	88.0753%

Dataset 2 
Best lambda is 0.001 with an accuracy of 89.70588235294117
Correct predictions:	413/456
Accuracy:	90.5702%

Dataset 3 
Best lambda is 0.001 with an accuracy of 98.75776397515529
Correct predictions:	261/342
Accuracy:	76.3158%