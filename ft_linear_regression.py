import csv
import numpy as np

theta0 = 0
theta1 = 0

class   linear_regression:

    data_len = 0
    mileage = []
    price = []

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        with open(dataset) as csvfile:
            rows = csv.reader(csvfile)
            next(rows)
            for row in rows:
                self.mileage.append(int(row[0]))
                self.price.append(int(row[1]))
                self.data_len += 1

    def change_thetas(self, final_theta0, final_theta1) -> None:
        with open(__file__, 'r') as f:
            lines = f.read().split('\n')
            new_theta0 = 'theta0 = {}'.format(final_theta0)
            new_theta1 = 'theta1 = {}'.format(final_theta1)
            new_file = '\n'.join(lines[:3] + [new_theta0] + [new_theta1] + lines[5:])

        with open(__file__, 'w') as f:
            f.write(new_file)

    def reset(self) -> None:
        self.change_thetas(0, 0)

    #explica learning rate hyperparameter
    #mas basicamente, pequeno de mais e demora muito a convergir,
    # grande demais e nunca converge
    #https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters

    def estimate(self, theta0, theta1, mileage) -> float:
        return theta0 + theta1 * mileage

    def train(self, data_len, mileage, price, learningRate, theta0, theta1) -> tuple[float, float]:
        i = 0
        sum0 = 0
        sum1 = 0
        while (i <= data_len - 1):
            est = self.estimate(theta0, theta1, mileage[i]) - price[i]
            #print(f"est =  {est:.2e}")
            sum0 += est * learningRate / data_len
            sum1 += est * mileage[i] * learningRate / data_len
            i += 1
        const = learningRate / data_len
        return const * sum0, const * sum1

    def find_learning_rate(self) -> None:
        global  theta0
        global  theta1
        delta0 = 11
        delta1 = 11
        learningRate = 0.01
        iteration = 0
        while (delta0 > 10 and delta1 > 10):
            new0, new1 = self.train(self.data_len, self.mileage, self.price, learningRate, theta0, theta1)
            delta0 = abs(theta0 - new0)
            delta1 = abs(theta1 - new1)
            theta0 = new0
            theta1 = new1
            print(f"delta0 {delta0:.3e}, delta1 {delta1:.3e}, theta0 {theta0:.03e} and theta1 {theta1:.03e}")
            iteration += 1
            '''
            if (delta0 > 1000000000 or delta1 > 1000000000):
                print("delta got too high")
                break
            '''
        #change_thetas(0, 0)
        print(self.data_len)
        print("iterations = ", iteration)

if __name__ == "__main__":
    result = linear_regression("data.csv")
    result.find_learning_rate()
    #reset()