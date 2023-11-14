import logging
import os

import cv2

from images import unique_count, get_size_in_mb


def setup_logger(output_id):
    log_path = f'./outputs/{output_id}/log.txt'

    # Caso não exista, cria o arquivo de log
    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))

    logging.basicConfig(
        filename=log_path,
        filemode='w',
        format='%(message)s',
        encoding='utf-8',
    )

    # Seta o nível de log para DEBUG e adiciona um handler para imprimir no console
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())


def print_info(path, resolution=False, timer=None, original_size=None):
    logger = logging.getLogger()

    size = get_size_in_mb(path)
    width, height, channels = cv2.imread(path).shape

    img = cv2.imread(path)
    colors = unique_count(img)

    if resolution:
        logging.info(f'Resolução: {width}x{height}')

    logger.info(f'Nº de cores: {colors}')
    logger.info(f'Tamanho: {size} mb')

    if original_size:
        logger.info(f'Compressão: {100 - (size / original_size * 100):.2f}%')

    if timer:
        logger.info(f'Tempo: {timer:.2f} s')

    logger.info('')


def print_initial_info(image_name):
    logger = logging.getLogger()
    logger.info('=====================================')
    logger.info(f'Imagem: {image_name}')
