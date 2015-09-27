#!/usr/bin/env python
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.datasets.samples_generator import make_blobs

def densityCluster(pts): #[[x1,y1],...]

	#TODO: max distance for clusters?
	db = DBSCAN(min_samples=4,metric="euclidean").fit(pts)
	labels = db.labels_
	

densityCluster(None);

