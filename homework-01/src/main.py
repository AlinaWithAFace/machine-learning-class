#!/usr/bin/env python3

import sys
import pandas
import json
from random import randint
import copy

"""
.\program <L> <K> <training-set> <validation-set> <test-set> <to-print>
L: integer (used in the post-pruning algorithm)
K: integer (used in the post-pruning algorithm)
to-print:{yes,no}
"""

# input_string = ['D:/_PROJECTS/machine-learning-class/homework-01/src/main.py', '2', '5', 'training_set.csv', 'validation_set.csv', 'test_set.csv', 'yes']
# print(input_string)
# inputs = input_string.split(" ")

# print(sys.argv)

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
    """
    recursive function which drills down until a pure node is returned
    no promises, but I think this recursive structure should work
    drill down by keys until you find 'Class'
    :param df:
    :return:
    """

    # Check current variance
    variance = variance_impurity(df)

    if variance == 0:
        # Pure node
        if (df['Class'] == 0).sum() == 0:
            class_outcome = 0
        else:
            class_outcome = 1

        return {'Class': class_outcome}

    else:
        node_attribute, zero, one = gain(df)  # returns attribute to split on, and if zero or ones were present
        if zero:
            branch_0 = node_formation(df[df[node_attribute] == 0].drop([node_attribute], axis=1))
            # filters df by attribute value and drops the named attribute
        if one:
            branch_1 = node_formation(df[df[node_attribute] == 1].drop([node_attribute], axis=1))

        if zero and one:  # attribute contained both
            return {node_attribute: {0: branch_0, 1: branch_1}}
        if zero:
            return {node_attribute: {0: branch_0}}
        if one:
            return {node_attribute: {1: branch_1}}


def variance_impurity(df):
    """
    Input is dataframe, which may be subset of larger set
    VI(S) = (K0/K*K1/K)
    K0, class = 0
    K1, class = 1
    K = sum(K0 + K)
    Returns variance impurity
    """

    K0 = (df['Class'] == 0).sum()  # Turns df in True/False
    K1 = (df['Class'] == 1).sum()
    K = K0 + K1

    if K == 0:
        # print("K is 0, returning 0")
        return 0

    K2 = K0 / K
    # print("K2:")
    # print(K2)
    K3 = K1 / K
    # print("K3:")
    # print(K3)

    variance = (K2 * K3)
    # print("variance:")
    # print(variance)

    return variance


def count_01s(df):
    """
    Input is dataframe, which may be subset of larger set
    Creates a dictionary for each remaining attributes/elements in the format
    {attribute: (zeros, ones)}
    returns dictionary
    """

    attribute_counts = {}
    # dictionary for attributes with counts as tuples (0, 1)
    # This creates the elements, counts, feel free to pop out
    for attribute in df.loc[:, df.columns != ('Class' or '' or 'None')]:
        # loops over all attributes not identified as Class, the outcome
        zeros = (df[attribute] == 0).sum()  # Turns df in True/False
        ones = (df[attribute] == 1).sum()
        attribute_counts[attribute] = (zeros, ones)

    return attribute_counts


def gain(df):
    """
    Input df
    variance_impurity and count_01 in finding the maximum gain
    Returns the attribute/element which the highest gain
    """

    target_values = count_01s(df)
    VIS = variance_impurity(df)
    initialize = True

    for attribute in target_values:
        zeros = target_values[attribute][0]
        ones = target_values[attribute][1]
        Pr0 = zeros / (zeros + ones)
        Pr1 = 1 - Pr0  # Using axioms, probability will sum to 1
        VIS0 = variance_impurity(df[df[attribute] == 0])
        VIS1 = variance_impurity(df[df[attribute] == 1])
        gainSX = VIS - Pr0 * VIS0 - Pr1 * VIS1

        if initialize:
            max_gain = (attribute, gainSX)
            initialize = False
        if gainSX > max_gain[1]:
            max_gain = (attribute, gainSX)

    attribute = max_gain[0]
    zero, one = False, False
    if target_values[attribute][0] > 0:
        zero = True
    if target_values[attribute][1] > 0:
        one = True

    return attribute, zero, one


def print_decision_tree(layer_count, dictionary):
    """
    Recursively go through the dictionaries and print out the keys/values, adding space to every layer for a tiered visual
    :param layer_count: the depth of the layer, initially use -1, gets added to every recursion
    :param dictionary: the dictionary to print, might not actually be a dictionary if we're at the end of the layers
    :return: a printed decision tree
    """
    if type(dictionary) != dict:
        # print("dictionary not a dictionary, return")
        return
    layer_count = layer_count + 1

    for key, value in dictionary.items():

        # for i in range(0, layer_count): print("| ", end="")

        # print("key {} ".format(key))

        if type(value) == dict:
            for v in value:
                print("")
                for i in range(0, layer_count): print("| ", end="")
                print("{} = {} : ".format(key, v), end="")

                print_decision_tree(layer_count, value[v])
        else:
            # for i in range(0, layer_count): print("| ", end="")
            # print("value not a dictionary, end of tree?")
            print("{} ".format(value), end="")


node_dict = node_formation(training_set)

if to_print:
    print_decision_tree(-1, node_dict)
    

tree_gain = #build tree with gain
tree_variance = #build tree with variance_impurity

def tree_accuracy(instance, tree, default_outcome=None):
    attribute = list(tree.keys())[0]
    if instance[attribute] in tree[attribute].keys():
        outcome = tree[attribute][instance[attribute]]
        if isinstance(outcome, dict): 
            return tree_accuracy(instance, outcome)
        else:
            return outcome
    else:
        return default_outcome
    
def order_the_nodes (tree, number):
    #this function orders the nodes in the new_tree D′ from 1 to N;
    if isinstance(tree, dict):
        attribute = list(tree.keys())[0]
        if tree[attribute]['number'] == number:
            if(tree[attribute][0]!=0 and tree[attribute][0]!=1):
                new_tree = tree[attribute][0]
                if isinstance(new_tree, dict):
                    new_attribute = list(new_tree.keys())[0]
                    tree[attribute][0] = new_tree[new_attribute]['best_class']
            elif(tree[attribute][1]!=0 and tree[attribute][1]!=1):
                new_tree = tree[attribute][1]
                if isinstance(new_tree, dict):
                    new_attribute = list(new_tree.keys())[0]      
                    new[attribute][1] = new_tree[new_attribute]['best_class']
        else:
            left = tree[attribute][0]
            right = tree[attribute][1]
            order_the_nodes(left, number)
            order_the_nodes(right,number)
    return tree

def number_of_internal_nodes(tree):
    if isinstance(tree, dict):
        attribute = list(tree.keys())[0]
        left = tree[attribute][0]
        right = tree[attribute][1]
        return (1 + number_of_internal_nodes(left) +  
               number_of_internal_nodes(right)); 
    else:
        return 0;

 
def post_pruning(L, K, tree):
    best_tree = tree
    for i in range(1, L+1) :
        new_tree = copy.deepcopy(best_tree)
        M = randint(1, K);
        for j in range(1, M+1):
            n = number_of_internal_nodes(new_tree)
            if n> 0:
                P = randint(1,n)
            else:
                P = 0
            order_the_nodes(new_tree, P)
        test_set['accuracy_before_pruning'] = test_set.apply(tree_accuracy, axis=1, args=(best_tree,'1') ) 
        accuracy_before_pruning = str( sum(test_set['Class']==test_set['accuracy_before_pruning'] ) / (1.0*len(test_set.index)) )
        test_set['accuracy_after_pruning'] = test_set.apply(tree_accuracy, axis=1, args=(new_tree,'1') ) 
        accuracy_after_pruning = str( sum(test_set['Class']==test_set['accuracy_after_pruning'] ) / (1.0*len(test_set.index)) )
        if accuracy_after_pruning >= accuracy_before_pruning:
            best_tree = new_tree
    return best_tree

if to_print == 'yes':
    print(tree_gain)
    print(tree_variance)
   
test_set['predicted_tree_gain'] = test_set.apply(tree_accuracy, axis=1, args=(tree_gain,'1') ) 
print( 'Accuracy with IG algrithm ' +  (str( sum(test_set['Class']==test_set['predicted_tree_gain'] ) / (0.01*len(test_set.index)) )))


test_set['predicted_tree_variance'] = test_set.apply(tree_accuracy, axis=1, args=(tree_variance,'1') ) 
print( 'Accuracy with Variance Impurity algorithm ' + (str( sum(test_set['Class']==test_set['predicted_tree_variance'] ) / (0.01*len(test_set.index)) )))

pruned_tree_gain = post_prune(L,K,tree_gain)
pruned_tree_variance = post_prune(L,K,tree_variance)

test_set['predicted_pruned_tree_gain'] = test_set.apply(tree_accuracy, axis=1, args=(pruned_tree_gain,'1') ) 
print( 'Accuracy with pruned IG tree ' + (str( sum(test_set['Class']==test_set['predicted_pruned_tree_gain'] ) / (0.01*len(test_set.index)) )))
test_set['predicted_pruned_tree_variance'] = test_set.apply(tree_accuracy, axis=1, args=(pruned_tree_variance,'1') ) 
print( 'Accuracy with pruned Variance Impurity tree ' + (str( sum(test_set['Class']==test_set['predicted_pruned_tree_variance'] ) / (0.01*len(test_set.index)) )))



# TODO: Test that this output aligns with data input

# print("L: {}".format(L))
# print("K: {}".format(K))
# print("Training Set: \n{}".format(training_set))
# print("Validation Set: \n{}".format(validation_set))
# print("Test Set: \n{}".format(test_set))
# print("To Print: {}".format(str(to_print)))
