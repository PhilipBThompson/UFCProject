###################################
# Import Packages
###################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


###################################
# Import CSV
###################################
trainingData = pd.read_csv(
    'Feb 2022 MySQL Octotrage Training.csv', index_col=0)
testingData = pd.read_csv('Feb 2022 MySQL Octotrage Testing.csv', index_col=0)
# print(trainingData)
# print(testingData)


###################################
# Exploratory Data Analysis
###################################
fighterA_age_training = trainingData.loc[:, 'AAge']
fighterB_age_training = trainingData.loc[:, 'BAge']
age_training = np.concatenate((fighterA_age_training, fighterB_age_training))
# plt.hist(fighterA_age_training, bins=15)
# plt.title('Fighter A Age Training', fontsize=20, color="black")
# plt.show()
# plt.hist(fighterB_age_training, bins=15)
# plt.show()
# plt.hist(age_training, bins=10)
# plt.title('Training Dataset Combined Age Distribution', fontsize=20, color="black")
# plt.show()

fighterA_height_training = trainingData.loc[:, 'AHeight']
fighterB_height_training = trainingData.loc[:, 'BHeight']
height_training = np.concatenate(
    (fighterA_height_training, fighterB_height_training))
fighterA_reach_training = trainingData.loc[:, 'AReach']
fighterB_reach_training = trainingData.loc[:, 'BReach']
reach_training = np.concatenate(
    (fighterA_reach_training, fighterB_reach_training))
fighterA_winpercentage_training = trainingData.loc[:, 'AWinPercentage']
fighterB_winpercentage_training = trainingData.loc[:, 'BWinPercentage']
winpercentage_training = np.concatenate(
    (fighterA_winpercentage_training, fighterB_winpercentage_training))

sns.set_context("talk", font_scale=1.1)
sns.scatterplot(x=fighterA_height_training,
                y=fighterA_reach_training,
                size=fighterA_winpercentage_training,
                sizes=(0, 100),
                data=trainingData)
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
plt.xlabel("Height")
plt.title("Training Dataset - Fight A")
plt.ylabel("Reach")
plt.show()
plt.pause(3)
plt.close()
