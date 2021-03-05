#!/usr/bin/env python3

import sys
import pandas

"""
.\program <L> <K> <training-set> <validation-set> <test-set> <to-print>
L: integer (used in the post-pruning algorithm)
K: integer (used in the post-pruning algorithm)
to-print:{yes,no}
"""

# input_string = ['D:/_PROJECTS/machine-learning-class/homework-01/src/main.py', '2', '5', 'training_set.csv', 'validation_set.csv', 'test_set.csv', 'yes']
# print(input_string)
# inputs = input_string.split(" ")

#print(sys.argv)

L = sys.argv[1]
K = sys.argv[2]
training_set_path = sys.argv[3]
validation_set_path = sys.argv[4]
test_set_path = sys.argv[5]
to_print_input = sys.argv[6]

training_set = pandas.read_csv(training_set_path)
validation_set = pandas.read_csv(validation_set_path)
test_set = pandas.read_csv(test_set_path)

if to_print_input == "yes":
    to_print = True
elif to_print_input == "no":
    to_print = False
else:
    print("to-print must be 'yes' or 'no', printing anyway")
    to_print = True


def node_formation(df):
    # recursive function which drills down until a pure node is returned
    # no promises, but I think this recursive structure should work

    count_01 = {}
    # dictionary for attributes with counts as tuples (0, 1)
    # This creates the elements, counts, feel free to pop out
    for attribute in df.loc[:, df.columns != ('Class' or '' or 'None')]:
        # loops over all attributes not identified as Class, the outcome
        zeros = (df[attribute] == 0).sum() # Turns df in True/False
        ones = (df[attribute] == 1).sum()
        count_01[attribute] = (zeros, ones)
        # TODO: Can use this formula to get varience of Class

    min_variance = calculate_variance(count_01)
    # returns tuple (attribute, variance)

    # TODO: Update this if/else once we know what to expect from gain and entropy
    if min_variance[1] > 0:
        branch_0 = node_formation(df[df[min_variance[0]] == 0].drop([min_variance[0]], axis=1))
        # filters df by attribute value and drops the named attribute
        branch_1 = node_formation(df[df[min_variance[0]] == 1].drop([min_variance[0]], axis=1))
        return {min_variance[0]: {0: branch_0, 1: branch_1}}
        
    else: # value was 0, set as pure_node with outcome
        return {min_variance[0]: {Value: 'Class', 'Class': Outcome}}
        # TODO: need a way to capture the value and class outcome
        # pure_node is an attribute "X_"
        # leaf is 0 or 1


def calculate_variance(target_values):
    #values = list(target_values)
    #elements,counts = #here we need a function that assigns to "element" the lists of our elements X_i
                      #and to "counts" the pair [number of 0s in X_i, number of 1s in X_i]
    #variance_impurity = 0
    #sum_counts = _sum(counts)
    #for i in elements:
     #   variance_impurity += (-counts[i]/sum_counts*(counts[i]/sum_counts))

    # I attempted to rework the formula with the data that comes from node_formation
    # Please double check my math - Alexa
    # Spoiler, it isn't correct

    min_impurity = ('NotMe!', 1)
    # all calculations should be less than 1
    
    # TODO: This loop doen't do what we need it too, but will work for updating gain?
    for attribute in target_values:
        counts = target_values[attribute]
        # (0s, 1s)
        zeros = counts[0]
        ones = counts[1]
        sum_counts = zeros + ones
        variance_impurity = (zeros/sum_counts*ones/sum_counts)
        if min_impurity[1] > variance_impurity:
            min_impurity = (attribute, variance_impurity)

    if min_impurity[0] == 'NotMe!':
        print('Ya done messed up.')

    return min_impurity


node_dict = node_formation(training_set)
print(node_dict)
# TODO: Test that this output aligns with data input

#print("L: {}".format(L))
#print("K: {}".format(K))
#print("Training Set: \n{}".format(training_set))
#print("Validation Set: \n{}".format(validation_set))
#print("Test Set: \n{}".format(test_set))
#print("To Print: {}".format(str(to_print)))
