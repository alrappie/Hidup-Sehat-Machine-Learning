## tf record

### train
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\images\jalanan_luar\train -l D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\annotations\jalanan\label_map.pbtxt -o D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\annotations\jalanan\train.record

### test
python generate_tfrecord.py -x D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\images\jalanan_luar\test -l D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\annotations\jalanan\label_map.pbtxt -o D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\annotations\jalanan\test.record

## Train

python model_main_tf2.py --model_dir=D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\models\my_ssd_mobilenet_v2_fpnlite_640_3 --pipeline_config_path=D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\models\my_ssd_mobilenet_v2_fpnlite_640_3/pipeline.config

## tensorboard
tensorboard --logdir=D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\models\my_ssd_mobilenet_v2_fpnlite_640_2

## export
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\models\my_ssd_mobilenet_v2_fpnlite_640_3\pipeline.config --trained_checkpoint_dir D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\models\my_ssd_mobilenet_v2_fpnlite_640_3 --output_directory D:\Pemrograman\Python\Project\TensorFlow\workspace\training_demo\exported-models\my_model_3