"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    
    intersection = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for j in range(a.shape[2]):
                if (a[i, j, k] == 1 and b[i, j, k] == 1):
                    intersection += 1

    volumes = sum(np.ones(a[a == 1].shape)) + sum(np.ones(b[b == 1].shape))
    
    if volumes == 0:
        return -1

    return 2.*float(intersection) / float(volumes)

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    
    intersection = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for j in range(a.shape[2]):
                if (a[i, j, k] == 1 and b[i, j, k] == 1):
                    intersection += 1

    union = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for j in range(a.shape[2]):
                if (a[i, j, k] == 1 or b[i, j, k] == 1):
                    union += 1
    
    volume = intersection/union
    return volume