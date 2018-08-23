'''
Copyright (C) 2018 Aditia A. Pratama
aditia.ap@gmail.com

Created by Aditia A. Pratama

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
if "bpy" in locals():
    import imp
    imp.reload(c2o_ops)
    imp.reload(c2o_ui)
else:
    from . import c2o_ops
    from . import c20_ui

import bpy
import os
from bpy.props import *

bl_info = {
    "name": "Cycles to Octane Material Converter",
    "description": "Cycles to Octane Material Converter",
    "author": "Aditia A. Pratama",
    "version": (0, 0, 4),
    "blender": (2, 7, 9),
    "location": "",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "" }

class c2oSettings(bpy.types.PropertyGroup):
    mode_options = [
        ('SELECTED', 'Selected Objects Only', '', 1),
        ('ALL','All Objects', '', 2)
    ]
    mode_select = bpy.props.EnumProperty(
        items = mode_options,
        name = 'Select Mode', 
        description = "Change the mode of converting mode",
        default = 'ALL'
    )

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.c2oSettings = bpy.props.PointerProperty(type=c2oSettings)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.c2oSettings

if __name__ == "__main__":
    register()
    