## tf record

### train
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\photos\food\train -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\train.record

### test
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\photos\food\test -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\test.record

## Train

python model_main_tf2.py --model_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640 --pipeline_config_path=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640\pipeline.config

## tensorboard
tensorboard --logdir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640

## export
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640\pipeline.config --trained_checkpoint_dir D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640 --output_directory D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\exported-models\01-my_model