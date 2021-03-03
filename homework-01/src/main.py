"""
.\program <L> <K> <training-set> <validation-set> <test-set> <to-print>
L: integer (used in the post-pruning algorithm)
K: integer (used in the post-pruning algorithm)
to-print:{yes,no}
"""

input_string = "2 5 data_sets_1/training_set.csv data_sets_1/validation_set.csv data_sets_1/test_set.csv yes"

print(input_string)
inputs = input_string.split(" ")
print(inputs)

L = inputs[0]
K = inputs[1]
training_set_path = inputs[2]
validation_set_path = inputs[3]
test_set_path = inputs[4]
to_print = inputs[5]

# csv.reader(training_set_path)

training_set = training_set_path
validation_set = validation_set_path
test_set = test_set_path

print(L)
print(K)
print(training_set)
print(validation_set)
print(test_set)
print(to_print)
