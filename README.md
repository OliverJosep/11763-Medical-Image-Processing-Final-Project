# Medical Image Processing Final Project

This project focuses on DICOM data loading, CT volume visualisation, liver tumour segmentation, and projection-based animations with ground truth and predicted masks.

## 📁 Project Structure

```ssh
data/1685/
├── {dicom1}x2.50mm/
├── {dicom2}_Ax2.50mm/
├── {dicom1}x2.50mm_ManualROI_Liver/
├── {dicom1}x2.50mm_ManualROI_Tumor/
notebook/
├── Objective1.ipynb
├── Objective2.ipynb                         
scripts/
├── dicom.py
outputs/
├── projection/
│   ├── Animation.gif
│   ├── Projection_1.png
│   └── …
├── projection_prediction/
│   ├── Animation.gif
│   ├── Projection_1.png
│   └── …
requirments.txt
```

## 🧠 Functionality

In the `notebook/` directory, you can find two different Jupyter notebooks, one for each objective. By executing these notebooks, you will obtain all the results corresponding to both objectives.

## 🔧 Requirements

All Python dependencies are listed in the `requirements.txt` file. To install them, simply run:

```bash
pip install -r requirements.txt
```
