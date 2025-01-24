import numpy as np
import matplotlib.pyplot as plt


def sigmoid(sum):
    return 1 / (1 + np.exp(-sum))


def sigmoid_derivative(sigmoid):
    return sigmoid * (1 - sigmoid)


inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

weights0 = 2 * np.random.random((2, 3)) - 1
weights1 = 2 * np.random.random((3, 1)) - 1

epochs = 100000
learning_rate = 0.6
error = []

for epoch in range(epochs):
    input_layer = inputs
    sum_synapse0 = np.dot(input_layer, weights0)
    hidden_layer = sigmoid(sum_synapse0)

    sum_synapse1 = np.dot(hidden_layer, weights1)
    output_layer = sigmoid(sum_synapse1)

    error_output_layer = outputs - output_layer
    average = np.mean(abs(error_output_layer))
    if epoch % 10000 == 0:
        print('Epoch: ' + str(epoch + 1) + ' Error: ' + str(average))
        error.append(average)

    derivative_output = sigmoid_derivative(output_layer)
    delta_output = error_output_layer * derivative_output

    weights1T = weights1.T
    delta_output_weight = delta_output.dot(weights1T)
    delta_hidden_layer = delta_output_weight * sigmoid_derivative(hidden_layer)

    hidden_layerT = hidden_layer.T
    input_x_delta1 = hidden_layerT.dot(delta_output)
    weights1 = weights1 + (input_x_delta1 * learning_rate)

    input_layerT = input_layer.T
    input_x_delta0 = input_layerT.dot(delta_hidden_layer)
    weights0 = weights0 + (input_x_delta0 * learning_rate)


plt.xlabel('Epochs')
plt.ylabel('Error')
plt.plot(error)


def calculate_output(instance):
    hidden_layer = sigmoid(np.dot(instance, weights0))
    output_layer = sigmoid(np.dot(hidden_layer, weights1))
    return output_layer[0]


for i in range(len(inputs)):
    print(calculate_output(inputs[i]))


plt.show()
