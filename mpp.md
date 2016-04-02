Motor Protein Placement (.mpp) File Format Specification
========================================================

An .mpp file is an ASCII file containing spatial information for the placement
of motor proteins.


Example
-------

    version: 0.1
    size: 2
    h
    1.353023
    3.313535
    0.000000
    t
    2.621235
    2.123455
    0.000000

    
Specification
-------------
    
A motor protein is of a certain type, and has a location.
Currently, there are two types of motor proteins that have to be described:
Head-to-tail and Tail-to-head.
These types are represented by the characters 'h' and 't' respectively.

The motor proteins' locations are described by 3 coordinates - x, y, and z -
in standard ASCII float notation.


# File Structure

An .mpp file consists of two parts: a header with some meta information, and
the body with the data.

The header should consist of the following two lines:

    version: 0.1

A version line, describing which version of the .mpp file format is used.

    size: 10

A size line, describing the integer number of points that are described in the file.

The body consists of all the point data, which is not necessarily ordered in any
way.
Any datapoint consists of 4 lines: 1 to specify the type, 't' or 'h', and 3 to specify the x, y,
and z coordinates respectively.

    h
    1.0
    2.0
    0.0
