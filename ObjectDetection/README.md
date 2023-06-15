# Object Detection
We Used Linux Terminal (from SSH GPU rent using [vast.ai](https://vast.ai/)) for train the model

* The latest model is in workspace > models > 03-my_model > saved_model folder or can be accessed [here](https://github.com/Hidup-Sehat/Hidup-Sehat-Machine-Learning/tree/main/ObjectDetection/workspace/exported-models/03-my_model).
* The latest TFlite model with metadata is in workspace > exported-models > 03-my_model_tflite > model_metadata_v2.tflite file or can be accessed [here](https://github.com/Hidup-Sehat/Hidup-Sehat-Machine-Learning/blob/main/ObjectDetection/workspace/exported-models/03-my_model_tflite/model_metadata_v2.tflite)
* The output sample of the model is in workspace > images_outputs_sample.ipynb file or can be accessed [here](https://github.com/Hidup-Sehat/Hidup-Sehat-Machine-Learning/blob/main/ObjectDetection/workspace/images_outputs_samples.ipynb).
* Label names is in workspace > annotations > labels.txt file or can be accessed [here](https://github.com/Hidup-Sehat/Hidup-Sehat-Machine-Learning/blob/main/ObjectDetection/workspace/annotations/labels.txt).
* Notebook for Created Metadata can be accessed [here](https://github.com/Hidup-Sehat/Hidup-Sehat-Machine-Learning/blob/main/ObjectDetection/workspace/convert-metadata.ipynb).
* Due to limited storage space on github, our dataset in TFrecord format is stored on Google Drive and can be accessed [here](https://drive.google.com/drive/folders/1HRpsDTKegL_IRKQDTLR39QT8o53vpziV?usp=sharing) (use the third model).
* For the foods dataset can be accessed [here](https://drive.google.com/file/d/1j82Wf6pb5tuNA75JSYEqnln0s2NagPx5/view?usp=sharing).

## How to run the model in Notebook
Here's a step-by-step for running the model in a notebook.

1. clone the github
2. Copy the path of the latest saved_model
3. Import tensorflow and load the model 
    ```python
    import tensorflow as tf
    model = tf.saved_model.load(PATH_TO_SAVED_MODEL)
    ```

## How to train the model using terminal command
Here's a step-by-step command for training the model in the terminal.

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
