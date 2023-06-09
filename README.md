# Hidup-Sehat-Machine-Learning

In our apps, there are three machine learning models.

1. Object recognition Our object detection model was trained with a pre-trained model ssd mobilenet v2 fpnlite 640x640 40000 steps 64 batch on 7400+ images from 36 food classes.

2. Yoga Pose Evaluation Using the movenet lightning model, extract the keypoint and calculate the similarity between the user and the yoga image with euclidean distance and angle.

3. Recommendation Based on user input, recommend content feeds and calculate similarity using cosine similarity and the tf-idf method.