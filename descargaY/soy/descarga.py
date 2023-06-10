import pytube

while True:
    url = input("Pon aquí tu asqueroso video que haré el trabajo (o 'salir' para terminar): ")
    
    if url.lower() == 'salir':
        print("Ya me voy cuidate... ")
        break

    video = pytube.YouTube(url)

    formato = input("Das pena, selecciona tu formato rápido, animal (mp4 o mp3): ")

    if formato.lower() == 'mp4':
        video.streams.filter(file_extension='mp4').first().download()
        print("¡Toma tu video asqueroso en formato mp4!")
    elif formato.lower() == 'mp3':
        audio = video.streams.filter(only_audio=True).first()
        audio.download()
        print("¡Toma tu asqueroso audio en formato mp3!")
    else:
        print("El formato es inválido, ni para eso eres bueno")

    continuar = input("¿Deseas descargar otro video? (s/n): ")
    if continuar.lower() != 's':
        print("Hasta luego")
        break