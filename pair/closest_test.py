#!/usr/bin/python3
import unittest
from closest import get_distance

print("{:f}".format(get_distance((0,0),(5,12))))
-> Should be 13
print("{:f}".format(get_distance((1,1),(4,4))))
print("{:f}".format(get_distance((-1,1),(4,-4))))
