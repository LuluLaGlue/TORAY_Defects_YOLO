# YOLO algorithm for defect monitoring

This folder contains the YOLO algorithm used for defect monitoring.
Run <code>pip install -U -r algo/requirements.txt</code> ton install dependencies

# Dataset
Use <url>https://blog.roboflow.com/cvat/</url> to annotate your data and <url>https://roboflow.com/</code> to create a dataset.
### Roboflow
When you download your dataset from roboflow please use YOLOv5 PyTorch format.

# Train

To create a new model run <code>python ./algo/train.py --img img_size --batch batch_size --epochs epochs_number --data path/to/data.yaml --workers nbr_workers</code>

# Detection

To use the previsouly trained model run <code>python detect.py --weights path/to/best/weights --img img_size --conf confidence_threshold --source img_source --save-crop --exist-ok</code> <br />

The weights created in training mode can be found in <code>./algo/runs/train/exp/weights</code>. The result are located in <code>./map-defects/</code>

# Exemple

There is a pretrained model in <code>algo/runs/train/exp</code>, that we trained using a mask detection dataset. To run it: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- install <code>motion</code> with <code>sudo apt-get install motion</code> <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <code>mkdir ~/.motion</code> <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <code>nano ~/.motion/motion.conf</code> <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- add the following lines: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- webcam_port 8081 <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- webcam_localhost off <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- in a new terminal run <code>motion</code> and leave it open <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- cd into <code>algo</code> <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- run <code>python detect.py --weights ./runs/train/exp/weights/best.pt --img 416 --conf 0.7 --source http://localhost:8081 --save-crop --exist-ok</code>
