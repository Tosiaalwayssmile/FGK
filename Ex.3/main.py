from Primitives.sphere import *
from Primitives.triangle import *
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *

# ============
#    ZAD 2
# ============
p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, fov=40)
o_cam = OrthogonalCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=500, height=500, pixel_size=(0.01, 0.01))

primitives1 = [
    #Sphere(Vec3(0, 0, 8), 2, [.2, .4, .75]),
    #Sphere(Vec3(2, 0, 7), 1, [.9, .0, 0]),
    Triangle(Vec3(-1, 0, 8), Vec3(0, 1, 8), Vec3(1, 0, 8), [0, 0, 0])
   
]

primitives2 = [
    Sphere(Vec3(0, 0, 8), 1, [.4, .4, .7]),
]


p_cam.render_scene(primitives1, antialiasing=True)
#o_cam.render_scene(primitives1)

print('KONIEC')
