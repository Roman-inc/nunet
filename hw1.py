import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


inputs = np.array([[18,2], [20,3], [21, 4], [35,15], [36,16], [38, 18]])
test_input = np.array([[17,5], [25,8], [45,10], [31,20]])
outputs = np.array([0, 0, 0, 1, 1, 1])
weights = np.array([0.0, 0.0])
learning_rate = 0.001

scaler = MinMaxScaler()
inputs = scaler.fit_transform(inputs)
test_input = scaler.transform(test_input)


df1 = pd.DataFrame(data=inputs, columns=["age", "educational"])
df2 = pd.DataFrame(data=outputs, columns=["class"])
df = pd.concat([df1, df2], axis=1)

df11 = pd.DataFrame(data=test_input, columns=["age", "educational"])
df21 = pd.DataFrame(data=outputs, columns=["class"])
dff = pd.concat([df11, df21], axis=1)


def build_chart():
    print(dff)
    sns.relplot(x="age", y="educational", data=dff, hue="class")
    plt.show()


def step_function(sum):
    if sum >= 1:
        return 1
    return 0


def calculate_output(instance):
    s = instance.dot(weights)
    return step_function(s)


def train():
    total_error = 1
    iteration = 1
    while total_error != 0:
        total_error = 0
        print(f'Iteration: {str(iteration)}')
        for i in range(len(outputs)):
            prediction = calculate_output(inputs[i])
            error = abs(outputs[i] - prediction)
            total_error += error
            if error > 0:
                for j in range(len(weights)):
                    weights[j] = weights[j] + (learning_rate * inputs[i][j] * error)
                    print(f'Weight updated: {str(weights[j])}')

        iteration += 1
        print(f'Total errors: {str(total_error)}')
    return weights


train()




def checkIt():
    print(f'new weights: {weights}\nNew test_input: {test_input}')
    for i in range(len(test_input)):
        print(f'Prediction for {i} : {calculate_output(test_input[i])}')


checkIt()

build_chart()


