import SimpleITK as sitk
import sys, os


def read_dicom_series(filename):
    if len(filename) < 3:
        print("Usage: DicomSeriesReader <input_directory> <output_file>")
        sys.exit(1)

    print("Reading Dicom directory:", filename)
    reader = sitk.ImageSeriesReader()

    dicom_names = reader.GetGDCMSeriesFileNames(filename)
    reader.SetFileNames(dicom_names)

    image = reader.Execute()

    size = image.GetSize()

    return image, size