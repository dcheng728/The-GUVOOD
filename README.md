# The-GUVOOD

This repository contains the Grasps Unver Varied Object Orientation (GUVOOD) dataset.

***experimental data*** - Complete set of raw data collected from the experiments

***distribution demo.py*** - Demonstration of creating distribution graphs from this dataset

***scatter demo.py*** - Demonstration of creating scatter plots from this dataset

***transformations_array.npy*** - numpy array file containing recorded wrist transformations during the experiments

***labels_array.npy*** - numpy array file containing manually labeled grasp classification according to the Cutkosky Hand Taxonomy, its order matches with transformation_array.npy

***labels.json*** - dictionary object containing labeled grasp classification



## Organization of the dataset
Inside the "experimental data" folder contains images captured from the grasp experiments. A total of 60 objects are grasped, 28 grasper subjects participated, and each object is grasped 8 times by each subject. During the experiments, the sixty objects are broken down into six groups of ten. The "meta_data.py" file contains information about how these groups are separated. 

For every grasp, three things are being recorded: an image of the grasp, a 3D transformation of the grasp, and whether the grasp succeed. The images of the grasps are saved under the "image/" directory under each subject in "experimental data/", the wrist transformations are registered and saved in batch by group, (i.e experiment data/10-cz/first group.npy will contain all wrist transformations in the second group of objects for this subject in order), the success/failure of a grasp is recorded in the wrist transformation (the failed grasps' transformation is recorded as a 4x4 matrix full of 0s). 

After the experiments are complete and all grasps have been registered. The image of every grasp is manually labeled, and the labeling results are saved in a dictionary object: labels.json. To get the label for subject 10-cz's grasp on apple at the 7th orientation:

```python
import json
#Loading a dictionary containing the labels, keys: [subject][item]
with open('labels.json','r',encoding='utf8')as fp:
    labels = json.load(fp)

subject = "10-cz"
item = "apple"
orientation = 7

print(labels[subject][item+str(orientation)])
```

When analyzing the data, it is frequently needed to separate the left and right data, which the dictionary will not do. Therefore, we have processed the transformation and label data to separate the left and right. 

```python
import numpy as np
#Loading a numpy array containing all the wrist transformations in 4x4 matrices
transformations = np.load("transformations_array.npy")
right_trans = transformations[:10080].copy()
left_trans = transformations[10080:].copy()

#Loading the labels in numpy array format, this contains the same 
#informaiton as the dicitonary loaded from .json, but its order 
#matches that of the transformation array
labels_array = np.load("labels_array.npy")
right_lbls = labels_array[:10080].copy()
left_lbls = labels_array[10080:].copy()
```

## To run the file
1. Clone the repository
2. Run distribution demo.py
3. Run scatter demo.py
