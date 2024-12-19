import csv
import numpy as np

theta0 = 12.715
theta1 = 17.615000000000002

def estimate(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def train(dataset):
    mileage = []
    price = []
    counter = 0
    with open(dataset) as csvfile:
        rows = csv.reader(csvfile)
        next(rows)
        for row in rows:
            mileage.append(row[0])
            price.append(row[1])
            counter += 1
    
def change_thetas():
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

if __name__ == "__main__":
    train("data.csv")
    #reset()