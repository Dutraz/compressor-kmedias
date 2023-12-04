# Compressor de Imagens K-Medias

Este projeto é um compressor de imagens que aplica o algoritmo k-médias em imagens selecionadas, gerando novas imagens
com redução de cores.

## Instruções de Uso

1. Coloque as imagens originais na pasta "images" com resolução de pelo menos 1280x720 pixels no formato PNG.
2. Instale as bibliotecas necessárias executando o comando:
    ```bash
    pip install -r requirements.txt
    ```
3. No arquivo "main.py":
    - Modifique o parâmetro "mode" para "CONTINUE" ou "RESTART" para continuar a execução ou reiniciar o algoritmo.
    - Ajuste a quantidade de cores das imagens geradas no array "clusters".
4. Execute o projeto com o comando:
    ```bash
    python main.py
    ```
5. As imagens resultantes serão armazenadas na pasta "outputs" dentro da pasta numerada correspondente à execução do
   algoritmo.

## Detalhes do Projeto

O software utiliza o algoritmo k-médias para comprimir imagens, variando o valor de k para reduzir a quantidade de cores
nas imagens originais. Ele gera novas imagens a partir dos centroides identificados pelo algoritmo e das imagens
originais.

### Experimento

- Seis imagens com resoluções diferentes foram selecionadas para aplicar o algoritmo com sete valores distintos de k,
  gerando um total de 42 novas imagens.
- Antes do experimento final, foram realizados testes para determinar o valor mínimo de k que não distorcesse
  significativamente as imagens resultantes.

### Informações Geradas

Para cada imagem original e suas versões geradas, o software computa e salva:

- Resolução da imagem em pixels.
- Tamanho ocupado em memória pela imagem em KB.
- Quantidade de cores únicas.


### Resultados

- O resultado do experimento pode ser visto no arquivo [relatorio.pdf](relatorio.pdf).
- Além disso, as imagens resultantes do experimento podem ser vistas na pasta [outputs_example](output_example/) deste projeto.