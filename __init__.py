from .ui.panel_ui import * 
from .ui.collection_rightclick_ui import *
from .ui.obj_rightclick_ui import *

from .config.catter_properties import *
from .import_model.migoto_import import *
from .generate_mod.m_export_mod import *


'''
Catter is compatible with all version start from Blender 3.6 LTS To 4.2LTS To Latest version.
To do this, we need keep track Blender's changelog:

4.1 to 4.2
https://docs.blender.org/api/4.2/change_log.html#to-4-2
4.0 to 4.1
https://docs.blender.org/api/4.1/change_log.html
3.6 to 4.0 
https://docs.blender.org/api/4.0/change_log.html#change-log

https://www.blender.org/support/
https://docs.blender.org/api/3.6/
https://docs.blender.org/api/4.2/

Dev:
https://github.com/JacquesLucke/blender_vscode
https://github.com/BlackStartx/PyCharm-Blender-Plugin


'''

# XXX Blender插件开发中的缓存问题：
# 在使用VSCode进行Blender插件开发中，会创建一个指向项目的软连接，路径大概如下：
# C:\Users\Administrator\AppData\Roaming\Blender Foundation\Blender\4.2\scripts\addons
# 在插件架构发生大幅度变更时可能导致无法启动Blender，此时需要手动删掉插件缓存的这个软链接。
# XXX 所有的文件夹都必须小写，因为git无法追踪文件夹名称大小写改变的记录

bl_info = {
    "name": "Catter",
    "description": "A simple blender plugin for generate 3Dmigoto mod.",
    "blender": (3, 6, 0),
    "version": (1, 0, 0),
    "location": "View3D",
    "category": "Generic",
    "tracker_url":"https://github.com/StarBobis/Catter"
}


register_classes = (
    # 全局配置
    CatterProperties_ImportModel_General,
    CatterProperties_ImportModel_Unreal,
    CatterProperties_GenerateMod_General,

    # DBMT所在位置
    OBJECT_OT_select_dbmt_folder,

    # 导入3Dmigoto模型功能
    Import3DMigotoRaw,
    DBMTImportAllFromCurrentWorkSpace,
    # 生成Mod功能
    ExportModHonkaiStarRail32,
    DBMTExportUnityVSModToWorkSpaceSeperated,
    DBMTExportUnityCSModToWorkSpaceSeperated,
    DBMTExportUnrealVSModToWorkSpace,
    DBMTExportUnrealCSModToWorkSpace,

    # 右键菜单栏
    RemoveAllVertexGroupOperator,
    RemoveUnusedVertexGroupOperator,
    MergeVertexGroupsWithSameNumber,
    FillVertexGroupGaps,
    AddBoneFromVertexGroupV2,
    RemoveNotNumberVertexGroup,
    MMTDeleteLoose,
    MMTResetRotation,
    CatterRightClickMenu,
    SplitMeshByCommonVertexGroup,
    RecalculateTANGENTWithVectorNormalizedNormal,
    RecalculateCOLORWithVectorNormalizedNormal,
    WWMI_ApplyModifierForObjectWithShapeKeysOperator,
    SmoothNormalSaveToUV,
    
    # 集合的右键菜单栏
    Catter_MarkCollection_Switch,
    Catter_MarkCollection_Toggle,

    # UI
    MigotoAttributePanel,
    PanelModelImportConfig,
    PanelGenerateModConfig,
    PanelButtons
    
)

def register():
    for cls in register_classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.dbmt = bpy.props.PointerProperty(type=CatterProperties_ImportModel_General)
    bpy.types.Scene.dbmt_import_config_unreal = bpy.props.PointerProperty(type=CatterProperties_ImportModel_Unreal)
    bpy.types.Scene.dbmt_generatemod = bpy.props.PointerProperty(type=CatterProperties_GenerateMod_General)

    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func_migoto_right_click)
    bpy.types.OUTLINER_MT_collection.append(menu_dbmt_mark_collection_switch)

def unregister():
    for cls in reversed(register_classes):
        bpy.utils.unregister_class(cls)

    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func_migoto_right_click)
    bpy.types.OUTLINER_MT_collection.remove(menu_dbmt_mark_collection_switch)

if __name__ == "__main__":
    register()