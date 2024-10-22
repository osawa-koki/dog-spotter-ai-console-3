import sys
import urllib.request

from keras.models import load_model
import numpy as np
from PIL import Image

klasses = ["toy_poodle", "border_collie", "pomeranian"]
image_size = 50


def main():
    argv = sys.argv
    if len(argv) < 2:
        i = input("Please provide an image URL: ")
        argv.append(i)
    url = argv[1]
    if url.startswith("data:image"):
        raise ValueError("Please provide a valid image URL")
    if url.startswith("http"):
        urllib.request.urlretrieve(url, "image.jpeg")
        print("Downloaded image from URL")
    image = Image.open("image.jpeg")
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
