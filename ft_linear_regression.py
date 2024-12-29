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
    x = np.linspace(20000 , 250000, 100)
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
            plt.ion() #interactive mode
            plt.plot(self.mileage, self.price, 'r.')
            plt.ylabel("Pricing")
            plt.xlabel("Mileage")
            plt.title("Price Prediction")
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

    def train(self, data_len, mileage, price, learningRate, theta0, theta1) -> tuple[float, float]:
        i = 0
        sum0 = 0
        sum1 = 0
        while (i < data_len - 1):
            est = self.estimate(theta0, theta1, mileage[i]) - price[i]
            #print(f"est =  {est:.2e}")
            sum0 += est
            sum1 += est * mileage[i]
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
        '''while (delta0 > 10 and delta1 > 10):
            new0, new1 = self.train(self.data_len, self.mileage, self.price, learningRate, theta0, theta1)
            delta0 = abs(theta0 - new0)
            delta1 = abs(theta1 - new1)
            print(f"new0 {new0:.03e} and new1 {new1:.03e}")
            theta0 = new0
            theta1 = new1
            iteration += 1
            if (delta0 > 1000000000 or delta1 > 1000000000):
                print("delta got too high")
                break
            self.data_graph(theta0, theta1)
        '''
        m,b = np.polyfit(np.array(self.mileage), np.array(self.price), 1)
        print(m, b)
        self.data_graph(b, m)
        print("iterations = ", iteration)
        plt.ioff()
        plt.show()

    #bonus   
    def data_graph(self, theta0, theta1):
        print(theta0, theta1)
        y = theta0 + self.x * theta1
        print(self.x, y)
        self.line.set_ydata(y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.1)
    

if __name__ == "__main__":
    result = linear_regression("data.csv")
    result.find_learning_rate()
    #reset()