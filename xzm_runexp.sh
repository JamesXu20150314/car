#!/bin/bash

export xgboost

python xzm_features_sampling.py
# map the data to features.
python xzm_mapfeat.py
# split train and validation
#python mknfold.py car.txt 1 6
python xzm.py car.txt 1 3
# training and output the models
python xzm_runxgb.py

