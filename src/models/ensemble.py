import tensorflow as tf
from tensorflow.keras import layers

def get_ensemble_models(horizon,
                        train_data,
                        test_data,
                        num_iter = 10,
                        num_epochs = 1000,
                        loss_fns = ['mae', 'mse', 'mape']):
  '''
  Returns a list of num_iter models each trained on MAE, MSE and MAPE loss.

  For example, if num_iter = 10, a list of 30 trained models will be returend:
  10 * len(['mae', 'mse', 'mape']).
  '''
  # Make empty list for trained ensemble models
  ensemble_models = []

  # Create num_iterm number of models perf loss function
  for i in range(num_iter):
    for loss_function in loss_fns:
      print(f'Optimizing model by reducing: {loss_function} for {num_epochs} epochs, model number: {i}')

      # Create model and initialize dense layers with normal distribution for estimating prediction intervals later on
      model = tf.keras.Sequential([
          layers.Dense(128, kernel_initializer = 'he_normal', activation = 'relu'),
          layers.Dense(128, kernel_initializer = 'he_normal', activation = 'relu'),
          layers.Dense(horizon)
      ])

      # Compile
      model.compile(loss = loss_function,
                    optimizer = tf.keras.optimizers.Adam(),
                    metrics = ['mae', 'mse'])

      # Fit the current model
      model.fit(train_data,
                epochs = num_epochs,
                validation_data = test_data,
                verbose = 0,
                callbacks = [tf.keras.callbacks.EarlyStopping(monitor = 'val_loss',
                                                              patience = 200,
                                                              restore_best_weights = True),
                             tf.keras.callbacks.ReduceLROnPlateau(monitor = 'val_loss',
                                                                  patience = 100,
                                                                  verbose = 1)])

      # Append fitted model
      ensemble_models.append(model)

  return ensemble_models


def make_ensemble_preds(ensemble_models, data):
  ensemble_preds = []
  for model in ensemble_models:
    preds = model.predict(data)
    ensemble_preds.append(preds)
  return tf.constant(tf.squeeze(ensemble_preds))