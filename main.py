import logging
import os
import time

from images import kmeans, save_image, get_size_in_mb
from log import print_info, setup_logger

if __name__ == '__main__':

    images = [f for f in os.listdir('./images') if f.endswith('.png')]
    output_id = max([int(f) for f in os.listdir('./outputs') if f.isdigit()] + [0]) + 1

    setup_logger(output_id)
    logger = logging.getLogger()

    for image_name in images:
        path = f'./images/{image_name}'

        logger.info('=====================================')
        logger.info(f'Imagem: {image_name}')
        print_info(path, resolution=True)

        original_size = get_size_in_mb(path)

        for n in [2, 4, 8, 16, 32, 64, 128, 256]:
            start = time.time()
            new_image = kmeans(path, n)
            timer = time.time() - start

            output = save_image(new_image, image_name, n, output_id)
            print_info(output, timer=timer, original_size=original_size)
