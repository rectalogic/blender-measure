import bpy
import bpy.props
import bmesh

bl_info = {
    "name": "Measure Selected Edges",
    "description": "Measure the total length of selected edges in a mesh.",
    "author": "Andrew Wason <rectalogic@rectalogic.com>",
    "version": (1, 0),
    "blender": (2, 6, 6),
    "location": "View3D > Properties > Measure Edges",
    "warning": '', # used for warning icon and text in addons panel
    "wiki_url": '',
    "tracker_url": '',
    "category": "3D View"
}

class MeasureEdges(bpy.types.Operator):
    bl_idname = "view3d.measure_edges"
    bl_label = "Measure Edges"
    bl_description = "Measure selected edges"

    def execute(self, context):
        bm = bmesh.from_edit_mesh(bpy.context.active_object.data)
        length = sum(edge.calc_length() for edge in bm.edges if edge.select)
        self.report({'INFO'}, "Edge length %f" % length)
        return {'FINISHED'}


class OBJECT_PT_measure_edges(bpy.types.Panel):
    bl_label = "Measure Edges"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    @classmethod
    def poll(cls, context):
        ob = bpy.context.active_object 
        if context.area.type == 'VIEW_3D' and ob.type == 'MESH' and ob.mode == 'EDIT': 
            return 1
        return 0

    def draw(self, context):
        layout = self.layout

        layout.label(text="Measure Edges")
        col = layout.column(align=True)
        col.operator("view3d.measure_edges", text="Measure")


def register():
    bpy.utils.register_module(__name__)
    pass

def unregister():
    bpy.utils.unregister_module(__name__)
    pass

if __name__ == "__main__":
    register()
