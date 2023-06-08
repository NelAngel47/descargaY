import pytube

url = input("Pon aquí tu asqueroso video que haré el trabajo: ")
video = pytube.YouTube(url)

formato = input("Das pena, selecciona tu formato rápido, animal (mp4 o Mp3): ")

if formato == 'mp4':
    video.streams.filter(file_extension='mp4').first().download()
    print("¡Toma tu video asqueroso en formato mp4!")
elif formato == 'mp3':
    audio = video.streams.filter(only_audio=True).first()
    audio.download()
    print("¡Toma tu asqueroso audio en formato mp3!")
else:
    print("El formato es inválido, ni para eso eres bueno")