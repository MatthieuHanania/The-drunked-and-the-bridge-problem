import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the given data
data = {
    'max_steps_per_drunked': [2000, 3000, 5000, 8000, 10000, 15000, 20000],
    '%_of_falling_at_left': [5.4, 9.66, 14.29, 16.35, 16.83, 16.85, 17.26],
    '%_of_falling_at_right': [70.53, 75.73, 80.33, 82.36, 82.69, 83.15, 82.74],
    'sum_of_%_falling': [75.93, 85.4, 94.62, 98.71, 99.52, 99.95, 100.00],
    'time_(s)': [45.5, 56.9, 63.6, 67.4, 70.7, 66.9, 69.6]
}

df = pd.DataFrame(data)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['max_steps_per_drunked'], df['%_of_falling_at_left'], marker='o', linestyle='-', color='b')
plt.title('Probability of Falling to the Left per Max Steps')
plt.xlabel('Max Steps per Drunked')
plt.ylabel('% Chance of Falling to the Left')
plt.grid(True)
plt.show()
