import os
import pandas as pd
import random

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import yaml
from PIL import Image, ImageDraw, ImageFont
from scipy.signal import butter, filtfilt


def xywhn2xyxy(x, w=640, h=640, padw=0, padh=0):
    # Convert nx4 boxes from [x, y, w, h] normalized to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
    y = np.copy(x)
    y[:, 0] = w * (x[:, 0] - x[:, 2] / 2) + padw  # top left x
    y[:, 1] = h * (x[:, 1] - x[:, 3] / 2) + padh  # top left y
    y[:, 2] = w * (x[:, 0] + x[:, 2] / 2) + padw  # bottom right x
    y[:, 3] = h * (x[:, 1] + x[:, 3] / 2) + padh  # bottom right y
    return y


def get_bbox_to_txt(fpath, classe=1):
    df = pd.read_csv(fpath, header=None)
    array = df.to_numpy()
    array_conver = [str(a[0]).split(' ')[classe:] for a in array]
    return np.array(array_conver, dtype='float32')

def plot_one_box(x, img, color=None, label=None, line_thickness=10):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def set_bbox(imname, path_images, path_pred, path_targ, out='predictions/'):
    
    obj = imname.split('.')[0] 
    
    image = cv2.imread(f"{path_images}{imname}")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (640, 640))
    
    
    mark_esp  = get_bbox_to_txt(f"{path_targ}{obj}.txt")
    
    c_esp = [0, 153, 51]
    c_det = [255, 51, 0]
    
    mark_esp = xywhn2xyxy(mark_esp, w=image.shape[0], h=image.shape[1])
    
    
    for bbox in mark_esp:
        plot_one_box(bbox, image, color=c_esp, line_thickness=1)
    # plot all yolo 
    try:
        mark_pred = get_bbox_to_txt(f"{path_pred}{obj}.txt")
        mark_pred_f = xywhn2xyxy(mark_pred[:,:4], w=image.shape[0], h=image.shape[1])
        labels = mark_pred[:,-1]
        for i, bbox in enumerate(mark_pred_f):
            plot_one_box(bbox, image, color=c_det, label=f"{labels[i]:.2f}", line_thickness=1)
    except:
        print(f"Image without detections: {obj}")
    # write image    
    cv2.imwrite(f'{out}{imname}', image)
    
def export_one_image(fold = 2, out='predictions/'):
    path_targ   = f'/home/marcos/data/10_fold/fold_{fold}/test/labels/'
    path_pred   = f'runs/test/fold_{fold}/labels/'
    path_images = f'/home/marcos/data/10_fold/fold_{fold}/test/images/'
    
    images = os.listdir(path_images)
    
    for image in images:
        set_bbox(image, path_images, path_pred, path_targ, out)    
        
if __name__ == '__main__':
    for fold in [1,2,3,4,5,6,7,8,9,10]:
        print("-" * 30)
        print(f"Process fold {fold}....")
        export_one_image(fold, f"preds/fold_{fold}/")
        print("-" * 30)