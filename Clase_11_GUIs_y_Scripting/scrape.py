import argparse
import base64
import json
from pathlib import Path
import re
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

# Función para realizar el scraping de imágenes
def scrape(url, format_, type_):
    try:
        page = requests.get(url)
        page.raise_for_status()  # Asegúrate de que no hubo errores al hacer la solicitud
    except requests.RequestException as err:
        print(str(err))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = fetch_images(soup, url)
        images = filter_images(images, type_)
        save(images, format_)
        save_json_with_titles_prices(images)  # Siempre guardar la información en un archivo JSON

# Función para obtener las imágenes y títulos del contenido HTML
def fetch_images(soup, base_url):
    # Trabaja con rutas relativas y absolutas de src.
    images = []
    for img, title, price in zip(soup.find_all('img', attrs={'class': 'product-image-photo'}),
                          soup.find_all('a', attrs={'class': 'product-item-link'}),
                          soup.find_all('span', attrs={'class': 'price'})):
        src = img.get('src')
        if src:
            img_url = urljoin(base_url, src)  # Construye la URL completa
            name = sanitize_filename(img_url.split('/')[-1])
            product_title = title.get_text(strip=True)
            price = price.get_text(strip=True)
            images.append(dict(name=name, url=img_url, title=product_title, price=price))
    return images

# Función para filtrar las imágenes por tipo (png, jpg, webp, etc.)
def filter_images(images, type_):
    if type_ == 'all':
        return images
    ext_map = {
        'png': ['.png'],
        'jpg': ['.jpg', '.jpeg'],
        'webp': ['.webp'],
    }
    return [
        img for img in images
        if matches_extension(img['name'], ext_map[type_])
    ]

# Función para verificar si el archivo tiene una extensión válida
def matches_extension(filename, extension_list):
    extension = Path(filename.lower()).suffix
    return extension in extension_list

# Función para limpiar y sanitizar el nombre del archivo
def sanitize_filename(filename):
    # Eliminar los parámetros de la URL después del nombre de archivo
    filename = filename.split('?')[0]
    # Reemplaza caracteres no permitidos en nombres de archivos en Windows
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# Función para guardar las imágenes o los datos en formato JSON
def save(images, format_):
    if images:
        if format_ == 'img':
            save_images(images)
        else:
            save_json(images)
        print('Done')
    else:
        print('No images to save.')

# Función para guardar las imágenes como archivos
def save_images(images):
    for img in images:
        try:
            response = requests.get(img['url'])
            response.raise_for_status()  # Asegúrate de que la solicitud fue exitosa
            img_data = response.content
            with open(img['name'], 'wb') as f:
                f.write(img_data)
        except requests.RequestException as err:
            print(f"Error al descargar la imagen {img['url']}: {err}")

# Función para guardar las imágenes en un archivo JSON codificadas en base64
def save_json(images):
    data = {}
    for img in images:
        try:
            response = requests.get(img['url'])
            response.raise_for_status()  # Asegúrate de que la solicitud fue exitosa
            img_data = response.content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data
        except requests.RequestException as err:
            print(f"Error al descargar la imagen {img['url']}: {err}")

    with open('images.json', 'w') as ijson:
        ijson.write(json.dumps(data, ensure_ascii=False, indent=4))

# Función para guardar siempre la información en un archivo JSON con títulos, URLs y precio
def save_json_with_titles_prices(images):
    data = []
    for img in images:
        data.append({
            'title': img['title'],
            'image_url': img['url'],
            'image_name': img['name'],
            'price': img['price']
        })

    with open('products.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Código principal para parsear los argumentos y ejecutar el scraping
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scrape a webpage.')
    parser.add_argument(
        '-t',
        '--type',
        choices=['all', 'png', 'jpg', 'webp'],
        default='all',
        help='The image type we want to scrape.')

    parser.add_argument(
        '-f',
        '--format',
        choices=['img', 'json'],
        default='img',
        help='The format images are saved to.')

    parser.add_argument(
        'url',
        help='The URL we want to scrape for images.')

    args = parser.parse_args()
    scrape(args.url, args.format, args.type)