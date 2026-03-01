import tensorflow as tf
from tensorflow.keras import layers, models, Input

def create_transformer(input_shape):
    inputs = Input(shape=input_shape)
    x = layers.MultiHeadAttention(num_heads=4, key_dim=4)(inputs, inputs)
    x = layers.LayerNormalization(epsilon=1e-6)(x + inputs)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    model = models.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")
    return model
