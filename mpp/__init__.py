import bpy

import math 

from bpy.props import StringProperty

from . import fileio

bl_info = {
    'name': 'Motor Protein Placement',
    'author': 'Dennis Merkus',
    'location': 'View3D > UI panel > Add meshes',
    'category': 'User',
}


def create_protein_at(location):
    bpy.ops.mesh.primitive_uv_sphere_add()
    object = bpy.context.active_object
    object.name = "Motor Protein"
    object.location = location
    mesh = object.data
    mesh.name = "Mesh"
    
    return


def create_proteins_from_list(coordinates):
    for (x, y, z) in coordinates:
        create_protein_at((x, y, z))

    return


def protein_coordinates(scene):
    # Select all motor protein objects
    proteins = [p for p in scene.objects if "Motor Protein" in p.name]
    
    # Get all coordinates
    return [p.location for p in proteins]


class MPPReaderOperator(bpy.types.Operator):
    bl_idname = "mpp.read"
    bl_label = "Read .mpp"
    
    file_name = bpy.props.StringProperty(name="File", default=r"C:\Users\Dennis\Google Drive\dev\msc\pattern.mpp")

    def execute(self, context):
        coordinates = fileio.read_mpp(self.file_name)
        print(coordinates)
        create_proteins_from_list(coordinates)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

        
def write_mpp(name, coordinates):
    with open(name, "w+") as f:
        f.write("version: 0.1\n")
        f.write("size: {:d}\n".format(len(coordinates)))
        for x, y, z in coordinates:
            f.write("h\n")
            f.write("{:f}\n{:f}\n{:f}\n".format(x, y, z))
        
    f.close()


class MPPWriterOperator(bpy.types.Operator):
    bl_idname = "mpp.write"
    bl_label = "Write .mpp"
    
    file_name = bpy.props.StringProperty(name="File", default=r"C:\Users\Dennis\Google Drive\dev\msc\saved.mpp")

    def execute(self, context):
        write_mpp(self.file_name, protein_coordinates(context.scene))
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

        
class MPPManualAdd(bpy.types.Operator):
    bl_idname = "mpp.manual_add"
    bl_label = "Manually add a motor protein"
    
    x = bpy.props.FloatProperty(name="x", default=0.0)
    y = bpy.props.FloatProperty(name="y", default=0.0)
    z = bpy.props.FloatProperty(name="z", default=0.0)
    
    def execute(self, context):
        create_protein_at((self.x, self.y, self.z))
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class MPPCircleGenerator(bpy.types.Operator):
    bl_idname = "mpp.generatorcircle"
    bl_label = "Generate motor proteins in a circle"
    
    x = bpy.props.FloatProperty(name="x", default=0.0)
    y = bpy.props.FloatProperty(name="y", default=0.0)
    z = bpy.props.FloatProperty(name="z", default=0.0)
    
    r = bpy.props.FloatProperty(name="r", default=10.0)
    
    density = bpy.props.IntProperty(name="Density", default=1)
    
    def execute(self, context):
        angle_start = 0.0
        angle_end = 2.0 * math.pi
        
        angles = [angle_start + i * 0.01 * (angle_end - angle_start) for i in range(0, 100, self.density)]
        
        coordinates = [(self.r * math.cos(a), self.r * math.sin(a), self.z)
                       for a in angles]
        
        create_proteins_from_list(coordinates)
        return {'FINISHED'}
            
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        
        
class MPPGridGenerator(bpy.types.Operator):
    bl_idname = "mpp.generatorgrid"
    bl_label = "Layout motor proteins in a grid"
    
    grid_width = bpy.props.IntProperty(name="Grid width", default=5)
    grid_height = bpy.props.IntProperty(name="Grid Height", default=5)
    
    tile_width = bpy.props.FloatProperty(name="Tile width", default=4.0)
    tile_height = bpy.props.FloatProperty(name="Tile height", default=4.0)
    
    z = bpy.props.FloatProperty(name="Z-coordinate", default=0.0)
    
    density = bpy.props.IntProperty(name="Density", default=1)

    def execute(self, context):
        x_min = 0
        x_max = self.grid_width
        y_min = 0
        y_max = self.grid_height
        
        xs = range(x_min, x_max * self.density)
        ys = range(y_min, y_max * self.density)
        
        grid_points = [(x, y) for x in xs for y in ys if x % self.density == 0 or y % self.density == 0]
        coordinates = [(x * self.tile_width, y * self.tile_height, self.z) for x in xs for y in ys]
        
        create_proteins_from_list(coordinates)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class MainPanel(bpy.types.Panel):
    bl_label = "Main panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout

        layout.label("Files")
        row = layout.row()
        row.operator("mpp.read", text="Open .mpp")
        row.operator("mpp.write", text="Save As .mpp")
        
        layout.label("Manual")
        row = layout.row()
        row.operator("mpp.manual_add", text="Manually add a motor protein")

        layout.label("Generators")
        row = layout.row()
        row.alignment = 'CENTER'
        row.operator("mpp.generatorgrid", text="Grid")
        row.operator("mpp.generatorcircle", text="Circle")

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()
