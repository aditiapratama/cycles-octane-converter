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
        col = box.column(align=True)
        col.operator(
            "c2oconvert.diffuse",
            text="Convert",
            icon="ALIGN"
        )


def register():
    from bpy.utils import register_class

    register_class(c2oPanel)

def unregister():
    from bpy.utils import unregister_class

    unregister_class(c2oPanel)

if __name__ == "__main__":
    register()