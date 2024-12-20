import csv
import numpy as np

theta0 = 12.715
theta1 = 17.615000000000002
data_len = 0
mileage = []
price = []

def estimate(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def read_data(dataset):
    global data_len
    global mileage
    global price
    with open(dataset) as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        for row in rows:
            mileage.append(row[0])
            price.append(row[1])
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

def train(dataset, learningRate):
    global  data_len
    global  mileage
    global  price
    i = 0
    const1 = learningRate * (1 / data_len)
    while (i <= data_len - 1):
        est = estimate(theta0, theta1, mileage[i] - price[i])
        theta0 += est
        theta1 += est * mileage[i]
        i += 1
    theta0 = const1 * theta0
    theta1 = const1 * theta1
    change_thetas(theta0, theta1)

if __name__ == "__main__":
    train("data.csv")
    #reset()