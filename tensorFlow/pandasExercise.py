import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# print(pd.__version__)

names = pd.Series(["Zhang", "Li", "Wang"])
ages = pd.Series([12, 22, 32])

persons = pd.DataFrame({"name": names, "age": ages})
print(persons)
# print(persons.describe())
# df.hist()
# print("\nlog(age): \n", np.log(persons['age']))
# print("\nage>=18\n", ages.apply(lambda a: a >= 18))

persons['income'] = pd.Series([0, 1000, 6000])
persons['income/age'] = persons['income'] / persons['age']
print(persons)

# california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
# print(california_housing_dataframe.describe())
# california_housing_dataframe.hist('housing_median_age')
# plt.show()
