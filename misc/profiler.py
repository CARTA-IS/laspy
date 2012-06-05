#!/usr/bin/env python
import sys
import cProfile
sys.path.append("../")

from laspy import file as File
inFile = File.File(sys.argv[1],mode= "r")
outFile = File.File(sys.argv[2],mode= "w", header = inFile.header)

spec = inFile.reader.point_format.lookup.keys()

def f():
    outFile.X = inFile.X

cProfile.run("outFile.X = inFile.X")

#for x in spec:
#    print(x)
#    outFile.writer.set_dimension(x, inFile.reader.get_dimension(x))


inFile.close()
outFile.close()
