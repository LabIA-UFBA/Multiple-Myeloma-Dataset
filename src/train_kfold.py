
import os
import sys
from loguru import logger as log
from tqdm import tqdm

log.add('train_10_fold.log')

os.system(f"pyenv local yolov7 ")

for i in tqdm([1,2,3,4,5,6,7]):#8, 9, 10
    log.info(f"train GPU in fold {i}...")
    os.system(f" python train.py --workers 8 --device 0,1,2,3 --batch-size 32 --data fold_{i}/data.yaml --cfg cfg/training/yolov7x.yaml --weights 'transfer/yolov7x_training.pt' --name yolov7-mieloma_fold_{i} --hyp data/hyp.scratch.custom.yaml --hyp data/hyp.scratch.custom.yaml --single-cls ")
