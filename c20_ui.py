import bpy
from bpy.types import Menu, Panel
from bpy import context

class c2oPanel(bpy.types.Panel):
    bl_idname = "c2opanel"
    bl_label = "Cycles to Octane"
    bl_category = "C2O"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        c2oSettings = bpy.context.scene.c2oSettings
        col = box.column(align=True)
        col.prop(
            c2oSettings,
            "mode_select",
            text = ''
        )
        col.operator(
            "c2oconvert.all",
            text="Convert",
            icon="ALIGN"
        )
