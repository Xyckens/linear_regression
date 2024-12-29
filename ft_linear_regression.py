import csv
import numpy as np
import matplotlib.pyplot as plt

theta0 = 0
theta1 = 0

class   linear_regression:

    data_len = 0
    mileage = []
    price = []
    fig, ax = plt.subplots()
    x = np.linspace(-2 , 3, 100)
    line, = ax.plot(x, 0 * x)

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        try:
            with open(dataset) as csvfile:
                rows = csv.reader(csvfile)
                next(rows)
                for row in rows:
                    self.mileage.append(int(row[0]))
                    self.price.append(int(row[1]))
                    self.data_len += 1
            self.mileage = (self.mileage - np.mean(self.mileage)) / np.std(self.mileage)
            self.price = (self.price - np.mean(self.price)) / np.std(self.price)
            plt.ion() #interactive mode
            plt.plot(self.mileage, self.price, 'r.')
            plt.ylabel("Pricing")
            plt.xlabel("Mileage")
            plt.title("Price Prediction")
            plt.legend(["My LR", "Real Points", "Numpy LR"])

        except:
            print ("Couldn't open", dataset)

    def change_thetas(self, final_theta0, final_theta1) -> None:
        try: 
            with open(__file__, 'r') as f:
                lines = f.read().split('\n')
                new_theta0 = f'theta0 = {final_theta0}'
                new_theta1 = f'theta1 = {final_theta1}'
                new_file = '\n'.join(lines[:4] + [new_theta0] + [new_theta1] + lines[6:])

            with open(__file__, 'w') as f:
                f.write(new_file)
        except:
            print ("Couldn't open", __file__)


    def reset(self) -> None:
        self.change_thetas(0, 0)

    #explica learning rate hyperparameter
    #mas basicamente, pequeno de mais e demora muito a convergir,
    # grande demais e nunca converge
    #https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters

    def estimate(self, theta0, theta1, mileage) -> float:
        return theta0 + theta1 * mileage

    def train(self, learningRate, theta0, theta1) -> tuple[float, float]:
        i = 0
        sum0 = 0
        sum1 = 0
        while (i <= self.data_len - 1):
            est = self.estimate(theta0, theta1, self.mileage[i]/100000) - self.price[i] / 1000
            #print(f"est =  {est:.2e}")
            sum0 += est
            sum1 += est * self.mileage[i]
            i += 1
        const = learningRate / self.data_len
        return const * sum0, const * sum1

    def find_learning_rate(self) -> None:
        global  theta0
        global  theta1
        delta0 = 11
        delta1 = 11
        learningRate = 0.01
        iteration = 0
        while (iteration < 30):
            new0, new1 = self.train(learningRate, theta0, theta1)
            delta0 = abs(theta0 - new0)
            delta1 = abs(theta1 - new1)
            print(f"new0 {new0:.03e} and new1 {new1:.03e} delta0 {delta0:.03e} delta1 {delta1:.03e}")
            theta0 = new0
            theta1 = new1
            iteration += 1
            '''
            if (delta0 > 1000000000 or delta1 > 1000000000):
                print("delta got too high")
                break
            '''
            self.data_graph(theta0, theta1)
        m,b = np.polyfit(np.array(self.mileage), np.array(self.price), 1)
        print(m, b)
        plt.plot(self.x, b + m * self.x, "g")
        print("iterations = ", iteration)
        plt.ioff()
        plt.show()

    #bonus   
    def data_graph(self, theta0, theta1) -> None:
        y = theta0 + self.x * theta1
        self.line.set_ydata(y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.1)

    def precision(self,theta0, theta1) -> float: #mean absolute error
        i = 0
        est = 0
        while (i <= self.data_len - 1):
            est += abs(self.estimate(theta0, theta1, self.mileage[i]) - self.price[i])
            i += 1
        return est / self.data_len
    

if __name__ == "__main__":
    result = linear_regression("data.csv")
    result.find_learning_rate()
    #reset()