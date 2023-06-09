# Object Detection
* The latest model is in workspace > models > 03-my_model > saved_model folder
* The latest TFlite model with metadata is in workspace > exported-models > 03-my_model_tflite > model_metadata_v2.tflite file
* The output sample of the model is in workspace > images_outputs_sample.ipynb file
* Label names is in workspace > annotations > labels.txt file

## How to run the model
Here's a step-by-step command for run the model.

1. clone the github
2. Copy the path of the latest saved_model
3. Import tensorflow and load the model 
    ```python
    import tensorflow as tf
    model = tf.saved_model.load(PATH_TO_SAVED_MODEL)
    ```

## How to train the model using terminal command
Here's a step-by-step command for train the model in the terminal.

### train tf record
```
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\datasets\food\train -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\03_model\train.record
```

### test tf record
```
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\datasets\food\test -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\03_model\test.record
```

### Train model

    python model_main_tf2.py --model_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640 --pipeline_config_path=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640\pipeline.config

### tensorboard
    tensorboard --logdir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640

### eval
    python model_main_tf2.py --pipeline_config_path=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640\pipeline.config --model_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640 --checkpoint_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640

### export
    python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\03_ssd_mobilenet_v2_fpnlite_640\pipeline.config --trained_checkpoint_dir D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\03_ssd_mobilenet_v2_fpnlite_640 --output_directory D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\03-my_model


### convert tflite
    python export_tflite_graph_tf2.py --trained_checkpoint_dir D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\03_ssd_mobilenet_v2_fpnlite_640 --output_directory D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\03-my_model_tflite --pipeline_config_path D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\03_ssd_mobilenet_v2_fpnlite_640\pipeline.config