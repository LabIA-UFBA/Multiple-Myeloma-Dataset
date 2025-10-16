# Multiple Myeloma Dataset

First and foremost, thanks for your interest in using our dataset with labeled cells design to support the detection of Plasma Cells.

This repository contains images of different cells, including Plasma ones, collected from histological slides of bone marrow aspirate stained with Wright-Giem. Moreover, we also shared a Deep Neural Network trained to help diagnose Multiple Myeloma (MM), a plasma cell oncohematology with the highest incidence, which is more frequent in individuals over 50 years old. According to the International Agency for Research on Cancer of the World Health Organization (WHO), in 2020, MM was responsible for 176,404 new cases and 117,077 deaths of patients of both sexes.

The dataset was created by the following the steps: (a) bone marrow aspirate procedure; (b) Wright-Giemsa stained bone marrow aspirate smear slides from MM patients, analyzed by the oncohematology and immunophenotyping service of the Laboratory of Immunology and Molecular Biology; (c) Observation of stained slides in visible light optical microscopes and image capture by smartphone device; (d) Identification and labeling of detected cells.

<center><img src="figures/fig1.png" width=500px/></center>

The following image shows an example of our dataset. This image contains a set of bounding boxes drawn by specialists used as ground truth in our experiments.

<center><img src="figures/boundingboxes.png" width=500px/></center>

Here you will find all codes, models, and data used in the manuscript “Enhancing Diagnostic Accuracy of Multiple Myeloma through ML-Driven Analysis of Hematological Slides: New dataset and identification model to support hematologists” (Journal, 2024).

The organization of this repository is:

> - **data** - contains images wit labeled cells: https://huggingface.co/datasets/LAB-IA-UFBA/myeloma-dataset
>  - `myeloma_dataset.zip`: all images and labels
>   -  `myeloma_dataset_conf_fold_1.zip`: example of organizing the test fold
>   -  `10_fold.csv`:  splitting of training, testing and validation data into the 10 folds
> - **/src** - contains source codes created to train and assess the DNN model used to identify Plasma cells
> - **/noteboks** - contains Python notebooks used to visualize imagens and reproduce our findings
> - **models** - contains frozen models used to detect plasma cells in our images: https://huggingface.co/LAB-IA-UFBA/myeloma-yolo7-model
> - If you find any issues with the code, please contact us: ricardoar@ufba.br.

On the behalf of all of the authors, we appreciate your interest in our data, code and models, and hope they are useful to your research.

DNN model used: [Yolo v7](https://github.com/WongKinYiu/yolov7/tree/main)

##  📝 Citation

If you find the dataset useful for your research, please consider citing:



```latex
@article{andrade2024enhancing,
  title={Enhancing diagnostic accuracy of multiple myeloma through ML-driven analysis of hematological slides: new dataset and identification model to support hematologists},
  author={Andrade, Caio LB and Ferreira, Marcos V and Alencar, Brenno M and Junior, Ariel MA and Lopes, Tiago JS and Dos Santos, Allan S and Dos Santos, Mariane M and Silva, Maria ICS and Rosa, Izabela MDRP and Filho, Jorge LSB and others},
  journal={Scientific Reports},
  volume={14},
  number={1},
  pages={11176},
  year={2024},
  publisher={Nature Publishing Group UK London}
}
