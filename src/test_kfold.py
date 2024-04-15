import os
import sys
from loguru import logger as log
from tqdm import tqdm

log.add('test_10_fold.log')

os.system(f"pyenv local yolov7 ")
for iou_tresh in tqdm([0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]):
    for i in [1,2,3,4,5,6,7,8,9,10]:#
        log.info(f"test GPU: tresh IOU {iou_tresh} in fold {i}...")
        os.system(f" python test.py --data fold_{i}/data.yaml --conf {iou_tresh} --iou 0.65 --device 0,1,2,3 --weights runs/train/yolov7-mieloma_fold_{i}/weights/best.pt --name fold_{i} --verbose --save-txt --single-cls --task test --save-conf > fold_{i}_out_confid_{iou_tresh}.txt")

