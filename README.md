# Scraper de Comentarios de YouTube para el Canal de Claudia Sheinbaum

Este script en Python utiliza la API de YouTube Data v3 para buscar el canal oficial de Claudia Sheinbaum, obtener los videos más recientes y extraer los 100 comentarios mas recientes de cada video.

## 📦 ¿Qué hace este script?

- Busca en YouTube el canal `ClaudiaSheinbaumP`
- Obtiene los 10 videos más recientes del canal
- Extrae hasta 100 comentarios de nivel superior por video
- Guarda los resultados (ID del comentario, texto, ID del video y URL) en un archivo CSV en la carpeta `../data`

## 🛠 Requisitos

Crea el entorno con:

```bash
conda env create -f environment.yml
conda activate nombre-del-entorno
