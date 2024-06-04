from main import extract_nifti_data, threshold_data, get_mean
import nibabel as nib
import numpy as np
import os


def test_extract_nifti_data(tmpdir): 
    data = np.ones((32, 32, 15, 100), dtype = np.int16)
    img = nib.Nifti1Image(data, np.eye(4))
    path = os.path.join(tmpdir,"test_img.nii.gz")
    nib.save(img, path)

    loaded_data = extract_nifti_data(path) # This is where we call the function to test

    assert np.array_equal(data, loaded_data), "loading incorrect"
    # os.system("rm test_img.nii.gz") # Boring and manual way to eliminate
    #Not very efficient

def test_threshold_data():
    data = np.random.randn(4,4)
    threshold = 0.1
    thresholded_data = threshold_data(data,threshold)

    assert (thresholded_data > threshold).all(), 'thresholding incorrect'
    # This is an array > float. SO we will get an array
    # Thats why why use the (...).all 
    # This will only return true if all values inside the array are True

def test_get_mean():
    data = np.ones((4,4))
    average = get_mean(data)
    #We know for sure that the average should be one

    assert average == 1, 'mean incorrect'

