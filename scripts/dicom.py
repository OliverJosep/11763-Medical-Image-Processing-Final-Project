import pydicom
import os
import numpy as np


def load_dicom(path_folder: str):
    slices: list[pydicom.Dataset] = []

    sorted_files = sorted(os.listdir(path_folder))
    for file in sorted_files:
        if file.endswith('.dcm'):
            file_path = os.path.join(path_folder, file)
            slices.append(pydicom.dcmread(file_path))

    slices.sort(key=lambda x: int(x.InstanceNumber))
    return slices

def create_3d_array_from_dicom(slices: list[pydicom.Dataset]) -> np.ndarray:
    """ Create a 3D numpy array from DICOM slices. """
    # Asegurar que totes les imatges tenen la mateixa mida
    img_shape = slices[0].pixel_array.shape
    img_3d = np.zeros((len(slices), *img_shape), dtype=np.int16)

    for i, slice in enumerate(slices):
        img_3d[i] = slice.pixel_array

    return img_3d

# Median
def median_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median sagittal plane of the CT image provided. """
    return img_dcm[:, :, img_dcm.shape[2] // 2]

def median_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the median coronal plane of the CT image provided. """
    return img_dcm[:, img_dcm.shape[1] // 2, :]

# Average Intensity Projection (AIP)
def AIP_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the average intensity projection on the sagittal orientation. """
    return np.mean(img_dcm, axis=2)

def AIP_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the average intensity projection on the coronal orientation. """
    return np.mean(img_dcm, axis=1)

# Maximum Intensity Projection (MIP)
def MIP_sagittal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the maximum intensity projection on the sagittal orientation. """
    return np.max(img_dcm, axis=2)

def MIP_coronal_plane(img_dcm: np.ndarray) -> np.ndarray:
    """ Compute the maximum intensity projection on the coronal orientation. """
    return np.max(img_dcm, axis=1)
