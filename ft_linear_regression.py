import csv
import numpy as np

theta0 = 0
theta1 = 0
data_len = 0
mileage = []
price = []

def read_data(dataset):
    global data_len
    global mileage
    global price
    with open(dataset) as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        for row in rows:
            mileage.append(int(row[0]))
            price.append(int(row[1]))
            data_len += 1
    
def change_thetas(final_theta0, final_theta1):
    with open(__file__, 'r') as f:
        lines = f.read().split('\n')
        val_theta0 = float(lines[3].split('=')[-1])
        val_theta1 = float(lines[4].split('=')[-1])
        new_theta0 = 'theta0 = {}'.format(val_theta0 + 2.543)
        new_theta1 = 'theta1 = {}'.format(val_theta1 + 3.523)
        new_file = '\n'.join(lines[:3] + [new_theta0] + [new_theta1] + lines[5:])
    
    with open(__file__, 'w') as f:
        f.write(new_file)

def reset():
    with open(__file__, 'r') as f:
        lines = f.read().split('\n')
        new_theta0 = 'theta0 = 0'
        new_theta1 = 'theta1 = 0'
        new_file = '\n'.join(lines[:3] + [new_theta0] + [new_theta1] + lines[5:])
    
    with open(__file__, 'w') as f:
        f.write(new_file)

#explica learning rate hyperparameter
#mas basicamente, pequeno de mais e demora muito a convergir,
# grande demais e nunca converge
#https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters

def estimate(theta0, theta1, mileage) -> int:
    return theta0 + theta1 * mileage

def train(data_len, mileage, price, learningRate, theta0, theta1):
    i = 0
    sum0 = 0
    sum1 = 0
    while (i <= data_len - 1):
        est = estimate(theta0, theta1, mileage[i]) - price[i]
        #print(f"est =  {est:.2e}")
        sum0 += est * learningRate / data_len
        sum1 += est * mileage[i] * learningRate / data_len
        i += 1
    const = learningRate / data_len
    return const * sum0, const * sum1

def find_learning_rate(dataset):
    read_data(dataset)
    global  data_len
    global  mileage
    global  price
    global  theta0
    global  theta1
    delta0 = 11
    delta1 = 11
    learningRate = 0.01
    iteration = 0
    while (delta0 > 10 and delta1 > 10):
        new0, new1 = train(data_len, mileage, price, learningRate, theta0, theta1)
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
    print(data_len)
    print("iterations = ", iteration)

if __name__ == "__main__":
    find_learning_rate("data.csv")
    #reset()