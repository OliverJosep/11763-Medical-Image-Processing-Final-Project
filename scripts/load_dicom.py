import pydicom
import os

def load_dicom(path_folder: str):
    slices: list[pydicom.Dataset] = []

    sorted_files = sorted(os.listdir(path_folder))
    for file in sorted_files:
        if file.endswith('.dcm'):
            file_path = os.path.join(path_folder, file)
            slices.append(pydicom.dcmread(file_path))

    slices.sort(key=lambda x: int(x.InstanceNumber))
    return slices
