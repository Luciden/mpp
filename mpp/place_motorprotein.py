import bpy


def place_motorprotein(x, y, z):
    bpy.ops.mesh.primitive_sphere_add(location=(x, y, z))
    return bpy.context.object


if __name__ == '__main__':
    ob = place_motorprotein(0, 0, 0)
