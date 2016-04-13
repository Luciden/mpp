import bpy

from bpy.props import StringProperty

from . import fileio

bl_info = {
    'name': 'Motor Protein Placement',
    'author': 'Dennis Merkus',
    'location': 'View3D > UI panel > Add meshes',
    'category': 'User',
}


class MPPReaderOperator(bpy.types.Operator):
    bl_idname = "mpp.read"
    bl_label = "Read .mpp"
    
    file_name = bpy.props.StringProperty(name="File", default=r"C:\Users\Dennis\Google Drive\dev\msc\pattern.mpp")

    def execute(self, context):
        print(fileio.read_mpp(self.file_name))
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class MPPWriterOperator(bpy.types.Operator):
    bl_idname = "mpp.write"
    bl_label = "Write .mpp"
    name = bpy.props.StringProperty()

    def execute(self, context):
        return {'FINISHED'}

        
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

        layout.label("Functions")
        row = layout.row()
        row.alignment = 'CENTER'
        row.operator("mpp.write", text="Add motor protein")

def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()
