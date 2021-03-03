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

print(sys.argv)

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

print("L: {}".format(L))
print("K: {}".format(K))
print("Training Set: \n{}".format(training_set))
print("Validation Set: \n{}".format(validation_set))
print("Test Set: \n{}".format(test_set))
print("To Print: {}".format(str(to_print)))
