import os


class MODE:
    CONTINUE = 0
    RESTART = 1


def get_images():
    return [f for f in os.listdir('images') if f.endswith('.png')]


def get_output_images(output_id):
    return [f for f in os.listdir(f'./outputs/{output_id}') if f.endswith('.png')]


def get_last_output():
    return max([int(f) for f in os.listdir('outputs') if f.isdigit()] + [0])


def output_exists(output_id, image, clusters):
    return os.path.exists(f'./outputs/{output_id}/{image[:-4]}_{clusters}.png')
