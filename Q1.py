


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





from sklearn.datasets import load_iris





iris = datasets.load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

iris_df['species'] = iris.target

print("First 10 Rows of the Dataset:")

print(iris_df.head(10))







