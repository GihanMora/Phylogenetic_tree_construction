import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, LeakyReLU, Dropout
import math
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


train_df = pd.read_csv('Training_Data.csv')
def norm(x,stats):
  return (x - stats['mean']) / stats['std']
train_stats = {'mean':train_df.mean(),'std': train_df.std()}
normed_train_data = norm(train_df,train_stats)

train_X = normed_train_data.drop('kmerSimilarity', axis=1).values

train_Y = normed_train_data['kmerSimilarity'].values

X_train, X_test, y_train, y_test = train_test_split(train_X,train_Y,test_size=0.001)


print(type(X_test))
#random_state=6,21,8
# testData_with_names = pd.read_csv('testDatasetDeleted60_nonames.csv')

# print(train_df)
import keras.backend as K
import tensorflow as tf
accepted_diff = 0.09
def linear_regression_equality(y_true, y_pred):
    diff = K.abs(y_true-y_pred)
    return K.mean(K.cast(diff < accepted_diff, tf.float32))


targetLSH = 'LSH Similarity'
target = 'kmerSimilarity'

train_stats = {'mean':X_train.mean(),'std': X_train.std()}
test_stats = {'mean':X_test.mean(),'std': X_test.std()}

print('test_stat',test_stats)
print('train_stat',train_stats)
# def norm(x,stats):
#   return (x - stats['mean']) / stats['std']
# normed_train_data = norm(X_train,train_stats)
# normed_test_data = norm(X_test,train_stats)


model = Sequential()
# model.add(Dropout(0.2, input_shape=(36,)))
model.add(Dense(100, activation='relu',input_shape=(36,)))
model.add(Dense(50, activation='relu'))

model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=[linear_regression_equality])
# train_X = normed_train_data.drop(target, axis=1).values
#
# train_Y = normed_train_data[target].values

model.fit(
    X_train,
    y_train,
    epochs=50,
    verbose=2
)


# test_X = normed_test_data.drop(target, axis=1).values
# test_Y = normed_test_data[target].values

print("evaluate")
results = model.evaluate(X_test,y_test)
print(results)


model_json = model.to_json()
with open ('model.json','w') as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")



prediction = model.predict(X_test)
print(prediction)





predictionArray=[]

for i in prediction:
    predictionArray.append(i[0])
print("predicted max",predictionArray.index(max(predictionArray)))
print("ground truth max index",y_test.tolist().index(max(y_test)))

plt.plot(predictionArray)
# plt.show()
plt.plot(y_test)
# plt.plot(Y)
plt.show()
