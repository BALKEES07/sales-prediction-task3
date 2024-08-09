import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("/archive.zip")
df.head()
df.head(10)
df.shape
df.describe()
sns.pairplot(df, x_vars=['TV', 'Radio','Newspaper'], y_vars='Sales', kind='scatter')
plt.show()
df['TV'].plot.hist(bins=10)
df['Radio'].plot.hist(bins=10, color="green", xlabel="Radio")
df['Newspaper'].plot.hist(bins=10,color="purple", xlabel="newspaper")
sns.heatmap(df.corr(),annot = True)
plt.show()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['TV']], df[['Sales']], test_size = 0.3,random_state=0)
print(X_train)
print(y_train)
print(X_test)
print(y_test)
res= model.predict(X_test)
print(res)
