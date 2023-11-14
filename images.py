import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def kmeans(path, clusters):
    # Carrega a Imagem
    img = cv2.imread(path)

    # Convertendo a imagem de BGR para RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reformatando a imagem em uma matriz 2D de pixels e 3 valores de cores (RGB)
    pixel_vals = img.reshape((-1, 3))

    # Convertendo os valores de pixel para float para suportar o cv2.kmean
    pixel_vals = np.float32(pixel_vals)

    retval, labels, centers = cv2.kmeans(
        pixel_vals,
        clusters,
        None,

        # Definindo o critério de parada
        # Para ao atingir a precisão de 0.85 ou 500 iterações
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 500, 0.85),

        # Número de vezes que o algoritmo vai tentar obter o melhor resultado iniciando por outro valor
        10,

        # Definindo o método de inicialização dos centros como aleatório
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Convertendo os valores de pixel para inteiros e mapeando os valores de pixel para cada centro
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    # Reformatando a imagem para o tamanho original
    segmented_image = segmented_data.reshape(img.shape)

    return segmented_image


def show_image(img):
    # Carrega dimensões da imagem
    height, width, channels = img.shape

    # Plota a imagem
    plt.figure()
    plt.imshow(img)
    fig = plt.gcf()

    # Configura o tamanho da imagem
    fig.set_size_inches(width / 100, height / 100)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Mostra a imagem
    plt.show()


def unique_count(img):
    colors, counts = np.unique(
        img.reshape(-1, img.shape[-1]),
        return_counts=True,
        axis=0,
    )
    return counts.size


def save_image(img, name, clusters, output_id=0):
    # Cria a pasta de saída, caso não exista
    folder = f'./outputs/{output_id}'
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Salva a imagem
    path = f'{folder}/{name[:-4]}_{clusters}.png'
    if not cv2.imwrite(path, img):
        raise Exception('Erro ao salvar imagem')

    return path


def get_size_in_mb(path):
    return os.path.getsize(path) / 1000000
