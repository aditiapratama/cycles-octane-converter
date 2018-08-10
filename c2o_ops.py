import bpy
import os


def diffuse_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        diff_nodes = [n for n in nodes if n.type == 'BSDF_DIFFUSE']
        for n in diff_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y
            n_color = n.inputs[0].default_value

            shader_oct_diff = nodes.new('ShaderNodeOctDiffuseMat')
            shader_oct_diff.location = n_loc_x, n_loc_y
            shader_oct_diff.inputs[0].default_value = n_color

            n_inputs = n.inputs
            i_links = [i for i in n_inputs]
            for i in i_links:
                i_links = i.links
                for il in i_links:
                    from_socket = il.from_socket

            if n_inputs[0].is_linked:
                links.new(
                    shader_oct_diff.inputs[0],
                    from_socket
                )

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket
            
            links.new(
                shader_oct_diff.outputs[0],
                to_socket
                )
            nodes.remove(n)

def image_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        img_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
        for n in img_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y
            n_image= n.image

            shader_oct_img = nodes.new('ShaderNodeOctImageTex')
            shader_oct_img.location = n_loc_x, n_loc_y
            shader_oct_img.image = n_image

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket
            
            links.new(
                shader_oct_img.outputs[0],
                to_socket
                )
            nodes.remove(n)


def glossy_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        glossy_nodes = [n for n in nodes if n.type == 'BSDF_GLOSSY']
        for n in glossy_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y - 225
            n_color = n.inputs[0].default_value
            
            shader_oct_glossy = nodes.new('ShaderNodeOctGlossyMat')
            shader_oct_glossy.location = n_loc_x, n_loc_y
            shader_oct_glossy.inputs[0].default_value = n_color

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket

            links.new(
                shader_oct_glossy.outputs[0],
                to_socket
            )
            nodes.remove(n)


def glass_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        glossy_nodes = [n for n in nodes if n.type == 'BSDF_GLASS']
        for n in glossy_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y - 225
            n_color = n.inputs[0].default_value
           
            shader_oct_glass = nodes.new('ShaderNodeOctSpecularMat')
            shader_oct_glass.location = n_loc_x, n_loc_y
            shader_oct_glass.inputs[1].default_value = n_color

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket

            links.new(
                shader_oct_glass.outputs[0],
                to_socket
            )
            nodes.remove(n)

class c2oDiffuseConvert(bpy.types.Operator):
    bl_idname = "c2oconvert.diffuse"
    bl_label = "C2O Convert Diffuse"
    bl_description = "C2O Convert Diffuse Shader"
    bl_options = {"REGISTER"}


    def execute(self, context):
        scenes = bpy.data.scenes
        scenes[0].render.engine = 'octane'
        diffuse_convert(self)
        image_convert(self)
        glossy_convert(self)
        glass_convert(self)

        return {"FINISHED"}


def register():
    from bpy.utils import register_class

    register_class(c2oDiffuseConvert)

def unregister():
    from bpy.utils import unregister_class

    unregister_class(c2oDiffuseConvert)

if __name__ == "__main__":
    register()