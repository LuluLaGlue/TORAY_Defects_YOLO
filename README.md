# YOLO algorithm for defect monitoring

This folder contains the YOLO algorithm used for defect monitoring.
Run <code>pip install -U -r algo/requirements.txt</code> ton install dependencies

# Dataset
Use <url>https://blog.roboflow.com/cvat/</url> to annotate your data and <url>https://roboflow.com/</code> to create a dataset.
### Roboflow
When you download your dataset from roboflow please use YOLOv5 PyTorch format.

# Train

To create a new model run <code>python ./algo/train.py --img img_size --batch batch_size --epochs epochs_number --data path/to/data.yaml</code>

# Detection

To use the previsouly trained model run <code>python detect.py --weights path/to/best/weights --img img_size --conf confidence_threshold --source img_source --save-crop</code> <br />

The weights created in training mode can be found in <code>./algo/runs/train/exp/weights</code>. The result are located in <code>./algo/runs/detect/expRunNbr/</code>