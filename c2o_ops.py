import bpy
import os

class c2oDiffuseConvert(bpy.types.Operator):
    bl_idname = "c2oconvert.diffuse"
    bl_label = "C2O Convert Diffuse"
    bl_description = "C2O Convert Diffuse Shader"
    bl_options = {"REGISTER"}


    def execute(self, context):
        objects = bpy.data.objects
        scenes = bpy.data.scenes
        scenes[0].render.engine = 'octane'
        materials = [m for m in bpy.data.materials if m.use_nodes]
        for m in materials:
            nodes = m.node_tree.nodes
            links = m.node_tree.links
            diff_nodes = [n for n in nodes if n.type == 'BSDF_DIFFUSE']
            for n in diff_nodes:
                n_loc_x = n.location.x - 250
                n_loc_y = n.location.y
                n_color = n.inputs[0].default_value
                n_outputs = [o for o in n.outputs]
                for o in n_outputs:
                    n_links = [l for l in o.links]
                    for l in n_links:
                        n_socket = l.to_socket
                #n_link = n.outputs[0].links[0].to_socket
                shader_oct_diff = nodes.new('ShaderNodeOctDiffuseMat')
                shader_oct_diff.location = n_loc_x, n_loc_y
                shader_oct_diff.inputs[0].default_value = n_color
                links.new(
                    shader_oct_diff.outputs[0],
                    n_socket
                    )
                nodes.remove(n)

        return {"FINISHED"}


def register():
    from bpy.utils import register_class

    register_class(c2oDiffuseConvert)

def unregister():
    from bpy.utils import unregister_class

    unregister_class(c2oDiffuseConvert)

if __name__ == "__main__":
    register()