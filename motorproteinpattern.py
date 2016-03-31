#!/usr/bin/python
OUTFILE = "pattern.txt"

outputFile = open(OUTFILE, "wb")


def writeCoordinate(c):
    outputFile.write(str(c))
    outputFile.write('\n')

    
def writeCoordinates(x, y, z):
    writeCoordinate(x)
    writeCoordinate(y)
    writeCoordinate(z)


if __name__ == "__main__":
    writeCoordinates(1.0, 2.0, 3.0)
