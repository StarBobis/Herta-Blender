import bpy

# Simple Class to get attributes.
# easy to use, safe to modifiy.
class GenerateModConfig:
    
    @classmethod
    def forbid_auto_texture_ini(cls):
        '''
        bpy.context.scene.dbmt_generatemod.forbid_auto_texture_ini
        '''
        return bpy.context.scene.dbmt_generatemod.forbid_auto_texture_ini

    
    @classmethod
    def author_name(cls):
        '''
        bpy.context.scene.dbmt_generatemod.credit_info_author_name
        '''
        return bpy.context.scene.dbmt_generatemod.credit_info_author_name
    
    @classmethod
    def author_link(cls):
        '''
        bpy.context.scene.dbmt_generatemod.credit_info_author_social_link
        '''
        return bpy.context.scene.dbmt_generatemod.credit_info_author_social_link
    
    @classmethod
    def export_same_number(cls):
        '''
        bpy.context.scene.dbmt_generatemod.export_same_number
        '''
        return bpy.context.scene.dbmt_generatemod.export_same_number
    
    @classmethod
    def recalculate_tangent(cls):
        '''
        bpy.context.scene.dbmt_generatemod.recalculate_tangent
        '''
        return bpy.context.scene.dbmt_generatemod.recalculate_tangent
    
    @classmethod
    def recalculate_color(cls):
        '''
        bpy.context.scene.dbmt_generatemod.recalculate_color
        '''
        return bpy.context.scene.dbmt_generatemod.recalculate_color
    

    @classmethod
    def position_override_filter_draw_type(cls):
        '''
        bpy.context.scene.dbmt_generatemod.position_override_filter_draw_type
        '''
        return bpy.context.scene.dbmt_generatemod.position_override_filter_draw_type
    
    @classmethod
    def vertex_limit_raise_add_filter_index(cls):
        '''
        bpy.context.scene.dbmt_generatemod.vertex_limit_raise_add_filter_index
        '''
        return bpy.context.scene.dbmt_generatemod.vertex_limit_raise_add_filter_index

    @classmethod
    def slot_style_texture_add_filter_index(cls):
        '''
        bpy.context.scene.dbmt_generatemod.slot_style_texture_add_filter_index
        '''
        return bpy.context.scene.dbmt_generatemod.slot_style_texture_add_filter_index
    
    # only_use_marked_texture
    @classmethod
    def only_use_marked_texture(cls):
        '''
        bpy.context.scene.dbmt_generatemod.only_use_marked_texture
        '''
        return bpy.context.scene.dbmt_generatemod.only_use_marked_texture
    
    