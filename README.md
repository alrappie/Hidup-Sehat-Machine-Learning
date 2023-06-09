# Hidup-Sehat-Machine-Learning

There are 3 models for the machine learning in our apps

1. Object detection
   Our object detection using 7400+ images within 36 classes of food, trained with pre-trained model ssd mobilenet v2 fpnlite 640x640 40000 steps 64 batch.

2. Pose Estimation
   Extract the keypoint using movenet lightning model and calculate the similarity between user and the picture yoga selected with euclidean distance & angle.

3. Recommendation
   Give a content feeds recommendation based on user input, calculate the similarity using cosine similarity with tf-idf method.