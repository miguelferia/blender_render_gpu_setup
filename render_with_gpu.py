import bpy

prop = bpy.context.preferences.addons['cycles'].preferences
prop.get_devices()
prop.compute_device_type = 'CUDA'

for device in prop.devices:
    if device.type == 'CUDA':
        device.use = True
bpy.context.scene.cycles.device = 'GPU'

print('hello nagwwork ba to dito hehe')
print('-'*30)

for scene in bpy.data.scenes:
    scene.cycles.device = 'GPU'
    scene.render.tile_x = 600
    scene.render.tile_y = 600