import yt_dlp

# URL do vídeo no Facebook
url = 'https://www.youtube.com/watch?v=LgmL4TQCNtI'

# Opções de download para limitar o tamanho do vídeo a aproximadamente 1 MB
ydl_opts = {
    'format': 'mp4',  # Definir o formato como MP4
    'outtmpl': 'video_whatsapp_1mb.mp4',  # Nome do arquivo de saída
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Converte para MP4
    }],
    'video-quality': '20',  # Valor de qualidade para ajustar a compressão (menor número, menor qualidade)
    'postprocessor_args': [
        '-vf', 'scale=-1:240',  # Reduz a resolução para 240p
        '-b:v', '500k',  # Limita a taxa de bits de vídeo para 500 kbps
        '-b:a', '64k',   # Limita a taxa de bits de áudio para 64 kbps
    ],
}

# Download do vídeo
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")
