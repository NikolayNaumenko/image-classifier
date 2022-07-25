import os
import json
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub
import warnings
import logging

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

IMAGE_SIZE = 224
URL = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
EXCEPTION_MSG = 'Provided top_k value ({}) is greater than the number of model classes ({})'


def get_class_name_by_label_fn(label_map_path):
    if label_map_path is not None:
        with open(label_map_path, 'r') as f:
            class_names = json.load(f)

        return lambda label: '{} ({})'.format(class_names[str(label + 1)].title(), label)
    else:
        return lambda label: label


def load_image(image_path):
    loaded_image = Image.open(image_path)
    return np.array(loaded_image)


def process_image(image):
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, (IMAGE_SIZE, IMAGE_SIZE))
    image /= 255

    return image


def to_sorted_dict(predictions):
    return sorted(dict(predictions).items(), key=lambda item: item[1], reverse=True)


def predict(image_path, model, top_k, get_class_name_by_label):
    image = load_image(image_path)
    processed_test_image = np.expand_dims(process_image(image), axis=0)
    predictions = model.predict(processed_test_image, verbose=0)[0]

    if len(predictions) < top_k:
        raise Exception(EXCEPTION_MSG.format(top_k, len(predictions)))

    indices = np.argpartition(predictions, -top_k)[-top_k:]
    zipped_result = zip(map(get_class_name_by_label, indices), predictions[indices])

    return to_sorted_dict(zipped_result)


def load_model(model_filename):
    feature_extractor = hub.KerasLayer(URL, input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3))

    return tf.keras.models.load_model(model_filename, custom_objects={'KerasLayer': feature_extractor})
