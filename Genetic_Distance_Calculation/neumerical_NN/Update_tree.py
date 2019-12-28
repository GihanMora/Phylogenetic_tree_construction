import json
import os
import webbrowser

import pandas as pd
import keras.backend as K
import tensorflow as tf
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

from keras.models import model_from_json
json_file = open('model.json','r')
accepted_diff = 0.09
def linear_regression_equality(y_true, y_pred):
    diff = K.abs(y_true-y_pred)
    return K.mean(K.cast(diff < accepted_diff, tf.float32))
loaded_model_json = json_file.read()


json_file.close()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=[linear_regression_equality])

predict_data = pd.read_csv('Prediction_Data.csv')


New_specie = predict_data['DNA 1'].values[0]
Existing_species = predict_data['DNA 2'].values


predict_data = predict_data.drop('DNA 1', axis=1)
predict_data = predict_data.drop('DNA 2', axis=1)


def norm(x,stats):
  return (x - stats['mean']) / stats['std']

predicting_stats = {'mean':predict_data.mean(),'std': predict_data.std()}
# print(predicting_stats)

normed_predict_data = norm(predict_data,predicting_stats)
# print(normed_predict_data.head())

# print(New_specie,Existing_species)
prediction = loaded_model.predict(normed_predict_data)
predited_similarities = []
for each in prediction:
    predited_similarities.append(each)

# print( Existing_species[predited_similarities.index(max(predited_similarities))])

nearest_neighbour = Existing_species[predited_similarities.index(max(predited_similarities))]

print("Nearest Neighbour for the new specie",New_specie," is ",nearest_neighbour)



# tree updation visualization
with open('../kmedoid/kmer_tree.json') as f:
  data = json.load(f)

# print data;
parent = {}
def find_nn(data,parent,nearest_neighbour):
  # print data['name']
  if(data['name']==nearest_neighbour):
    print ("found")
    data['children'] = [{'name': nearest_neighbour},{'name':New_specie}]
    data['name'] = ''
  else:
    if('children' in data.keys()):
      find_nn(data['children'][0],data,nearest_neighbour)
      find_nn(data['children'][1],data, nearest_neighbour)


find_nn(data,{},nearest_neighbour)
with open('updated_tree.json', 'w') as outfile:
  json.dump(data, outfile)

filename = os.getcwd()+'/' + 'Updated_Tree_visualization.html'
webbrowser.open_new_tab(filename)