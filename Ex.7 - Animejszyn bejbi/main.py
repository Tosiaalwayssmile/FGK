import imageio
from Cameras.perspective_camera import *
from Cameras.orthogonal_camera import *
from datetime import datetime


if __name__ == '__main__':
    p_cam = PerspectiveCamera(position=Vec3(0, 0, 0), view_direction=Vec3(0, 0, 1), width=512, height=512, fov=60)

    amount_of_frames = 360
    processes = 16
    blur_ratio = 5

    shutter_exposure_time = 1 / amount_of_frames
    images_file = []
    for i in range(amount_of_frames):
        print('GENERATING IMAGE: ' + str(i + 1))
        filename = ('Images/Image_' + str(i) + '.png')

        start = datetime.now()
        image = p_cam.render_scene((shutter_exposure_time * i, shutter_exposure_time * (i + 1)), blur_ratio=blur_ratio, antialiasing=False, amount_of_processes=processes)
        MyImage.save_image(image, filename)
        end = datetime.now()

        images_file.append(imageio.imread(filename))

        elapsed = end - start
        print('Amount of processes: ' + str(processes) + '\t| Blur ratio: ' + str(blur_ratio) + '\t| Time: ' + str(elapsed.seconds) + ':' + str(elapsed.microseconds) + ' s')

    gif_name = 'animation.gif'
    if os.path.exists(gif_name):
        os.remove(gif_name)
    print('GENERATING GIF...')
    imageio.mimsave(gif_name, images_file, fps=60)
    print('FINISHED')