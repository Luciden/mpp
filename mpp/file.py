

def read_header(data):
    if len(data) == 0:
        raise Exception("No header in the MPP file.")

    metadata = {}

    while len(data) > 0:
        line = data[0].split(": ")
        
        line_is_metadata = len(line) == 2 and line[0] in ["version", "size"]

        if line_is_metadata:
            field, value = line[0], line[1]

            if field == "version":
                metadata[field] = str(value).strip()
            elif field == "size":
                metadata[field] = int(value)

            data = data[1:]
        else:
            if "version" not in metadata:
                raise Exception("Header is missing version number.")
            elif "size" not in metadata:
                raise Exception("Header is missing size.")
            else:
                return metadata, data


def read_body(data):
    coordinates = []

    while len(data) > 0:
        x, y, z = float(data[1]), float(data[2]), float(data[3])
        coordinates.append((x, y, z))

        data = data[4:]

    return coordinates


def read_mpp(name="pattern.mpp"):
    with open(name) as f:
        data = f.readlines()

    meta, data = read_header(data)

    print meta
    print "XXXX"
    print data

    if len(data) % 4 != 0:
        raise Exception("Not the correct data format (4 lines per point).")
    elif len(data) != 4 * meta["size"]:
        raise Exception("Not the correct number of data points.")

    return read_body(data)


if __name__ == '__main__':
    print read_mpp("pattern.mpp")
