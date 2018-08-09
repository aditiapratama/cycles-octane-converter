import bpy
from . import c2o_ops
from . import c20_ui

bl_info = {
    "name": "Cycles to Octane Material Converter",
    "description": "Cycles to Octane Material Converter",
    "author": "Aditia A. Pratama",
    "version": (0, 0, 1),
    "blender": (2, 7, 9),
    "location": "",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "" }

def register():
    c2o_ops.register()
    c20_ui.register()

def unregister():
    c2o_ops.unregister()
    c20_ui.unregister()

if __name__ == "__main__":
    register()
    