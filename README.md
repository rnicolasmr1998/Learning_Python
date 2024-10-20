<!-- PROJECT PRESENTATION -->
<div align="center">
  <a href="https://github.com/rnicolasmr1998/Learning_Python">
    <img src="https://www.python.org/static/img/psf-logo.png">
  </a>

  <h1 align="center">Introducción a Python</h1>
</div><br>

<!-- ABOUT THE PROJECT -->
## 📖 Acerca del repositorio

Este repositorio contiene notas de clase y ejemplos prácticos para aprender Python. Es un recurso diseñado para principiantes y aquellos interesados en mejorar sus habilidades en programación, abarcando conceptos fundamentales del lenguaje y ejercicios prácticos.

### Temario
| Nº  | Tema                                   | Descripción                                       | Carpeta              |
| :-: | -------------------------------------- | :----------------------------------------------- | :------------------: |
| 01  | Tipos de datos                         | Introducción a los diferentes tipos de datos en Python, como enteros, flotantes y cadenas. | [Abrir][guide01-url] |
| 02  | Condicionales e iteración             | Uso de estructuras de control como `if`, `for`, y `while` para el flujo de programas. | [Abrir][guide02-url] |
| 03  | Funciones                              | Definición y uso de funciones, incluyendo parámetros y retorno de valores. | [Abrir][guide03-url] |
| 04  | Comprensiones y generadores            | Creación de listas y generadores de manera eficiente usando comprensiones. | [Abrir][guide04-url] |
| 05  | OOP, decoradores e iteradores          | Principios de la programación orientada a objetos, uso de decoradores y iteradores. | [Abrir][guide05-url] |
| 06  | Excepciones y gestores de contexto     | Manejo de errores con excepciones y uso de gestores de contexto para recursos. | [Abrir][guide06-url] |
| 07  | Ficheros y persistencia de datos       | Lectura y escritura de archivos, así como técnicas para la persistencia de datos. | [Abrir][guide07-url] |
| 08  | Criptografía y tokens                  | Fundamentos de la criptografía y manejo de tokens para la seguridad de datos. | [Abrir][guide08-url] |
| 09  | Testing                                | Estrategias para realizar pruebas en Python, incluyendo pruebas unitarias. | [Abrir][guide09-url] |
| 10  | Depuración y creación de perfiles      | Técnicas de depuración y análisis de rendimiento de aplicaciones en Python. | [Abrir][guide10-url] |
| 11  | GUIs y scripting                       | Desarrollo de interfaces gráficas y automatización de tareas mediante scripting. | [Abrir][guide11-url] |
| 12  | Data science                           | Aplicación de Python en ciencia de datos, incluyendo análisis y visualización. | [Abrir][guide12-url] |


## 🚀 Ejecutando el proyecto

Para poner en funcionamiento una copia local de los ejercicios de este repositorio, siga los siguientes pasos.

### Requisitos previos

**Obligatorio**

```txt
Python >= 3.09
```
Opcional

```txt
Visual Studio Code o PyCharm
```

### Configuración
1. Cree un entorno virtual dentro del proyecto y actívelo.

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

2. Descargue o clone este repositorio dentro de dicho proyecto.

```bash
git clone https://github.com/rnicolasmr1998/Learning_Python.git
```

3. Instale las dependencias necesarias usando el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```
4. Si utiliza SQLAlchemy, cree el archivo `config.py` con los detalles de conexión a la base de datos:

``` python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://your_user:your_password@localhost/your_database'
```
Modifique los valores de conexión de acuerdo a su entorno de base de datos.

## 📞 Contacto

Desarrollado por Nicolas Marroquin.
<p align="left">
  <a href="https://www.linkedin.com/in/rnicolas98/" target="_blank"> <img align="center"
  src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png" alt="Nicolas Marroquin" height="30" width="40"
  /> linkedin</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="mailto:rnicolas.mr.98@gmail.com" target="_blank"> <img align="center"
  src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/2560px-Gmail_icon_%282020%29.svg.png" alt="Nicolas Marroquin" height="30"
  width="40" /> rnicolas.mr.98@gmail.com </a>
</p>

<!-- ACKNOWLEDGMENTS -->
## 📚 Material revisado

Este repositorio contiene notas y recursos de libros sobre Python, como "Learn Python Programming" de Fabrizio Romano y Heinrich Kruger [[enlace](https://www.packtpub.com/en-us/product/learn-python-programming-3rd-edition-9781801815093?srsltid=AfmBOopOuH1kc6rsECq-Jl-S7eAg-WoSxK0kVmsafo8obWcU1byRbi2-)], "Python Crash Course" de Eric Matthes [[enlace](https://www.amazon.com/Python-Crash-Course-2nd-Edition/dp/1593279280)], y "Fluent Python" de Luciano Ramalho [[enlace](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)]. Además, se incluyen notas de capacitaciones realizadas en diversas instituciones dentro del Perú, lo que complementa la formación teórica con experiencia práctica.


[guide01-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_01_Tipos_de_datos/Sesion_01.ipynb
[guide02-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_02_Condicionales_e_Iteraccion/Sesion_02.ipynb
[guide03-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_03_Funciones/Sesion_03.ipynb
[guide04-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_04_Comprensiones_y_Generadores/Sesion_04.ipynb
[guide05-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_05_OOP_Decoradores_e_Iteradores/Sesion_05.ipynb
[guide06-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_06_Excepciones_y_Gestores_de_Contexto/Sesion_06.ipynb
[guide07-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_07_Ficheros_y_Persistencia_de_datos/Sesion_07.ipynb
[guide08-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_08_Criptograf%C3%ADa_y_tokens/Sesion_08.ipynb
[guide09-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_09_Testing/Sesion_09.ipynb
[guide10-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_10_Depuraci%C3%B3n_y_Creaci%C3%B3n_de_Perfiles/Sesion_10.ipynb
[guide11-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_11_GUIs_y_Scripting/Clase_11.ipynb
[guide12-url]: https://github.com/rnicolasmr1998/Learning_Python/blob/main/Clase_12_Data_Science/Clase_12.ipynb