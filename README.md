# DL-NM-Att-SC-Correction
## This repository offers versatile deep learning based attenuation and scatter correction solution in nuclear medicine modalities including PET and SPECT.
diferent tracers are convered here. 
the inference instruction is presented at [example.py](https://github.com/YazdanSalimi/DL-NM-Att-SC-Correction/blob/main/example.py) , you need to download the trained model for each task and convert your emission images to NIFTI before running the models.) soon. The PET images should be in weight based SUV unit. the instruction for converting Dicom to NIFTI and SUV PET conversion will be updated [here](https://github.com/YazdanSalimi/medical-image-processing-tools).
Multiple tasks for SPECT and PET CT less ateenuation and scatter corerction is available.
Please give the path to the "model directory" on your machine where you saved the trained models downloaded for each specific task. 
## Available models
[PET joint attenuation and scatter correction for 18FDG](link)

To install this repository, simply run:
```bash
pip install git+https://github.com/YazdanSalimi/DL-NM-Att-SC-Correction.git
```
We welcome any feedback, suggestions, or contributions to improve this project!

for any furtehr question please email me at: salimiyazdan@gmail.com

