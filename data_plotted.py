import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# matplotlib inline
sns.set_context('notebook')
plt.style.use('fivethirtyeight')
from warnings import filterwarnings
filterwarnings('ignore')

# Import the data
data_frame = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/dummy_data.csv')

# Plot the data
plt.figure(figsize=(8, 8))
plt.scatter(data_frame.iloc[:, 0], data_frame.iloc[:, 1])
plt.xlabel('Eruption time (minutes)', fontsize=16)
plt.ylabel('Waiting time to next eruption (minutes)', fontsize=16)
plt.title('Visualization of Eruption Data from \n Old Faithful Geyser, Yellowstone,USA', fontsize=20, fontweight='bold')
plt.savefig('plot-data.png')
