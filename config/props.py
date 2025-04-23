import bpy
from bpy.props import FloatProperty, IntProperty
from .main_config import MainConfig


class CatterProperties_ImportModel_General(bpy.types.PropertyGroup):
    # ------------------------------------------------------------------------------------------------------------
    path: bpy.props.StringProperty(
        name="DBMT.exe Location",
        description="插件需要先选择DBMT-GUI.exe的所在路径才能正常工作",
        default=MainConfig.load_dbmt_path(),
        subtype='DIR_PATH'
    ) # type: ignore

    use_specified_dbmt :bpy.props.BoolProperty(
        name="使用指定的DBMT路径",
        description="Use specified DBMT path to work for specified DBMT instead of current opening DBMT",
        default=False
    ) # type: ignore

    model_scale: FloatProperty(
        name="模型导入大小比例",
        description="默认为1.0",
        default=1.0,
    ) # type: ignore

    import_flip_scale_x :bpy.props.BoolProperty(
        name="设置Scale的X分量为-1避免模型镜像",
        description="勾选后在导入模型时把缩放的X分量乘以-1，实现镜像效果，还原游戏中原本的样子，解决导入后镜像对调的问题",
        default=False
    ) # type: ignore

    import_flip_scale_y :bpy.props.BoolProperty(
        name="设置Scale的Y分量为-1来改变模型朝向",
        description="勾选后在导入模型时把缩放的Y分量乘以-1，实现改变朝向效果，主要用于方便后续绑MMD骨",
        default=False
    ) # type: ignore


class CatterProperties_ImportModel_Unreal(bpy.types.PropertyGroup):
    import_merged_vgmap:bpy.props.BoolProperty(
        name="使用融合统一顶点组",
        description="导入时是否导入融合后的顶点组 (Unreal的合并顶点组技术会用到)，一般鸣潮Mod需要勾选来降低制作Mod的复杂度",
        default=False
    ) # type: ignore


class CatterProperties_GenerateMod_General(bpy.types.PropertyGroup):
    export_same_number: bpy.props.BoolProperty(
        name="使用共享TANGENT避免增加顶点数",
        description="使用共享的TANGENT值从而避免hashable计算导致的顶点数增加 (在Unity-CPU-PreSkinning技术中常用，GF2常用，避免顶点数变多导致无法和原本模型顶点数对应)",
        default=False
    ) # type: ignore

    forbid_auto_texture_ini: bpy.props.BoolProperty(
        name="禁止自动贴图流程",
        description="生成Mod时禁止生成贴图相关ini部分",
        default=False
    ) # type: ignore

    recalculate_tangent: bpy.props.BoolProperty(
        name="向量归一化法线存入TANGENT(全局)",
        description="使用向量相加归一化重计算所有模型的TANGENT值，勾选此项后无法精细控制具体某个模型是否计算，是偷懒选项,在不勾选时默认使用右键菜单中标记的选项。\n" \
        "用途:\n" \
        "1.一般用于修复GI角色,HI3 1.0角色,HSR角色轮廓线。\n" \
        "2.用于修复模型由于TANGENT不正确导致的黑色色块儿问题，比如HSR的薄裙子可能会出现此问题。",
        default=False
    ) # type: ignore

    recalculate_color: bpy.props.BoolProperty(
        name="算术平均归一化法线存入COLOR(全局)",
        description="使用算术平均归一化重计算所有模型的COLOR值，勾选此项后无法精细控制具体某个模型是否计算，是偷懒选项,在不勾选时默认使用右键菜单中标记的选项，仅用于HI3 2.0角色修复轮廓线",
        default=False
    ) # type: ignore

    position_override_filter_draw_type :bpy.props.BoolProperty(
        name="Position替换添加DRAW_TYPE = 1判断",
        description="在NPC与VAT-PreSKinning的NPC冲突时会用到此技术，例如HSR匹诺康尼NPC\n格式：\nif DRAW_TYPE == 1\n  ........\nendif",
        default=False
    ) # type: ignore

    vertex_limit_raise_add_filter_index:bpy.props.BoolProperty(
        name="VertexLimitRaise添加filter_index过滤器",
        description="在NPC与VAT-PreSKinning的NPC冲突时会用到此技术，例如HSR匹诺康尼NPC\n格式:\nfilter_index = 3000\n\n....\n\nif vb0 == 3000\n  ........\nendif",
        default=False
    ) # type: ignore


    slot_style_texture_add_filter_index:bpy.props.BoolProperty(
        name="槽位风格贴图添加filter_index过滤器",
        description="可解决HSR知更鸟多层渲染问题，可解决ZZZ NPC贴图俯视仰视槽位不一致问题（生成的只是模板，仍需手动添加或更改槽位以适配具体情况）",
        default=False
    ) # type: ignore



    only_use_marked_texture:bpy.props.BoolProperty(
        name="只使用标记过的贴图",
        description="勾选后不会再生成Hash风格的RenderTextures里的自动贴图，而是完全使用用户标记过的贴图，如果用户遗漏了标记，则不会生成对应没标记过的贴图的ini内容",
        default=False
    ) # type: ignore
    
