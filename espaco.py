import urllib.request
import matplotlib.pyplot as plt
from PIL import Image

def baixar_imagem(url, nome_arquivo):
    urllib.request.urlretrieve(url, nome_arquivo)

import numpy as np

def exibir_imagem(nome_arquivo):
    img = Image.open(nome_arquivo)
    img_array = np.array(img)
    plt.imshow(img_array)
    plt.axis('off')
    plt.show()

# Exemplo de uso
url_imagem = 'https://apod.nasa.gov/apod/image/2307/VenusUv_akatsuki_1024.jpg'
nome_arquivo = 'imagem_astronomica.jpg'

plt.bar(url_imagem, nome_arquivo)

baixar_imagem(url_imagem, nome_arquivo)
exibir_imagem(nome_arquivo)
