# license plate recognition 


reading license plates numbers using ai  

## Table of Contents

- [approach](#approach)
- [repository overview](#repositoroverview)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact Information](#contact-information)

## Approach
we chose to combine two models, an object detection model (yolov8) and an ocr model (easyocr)
the image is given to the object detection model that will detect only the licence and then crop it and send it to the ocr model to read it 
we didn't have labels to train the object detection model so we created them using the labelimg tool 
## Overview:
this repo contains 3 folders and a ipynb file , one directory contains the training for  yolov8  ,the other contains the training for easyocr ,the third folder contains the final trained weights for both models
and the ipynb file contains the the final model wich is the combination of both models 
to make  predictions run the ipynb file 
to retrain one of the models search for the .ipynb file in its folder it should be well commented and will guide through the training 

