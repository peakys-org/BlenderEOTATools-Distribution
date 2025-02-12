bl_info = {
  "name": "EOTA Tools",
  "description": "Create BG Layout tool ",
  "author": "加藤宏怜 (@hirosato654), EOTA, Peakys",
  "version": (1, 0, 2),
  "blender": (4, 3, 0),
  "location": "VIEW3D > Panel",
  "warning": "",
  "doc_url": "https://github.com/peakys-org/BlenderEOTATools-Distribution/blob/main/README.md",
  "tracker_url":"",
  "support": "COMMUNITY",
  "category": "3D View",
}

def check_expired():
    from datetime import datetime, timedelta, timezone
    tokyo_offset = timezone(timedelta(hours=9))
    tokyo_now = datetime.now(tokyo_offset)
    current_date = tokyo_now.date()
    expired_date = datetime(2026, 4, 2).date()
    return bool(current_date < expired_date)


if check_expired():
    Modules=['operate_operators','operate_interface','camera_list','resolution','overarea','composite','camera','output','bake','manual',]
else:
    Modules=['expired']

# Referencing the following URL:
# https://b3d.interplanety.org/en/creating-multifile-add-on-for-blender

import sys
import importlib

ModuleNames={}
for m in Modules:
    ModuleNames[m]='{}.{}'.format(__name__,m)

for m in ModuleNames.values():
    if m in sys.modules:
        importlib.reload(sys.modules[m])
    else:
        globals()[m] = importlib.import_module(m)
        setattr(globals()[m], 'Modules', ModuleNames)

def register():
    for m in ModuleNames.values():
        if m in sys.modules:
            if hasattr(sys.modules[m], 'register'):
                sys.modules[m].register()

def unregister():
    for m in reversed(ModuleNames.values()):
        if m in sys.modules:
            if hasattr(sys.modules[m], 'unregister'):
                sys.modules[m].unregister()

if __name__ == "__main__":
    register()
