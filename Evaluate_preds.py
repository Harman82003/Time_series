def evaluate_preds(y_true,y_pred):
  import tensorflow as tf
    y_true=tf.cast(y_true,dtype=tf.float32)
    y_pred=tf.cast(y_pred,dtype=tf.float32)
    mae=tf.keras.metrics.mean_absolute_error(y_true,y_pred)
    mse=tf.keras.metrics.mean_squared_error(y_true,y_pred)
    rmse=tf.sqrt(mse)
    mape=tf.keras.metrics.mean_absolute_percentage_error(y_true,y_pred)
    mase=mean_absolute_scaled_error(y_true,y_pred)
    return{"mae":mae.numpy()
           ,"mse":mse.numpy()
           ,"rmse":rmse.numpy()
           ,"mape":mape.numpy()
           ,"mase":mase.numpy()}
