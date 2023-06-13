# Hidup-Sehat-Machine-Learning

In our apps, there are three 2 deep learning models and 1 machine learning model, for each model will be explain in each folder

1. Object recognition Our object detection model was trained with a pre-trained model ssd mobilenet v2 fpnlite 640x640 40000 steps 64 batch on 7400+ images from 36 food classes.

2. Yoga Pose Evaluation Using the movenet lightning model, extract the keypoint and calculate the similarity between the user and the yoga image with euclidean distance and 8 angle.

3. Recommendation Based on user input, recommend content feeds and calculate similarity using cosine similarity and the tf-idf method.

4. Scraping nutriet foods from fatsecret and feeds content from halodoc using BeautifulSoup

# Library, Pre-Trained Model, & Method Used
* [TensorFlow](https://www.tensorflow.org/?hl=id)
* [TensorFlow SSD MobileNet v2 fpnlite 640x640](https://github.com/tensorflow/models/tree/master/research/object_detection)
* [TensorFlow Movenet Lightning](https://tfhub.dev/google/movenet/singlepose/lightning/)
* [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
* [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
* [NLTK](https://www.nltk.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Regex](https://regexr.com/)
* [TF-IDF](https://www.capitalone.com/tech/machine-learning/understanding-tf-idf/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Matplotlib](https://matplotlib.org/)
* [difPy](https://pypi.org/project/difPy/)
* [PIL](https://pillow.readthedocs.io/en/stable/)
* [xml](https://docs.python.org/3/library/xml.etree.elementtree.html)
