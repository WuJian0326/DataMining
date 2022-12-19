from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv')
feature = ['Age', 'Handsome','Height', 'Body Fat%', 'Crazy on work',
           'Attitude', 'Wage', 'Temper', 'Responsibility',
           'Have a cat', 'Ma bao', 'Have a car', 'Have a house', 'Have a rich dad',
           'Jai Jai']

x = df[feature]
y = df['Label']


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

clf = GaussianNB()
clf = clf.fit(X_train, y_train)
y_prediction = clf.predict(X_test)



print("Accuracy:", metrics.accuracy_score(y_test, y_prediction))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_prediction))

from sklearn.metrics import confusion_matrix
import seaborn as sns
mat = confusion_matrix(y_test, y_prediction)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=[0, 1], yticklabels=[0,1])
plt.xlabel('true label')
plt.ylabel('predicted label');
plt.savefig('./NaiveBayes.png')
plt.show()