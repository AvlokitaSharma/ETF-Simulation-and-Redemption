import simpy
import random
import pandas as pd
import matplotlib.pyplot as plt

def etf_process(env, etf_data, name, creation_size):
    while True:
        time = env.now
        print(f'{time}: {name} creation order processed')
        order_size = random.randint(100, 500)
        creation_size += order_size
        etf_data.append({"Time": time, "ETF Name": name, "Units": creation_size, "Order Size": order_size})
        yield env.timeout(random.randint(1, 10))  

def run_simulation():
    env = simpy.Environment()
    etf_data = []
    env.process(etf_process(env, etf_data, "ETF_A", 1000))  
    env.run(until=50)  e

    df = pd.DataFrame(etf_data)
    print(df.head())  
    return df

def plot_data(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Time'], df['Units'], label='Units in ETF')
    plt.title('ETF Units Over Time Due to Creation Orders')
    plt.xlabel('Time')
    plt.ylabel('Units')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    data = run_simulation()
    plot_data(data)
