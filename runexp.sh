#!/bin/bash

export xgboost

# map the data to features.
python mapfeat.py
# split train and validation
#python mknfold.py car.txt 1 6
python xzm.py car.txt 1 3
# training and output the models
python runxgb.py
