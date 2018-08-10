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

def mixmat_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        mix_nodes = [n for n in nodes if n.type == 'MIX_SHADER']
        for n in mix_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y

            shader_oct_mix = nodes.new('ShaderNodeOctMixMat')
            shader_oct_mix.location = n_loc_x, n_loc_y

            n_inputs = n.inputs[1]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket_1 = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_mix.inputs[1],
                    from_socket_1
                )
            n_inputs = n.inputs[2]
            i_links = [i for i in n_inputs.links]
            for i in i_links:
                from_socket_2 = i.from_socket

            if n_inputs.is_linked:
                links.new(
                    shader_oct_mix.inputs[2],
                    from_socket_2
                )

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket
            
            links.new(
                shader_oct_mix.outputs[0],
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
        
def floatimg_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links
        floatimg_nodes = [n for n in nodes if n.type == 'TEX_IMAGE'\
                    and n.color_space == 'NONE']
        for n in floatimg_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y
            n_image= n.image

            shader_oct_floatimg = nodes.new('ShaderNodeOctFloatImageTex')
            shader_oct_floatimg.location = n_loc_x, n_loc_y
            shader_oct_floatimg.image = n_image

            n_outputs = n.outputs
            o_links = [o for o in n_outputs]
            for o in o_links:
                o_links = o.links
                for ol in o_links:
                    to_socket = ol.to_socket
            
            links.new(
                shader_oct_floatimg.outputs[0],
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
            n_loc_y = n.location.y 
            n_color = n.inputs[0].default_value
            
            shader_oct_glossy = nodes.new('ShaderNodeOctGlossyMat')
            shader_oct_glossy.location = n_loc_x, n_loc_y
            shader_oct_glossy.inputs[0].default_value = n_color

            n_inputs = n.inputs
            i_links = [i for i in n_inputs]
            for i in i_links:
                i_links = i.links
                for il in i_links:
                    from_socket = il.from_socket

            if n_inputs[0].is_linked:
                links.new(
                    shader_oct_glossy.inputs[0],
                    from_socket
                )

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


def principled_convert(context):
    materials = [m for m in bpy.data.materials if m.use_nodes]
    for m in materials:
        nodes = m.node_tree.nodes
        links = m.node_tree.links

        principled_nodes = [n for n in nodes if n.type == 'BSDF_PRINCIPLED']
        for n in principled_nodes:
            n_loc_x = n.location.x 
            n_loc_y = n.location.y 
            n_color = n.inputs[0].default_value
            n_specular = n.inputs['Specular'].default_value
            n_roughness = n.inputs['Roughness'].default_value
            n_ior = n.inputs['IOR'].default_value
            
            shader_oct_glossy = nodes.new('ShaderNodeOctGlossyMat')
            shader_oct_glossy.location = n_loc_x, n_loc_y
            shader_oct_glossy.inputs[0].default_value = n_color
            shader_oct_glossy.inputs['Specular'].default_value = n_specular
            shader_oct_glossy.inputs['Roughness'].default_value = n_roughness
            shader_oct_glossy.inputs['Index'].default_value = n_ior

            diff_input = n.inputs['Base Color']
            i_links = [i for i in diff_input.links]
            for i in i_links:
                from_socket_diff = i.from_socket

            if diff_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Diffuse'],
                    from_socket_diff
                )

            spec_input = n.inputs['Specular']
            i_links = [i for i in spec_input.links]
            for i in i_links:
                from_socket_spec = i.from_socket

            if spec_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Specular'],
                    from_socket_spec
                )
            
            rough_input = n.inputs['Roughness']
            i_links = [i for i in rough_input.links]
            for i in i_links:
                from_socket_rough = i.from_socket

            if rough_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Roughness'],
                    from_socket_rough
                )
            
            normal_input = n.inputs['Normal']
            i_links = [i for i in normal_input.links]
            for i in i_links:
                from_socket_normal = i.from_socket

            if normal_input.is_linked:
                links.new(
                    shader_oct_glossy.inputs['Normal'],
                    from_socket_normal
                )

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
        floatimg_convert(self)
        glossy_convert(self)
        principled_convert(self)
        glass_convert(self)
        mixmat_convert(self)

        objects = bpy.data.objects
        obj = [o for o in objects if o.type == 'MESH']
        for o in obj:
            mesh_data = o.data
            for poly in mesh_data.polygons:
                if poly.use_smooth:
                    materials = [mat for mat in mesh_data.materials\
                                if mat.use_nodes]
                    for mat in materials:
                        nodes = mat.node_tree.nodes
                        node_type = [
                                "OCT_GLOSSY_MAT", 
                                "OCT_DIFFUSE_MAT",
                                "OCT_SPECULAR_MAT"]
                        for node in nodes:
                            if node.type in node_type:
                                n_smooth = node.inputs['Smooth']
                                n_smooth.default_value = True


        return {"FINISHED"}


def register():
    from bpy.utils import register_class

    register_class(c2oDiffuseConvert)

def unregister():
    from bpy.utils import unregister_class

    unregister_class(c2oDiffuseConvert)

if __name__ == "__main__":
    register()