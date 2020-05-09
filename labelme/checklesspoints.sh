#!/bin/sh

# parameter 1 should be the root directory of json files like ~/video/t1/*.json


for f in $1/*.json;
do
    python getlesspointsshape.py -i $f
done


