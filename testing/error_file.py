import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.learning_rate = learning_rate
        self.input_size = input_size

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[:self.input_size]) + self.weights[-1]  # Weighted sum + bias
        activation = 1 if summation > 0 else 0  # Activation function
        return activation

    def train(self, inputs, label):
        prediction = self.predict(inputs)
        error = label - prediction
        self.weights[:self.input_size] += self.learning_rate * error * inputs  # Update weights
        self.weights[-1] += self.learning_rate * error  # Update bias

    def accuracy(self, test_inputs, test_labels):
        correct_predictions = 0
        for i in range(len(test_inputs)):
            prediction = self.predict(test_inputs[i])
            if prediction == test_labels[i]:
                correct_predictions += 1
        return correct_predictions / len(test_inputs)