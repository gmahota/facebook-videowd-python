import sys
import yt_dlp

def baixar_video_facebook(url):
    # Opções de download
    ydl_opts = {
        'format': 'best',  # Melhor qualidade disponível com vídeo e áudio juntos
        'outtmpl': 'video_whatsapp.mp4',  # Nome do arquivo de saída em MP4
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Converte para MP4
        }],
        'postprocessor_args': [
            '-vf', 'scale=-1:240',  # Reduz a resolução para 240p
            '-b:v', '500k',  # Limita a taxa de bits de vídeo para 500 kbps
            '-b:a', '64k',   # Limita a taxa de bits de áudio para 64 kbps
        ],
    }

    # Download do vídeo
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, forneça a URL do vídeo.")
    else:
        video_url = sys.argv[1]
        print(f"Baixando vídeo de: {video_url}")
        baixar_video_facebook(video_url)
        print("Download concluído!")
