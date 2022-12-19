from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('./data.csv')
feature = ['Age', 'Handsome','Height', 'Body Fat%', 'Crazy on work',
           'Attitude', 'Wage', 'Temper', 'Responsibility',
           'Have a cat', 'Ma bao', 'Have a car', 'Have a house', 'Have a rich dad',
           'Jai Jai']
x = df[feature]

y = df['Label']





train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=0)


model = DecisionTreeClassifier()                # 創造決策樹模型
model.fit(train_x, train_y)                     # 訓練決策樹模型

pred_y = model.predict(test_x)                 # 確認模型是否訓練成功
acc = accuracy_score(test_y, pred_y)           # 計算準確度
plot_tree(model,feature_names=feature,class_names="01")                  # 繪製訓練後的模型
plt.savefig('./tree.png')
print('accuracy: {}'.format(acc))               # 輸出準確度

model = DecisionTreeClassifier(                 # 創造決策樹模型
    # criterion='gini',                           # 設定最佳化方法為 Gini Index
    max_depth=5,                                # 設定最大深度為 2
    )                      # 設定最多葉子個數為 4

model.fit(train_x, train_y)                     # 訓練決策樹模型

pred_y = model.predict(test_x)                 # 確認模型是否訓練成功
# acc = accuracy_score(test_y, pred_y)           # 計算準確度

print("Accuracy:", metrics.accuracy_score(test_y, pred_y))
from sklearn.metrics import classification_report
print(classification_report(test_y, pred_y))
fig, ax = plt.subplots(figsize=(100, 100)) # 創造繪圖環境

plot_tree(model,feature_names=feature,class_names="01", ax=ax)                  # 繪製訓練後的模型
plt.savefig('./tree_d5.png')
from sklearn.metrics import confusion_matrix
import seaborn as sns
mat = confusion_matrix(test_y, pred_y)
print(mat)
fig = plt.figure()
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=[0, 1], yticklabels=[0,1])
plt.xlabel('true label')
plt.ylabel('predicted label');

fig.savefig('./tree_d5_confusion_matrix.png')
