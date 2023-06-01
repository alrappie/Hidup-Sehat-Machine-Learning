## tf record

### train tf record
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\photos\new_dataset\ayam\train -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\02_model\train.record

### test tf record
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\google_image_scraper\Google-Image-Scraper\photos\new_dataset\ayam\test -l D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\label_map.pbtxt -o D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\02_model\test.record

## Train model

python model_main_tf2.py --model_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640 --pipeline_config_path=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\02_ssd_mobilenet_v2_fpnlite_640\pipeline.config

## tensorboard
tensorboard --logdir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640

## eval
python model_main_tf2.py --pipeline_config_path=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640\pipeline.config --model_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640 --checkpoint_dir=D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640

## export
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640\pipeline.config --trained_checkpoint_dir D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640 --output_directory D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\01-my_model


## convert tflite
python export_tflite_graph_tf2.py --trained_checkpoint_dir D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640 --output_directory D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\01-my_model_tflite --pipeline_config_path D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\models\01_ssd_mobilenet_v2_fpnlite_640\pipeline.config

python metadata_writer_for_object_detection.py --model_file D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\01-my_model_tflite\model.tflite --label_file D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\annotations\labels.txt --export_directory D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\ObjectDetection\workspace\exported-models\01-my_model_tflite\metadata