import time

from images import kmeans, save_image, get_size_in_mb
from log import print_info, setup_logger, print_initial_info
from utils import MODE, get_images, get_last_output, output_exists

if __name__ == '__main__':

    # Parâmetros de execução
    mode = MODE.RESTART
    sizes = [2, 4, 8, 16, 32, 64, 128, 256]

    # Busca as imagens em disco e o último output gerado
    images = get_images()
    last_output = get_last_output()
    output_id = last_output + 1 if mode == MODE.RESTART else last_output

    setup_logger(output_id)

    for image_name in images:
        path = f'./images/{image_name}'

        # Faz o log inicial da imagem
        if mode == MODE.RESTART or not output_exists(output_id, image_name, sizes[0]):
            print_initial_info(image_name)
            print_info(path, resolution=True)

        # Salva o tamanho original da imagem para calcular a compressão
        original_size = get_size_in_mb(path)

        for n in sizes:

            # Pula a execução caso o output já exista e o modo seja CONTINUE
            if mode == MODE.CONTINUE and output_exists(output_id, image_name, n):
                continue

            # Executa o algoritmo e calcula o tempo de execução
            start = time.time()
            new_image = kmeans(path, n)
            timer = time.time() - start

            # Salva a imagem e faz o log final da execução
            output = save_image(new_image, image_name, n, output_id)
            print_info(output, timer=timer, original_size=original_size)
