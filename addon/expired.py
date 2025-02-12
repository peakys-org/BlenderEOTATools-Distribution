import bpy

class UI_PT_notice(bpy.types.Panel):
    bl_label = ""
    bl_idname = "UI_PT_notice"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "EOTA_Tools"
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="試用版は期限切れです。")
    def draw(self, context):
        layout = self.layout
        layout.label(text="ご利用ありがとうございました。")
        layout.label(text="kato@peakys.jp")

classes=[
    UI_PT_notice,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__=='__main__':
    register()
