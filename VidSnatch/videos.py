import yt_dlp

#############YOUTUBE
def obtener_enlaces(url):
    ydl_opts = {
        'quiet': False,
        'format': 'bestvideo+bestaudio',  # Obtener el mejor formato de video y audio disponibles
        'noplaylist': True,  # Para evitar listas de reproducción
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Obtener la información del video
            info = ydl.extract_info(url, download=False)

            # Inicializamos una lista para almacenar los enlaces de video
            enlaces = {
            'full': [],
            'audio': [],
            'video': []
            }

            # Recorremos todos los formatos disponibles
            for format in info['formats']:
                # Filtramos los formatos que tengan tanto video como audio
                if format.get('vcodec') != 'none' and format.get('acodec') != 'none':
                    enlaces['full'].append({"tipo":'video' , "resolucion":format['format_note'], "formato":format['ext']})

                if format.get('vcodec') != 'none' and format.get('acodec') == 'none':
                    if 'm3u8' not in format['url']:
                        enlaces['video'].append({"tipo":'video' , "resolucion":format['format_note'], "formato":format['ext']})

                if format.get('acodec') != 'none' and format.get('vcodec') == 'none':
                    if 'm3u8' not in format['url']:
                        enlaces['audio'].append({"tipo":'video' , "resolucion":format['format_note'], "formato":format['ext']})
            return enlaces
    except:
        return "Enlace no valido." 





####################################TWITTER
def descargar_video_twitter(url):
    ydl_opts = {
        'quiet': False,  # Para ver los detalles del proceso de descarga
        'format': 'best',  # Obtiene el mejor formato disponible
        'noplaylist': True,  # No descargar listas de reproducción
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info['url']
    except:
        return "No se ha encontrado video en el tweet."



########################INSTAGRAM
def descargar_video_instagram(url):
    # Opciones de configuración para yt-dlp
    ydl_opts = {
        'quiet': False,  # Para ver los detalles del proceso de descarga
        'format': 'best',  # Obtiene el mejor formato disponible
        'noplaylist': True,  # No descargar listas de reproducción
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Descargar el video de Instagram
                info = ydl.extract_info(url, download=False)
                return info['url']
    except:
        return "Enlace/Video invalido."




#### USO INSTAGRAM
# url_instagram = 'https://www.instagram.com/p/DHDARs-MN/'  # Sustituye con el enlace de Instagram del video
# print(descargar_video_instagram(url_instagram))


###### USO TWITTER
# url_tweet = 'https://x.com/Yoda4ever/status/1907273784714723791'  # Sustituye con el enlace del tuit
# print(descargar_video_twitter(url_tweet))


# ####USO YOUTUBE
# url_youtube = "https://www.youtube.com/watch?v=0xfE3dujc8k"
# print(obtener_enlaces(url_youtube))


