import os
import time
import random
import threading
from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp

app = Flask(__name__)

# Directorio donde se almacenarán los archivos temporalmente
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')

# Crear la carpeta de descargas si no existe
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


def borrar_archivo_despues(path, delay=5):
    """
    Función para borrar el archivo temporal en segundo plano.
    Espera unos segundos para asegurarse de que Windows haya liberado la conexión HTTP.
    """
    def borrar():
        time.sleep(delay)
        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"[Info] Archivo temporal eliminado: {os.path.basename(path)}")
        except Exception as e:
            print(f"[Error] No se pudo eliminar el archivo temporal: {e}")

    # Ejecuta la tarea en un hilo independiente para no congelar Flask
    threading.Thread(target=borrar).start()


@app.route('/')
def index():
    """Renderiza la interfaz principal HTML."""
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download_video():
    """Recibe la URL, descarga el video con un identificador único y lo envía al usuario."""
    data = request.get_json()
    video_url = data.get('url') if data else None

    if not video_url:
        return jsonify({'error': 'Debes proporcionar una URL válida.'}), 400

    # Genera un número aleatorio de 4 dígitos (ej: 4821)
    random_id = random.randint(1000, 9999)

    # Plantilla del nombre: "Título del Video [1234].ext"
    output_template = os.path.join(DOWNLOAD_FOLDER, f'%(title)s [{random_id}].%(ext)s')

    # Configuración de yt-dlp
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': output_template,
        'quiet': True,
        'no_warnings': True,
        # Evita errores de firmas/páginas usando los clientes de Android/iOS/Web
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'ios', 'web']
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extraer información y procesar la descarga
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)

        # Programar la eliminación diferida a los 5 segundos
        borrar_archivo_despues(filename, delay=5)

        # Enviar el archivo procesado hacia el navegador
        return send_file(
            filename,
            as_attachment=True,
            download_name=os.path.basename(filename)
        )

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar el video: {str(e)}'}), 500


if __name__ == '__main__':
    print("Servidor Flask iniciado correctamente.")
    print("Accede a http://127.0.0.1:5000/ en tu navegador.")
    app.run(debug=True, port=5000)