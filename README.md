
# license plate recognition

  
  

reading license plates numbers using ai

  

## Table of Contents

  

- [approach](#approach)

- [repository overview](#repositoroverview)



  

## Approach

we chose to combine two models, an object detection model (yolov8) and an ocr model (easyocr)

the image is given to the object detection model that will detect only the licence and then crop it and send it to the ocr model to read it

we didn't have labels to train the object detection model so we created them using the labelimg tool

## Overview:

this repo contains 4 folders and a .ipynb file ,
1.to train the yolov8 model search trainingyolov8.ipynb inside the "trainyolov8customdataset" folder the .ipynb file is well commented an will guide you through the training 
<br />

2.to train the easyocr model search for training_easyocr.ipynb in the "deep_text_recognition" folder  the .ipynb file is well commented an will guide you through the training 
<br />

3.to use the final trained model (wich is a combination between yolo and easyocr ) just open the final_model.ipynb file in the main directory the file  is well commented an will guide you through setting up, the model  ```
<br />

4.the predictions format  folder contains  log_demo_result.csv file containing img_id and the predicted labels by the final model it also contain a format_to_submission_format.py file that transformes the log_demo_result.csv.csv file to the format required for the rim-ai-competition submission 
