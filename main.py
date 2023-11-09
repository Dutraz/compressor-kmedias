import cv2
import matplotlib.pyplot as plt
import numpy as np


def kmeans(src, clusters):
    # Carrega a Imagem
    image = cv2.imread(src)

    # Convertendo a imagem de BGR para RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reformatando a imagem em uma matriz 2D de pixels e 3 valores de cores (RGB)
    pixel_vals = image.reshape((-1, 3))

    # Convertendo os valores de pixel para float para suportar o cv2.kmean
    pixel_vals = np.float32(pixel_vals)

    retval, labels, centers = cv2.kmeans(
        pixel_vals,
        clusters,
        None,

        # Definindo o critério de parada
        # Para ao atingir a precisão de 0.85 ou 100 iterações
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85),

        # Número de vezes que o algoritmo vai tentar obter o melhor resultado iniciando por outro valor
        10,

        # Definindo o método de inicialização dos centros como aleatório
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Convertendo os valores de pixel para inteiros e mapeando os valores de pixel para cada centro
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    # Reformatando a imagem para o tamanho original
    segmented_image = segmented_data.reshape((image.shape))

    return segmented_image


def show_image(image):
    height, width, channels = image.shape

    plt.figure()
    plt.imshow(image)
    fig = plt.gcf()
    fig.set_size_inches(width / 100, height / 100)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()


if __name__ == '__main__':
    for n in [2, 4, 8, 16, 32, 64, 128, 256]:
        image = kmeans('./images/arcane_1.png', n)
        show_image(image)
