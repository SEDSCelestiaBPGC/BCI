import numpy as np
import os
import shutil
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.layers import BatchNormalization

options = ['left', 'right']
test_size = 0.3

try:
  os.mkdir('data/')
  os.mkdir('data/left')
  os.mkdir('data/right')
  os.mkdir('test_data/')
  os.mkdir('test_data/left')
  os.mkdir('test_data/right')
  os.mkdir('validation_data/')
  os.mkdir('validation_data/left')
  os.mkdir('validation_data/right')
except:
  OSError

left_imagery = []  # list of left .npy files
right_imagery = []  # list of right .npy files
data_left = []  # list of loaded content of left .npy files
data_right = []  # list of loaded content of right .npy files

for filenames in os.listdir('/content'):
  if filenames.startswith('bci_imagery_left'):
    data_l = np.load(filenames)
    data_left.append(data_l)
    left_imagery.append(filenames)
  elif filenames.startswith('bci_imagery_right'):
    data_r = np.load(filenames)
    data_right.append(filenames)
    right_imagery.append(filenames)

for actions in options:
  if actions == 'left':
    train_left = []
    test_left = []

    num_test = int(len(left_imagery))
    indices = list(range(num_test))
    np.random.shuffle(indices)
    print(indices)
    split = int(test_size * len(left_imagery))
    print(split)
    train_idx, test_idx = indices[split:], indices[:split]

    for indices in train_idx:
      train_left.append(left_imagery[indices])
    for indices in test_idx:
      test_left.append(left_imagery[indices])

    #print(train_left)
    #print('\n')
    #print(test_left)

    for i in range(len(train_left)):
      shutil.copy(train_left[i], 'data/left')
    for j in range(len(test_left)):
      shutil.copy(test_left[j], 'test_data/left')

  elif actions == 'right':
    train_right = []
    test_right = []

    num_test = int(len(right_imagery))
    indices = list(range(num_test))
    np.random.shuffle(indices)
    split = int(test_size * len(right_imagery))
    train_idx, test_idx = indices[split:], indices[:split]

    for indices in train_idx:
      train_right.append(right_imagery[indices])
    for indices in test_idx:
      test_right.append(right_imagery[indices])

    for i in range(len(train_right)):
      shutil.copy(train_right[i], 'data/right')
    for j in range(len(test_right)):
      shutil.copy(test_right[j], 'test_data/right')

# List of training data + labels
combined_data = [] 

# Create training data
l = []
r = []

for item in os.listdir('data/left'):
  datal = np.load(os.path.join('data/left', item))
  for item in datal:
    l.append(item)
for datas in l:
  combined_data.append([datas, [1, 0]])  # [1, 0] for left

for item in os.listdir('data/right'):
  datar = np.load(os.path.join('data/right', item))
  for item in datar:
    r.append(item)
for datas in r:
  combined_data.append([datas, [0, 1]])  # [0, 1] for right


# Create testing data
l1 = []
r1 = []

# List of testing data + labels
combined_data_test = []

for item in os.listdir('test_data/left'):
  datal = np.load(os.path.join('test_data/left', item))
  for item in datal:
    l1.append(item)
for datas in l1:
  combined_data_test.append([datas, [1, 0]])

for item in os.listdir('test_data/right'):
  datar = np.load(os.path.join('test_data/right', item))
  for item in datar:
    r1.append(item)
for datas in r1:
  combined_data_test.append([datas, [0, 1]])

train_x = []
train_y = []
for x, y in combined_data:
  train_x.append(x)
  train_y.append(y)

test_x = []
test_y = []
for x, y in combined_data_test:
  test_x.append(x)
  test_y.append(y)

train_x = np.array(train_x).reshape((-1, 64, 3584))
train_y = np.array(train_y)
test_x = np.array(test_x).reshape((-1, 64, 3584))
test_y = np.array(test_y)

batch_size = 32

# Model 
model = Sequential()
model.add(Conv1D(16, (3), input_shape=train_x.shape[1:]))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling1D(pool_size=(2)))

model.add(Conv1D(32, (2)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling1D(pool_size=(2)))

model.add(Conv1D(64, (2)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling1D(pool_size=(2)))

model.add(Flatten())

model.add(Dropout(0.25))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(BatchNormalization())

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.25))
model.add(BatchNormalization())

model.add(Dense(2))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='adam')

epochs = 25
for e in range(epochs):
  history = model.fit(train_x, train_y, batch_size=batch_size, epochs=1, validation_data=(test_x, test_y))
  model_performance = model.evaluate(test_x, test_y, verbose=0)
  model.save('Model with performance: {}'.format(model_performance))
  print(model_performance)

# For analysis
from sklearn.metrics import classification_report, confusion_matrix

predictions = model.predict(test_x)

pred = np.argmax(predictions, axis=1)
label = np.argmax(test_y, axis=1)

print(classification_report(label, pred))
print('\n')
print(confusion_matrix(label, pred))
