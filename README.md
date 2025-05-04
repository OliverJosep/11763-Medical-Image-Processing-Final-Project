# Medical Image Processing Final Project

This project focuses on DICOM data loading, CT volume visualisation, liver tumour segmentation, and projection-based animations with ground truth and predicted masks.

## 📁 Project Structure

```ssh
data/1685/
├── 10_AP_Ax2.50mm/                          # DICOM CT volume
├── 40_RTRD_Ax2.50mm/                        # Secondary DICOM volume (optional)
├── 10_AP_Ax2.50mm_ManualROI_Liver/         # Liver segmentation (RTSTRUCT)
├── 10_AP_Ax2.50mm_ManualROI_Tumor/         # Tumour segmentation (RTSTRUCT)
notebook/
├── Objective1.ipynb                         # Main notebook with loading, segmentation, visualisation
scripts/
├── Objective1.ipynb                         # (Duplicate) Optional script format
outputs/
├── projection/                              # MIP + GIF with ground truth masks
│   ├── Animation.gif
│   ├── Projection_1.png
│   └── …
├── projection_prediction/                   # MIP + GIF with predicted masks
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
