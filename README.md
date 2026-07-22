# MI_EXTRACTOR_VIDEO

MI_EXTRACTOR_VIDEO es una App Web sencilla y fácil de usar para la descarga de videos de distintas webs usando la URL y que podemos ejecutar en local. 
Esta construida en ***"Python"*** usando ***"Flask"*** y la librería ***"yt_dlp"***.

**Estructura de archivos y directorios:**

```text
mi_extractor_video/
│
├── app.py                  # Servidor principal y endpoints de la API Flask
├── requirements.txt        # Gestión de dependencias y librerías Python
│
├── downloads/              # Carpeta temporal de almacenamiento binario
│
├── templates/              # Vistas HTML (Procesadas por el motor Jinja2)
│   └── index.html          # Interfaz de usuario y maquetación de la app
│
└── static/                 # Recursos web estáticos públicos
    ├── css/
    │   └── styles.css      # Hoja de estilos (Diseño responsivo y componentes)
    └── js/
        └── main.js         # Lógica cliente (Peticiones Fetch asíncronas y manipulación DOM)
```


---


## Requisitos

  * Tener instalado Python 3.9.* o superior (recomendado)
  * SO Windows 10/11


---


## Configuración inicial

  1. Descargamos archivo ***.zip*** del repositorio o
     lo clonamos con git:
     
```text
git clone https://github.com/jullianamigoes/mi_extractor_video.git
```

  2. Abrimos la terminal bash o cmd. Nos ubicamos en la raíz del proyecto y ejecutamos el siguiente comando:

```text
python install -r requirements.txt
```


----


## Ejecutar Servidor Web

  Desde la terminal debemos ubicarnos en la raíz del proyecto y escribir el siguiente comando:

```text
python app.py
```


  Nos mostrará el enlace de la web el cual debemos acceder presionando tecla **CRTL** + **Clic**

![levantar servidor](https://github.com/jullianamigoes/assets_proj/blob/main/assets/mi_extractor_de_video/servidor_web.png)



### Imagen de la Web

![vista web local](https://github.com/jullianamigoes/assets_proj/blob/main/assets/mi_extractor_de_video/interfaz_web.png)
