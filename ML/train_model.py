import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = [[0.1, 0.2], [0.9, 0.8], [0.5, 0.5]]
y = [0, 1, 1]

model = Sequential([
    Dense(5, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10)
model.save("arm_model.h5")