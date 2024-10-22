import sys

from keras.models import load_model
import numpy as np
from PIL import Image

klasses = ["toy_poodle", "border_collie", "pomeranian"]
image_size = 50


def main():
    image_path = sys.argv[1]
    image = Image.open(image_path)
    image = image.convert('RGB')
    image = image.resize((image_size, image_size))
    data = np.asarray(image) / 255
    X = []
    X.append(data)
    X = np.array(X)
    model = load_model('./dogs.h5')

    result = model.predict([X])[0]
    predicted = result.argmax()
    print({ "class": klasses[predicted], "probability": result[predicted] })


if __name__ == "__main__":
    main()
