from pytube import YouTube
def downloadYouTube(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download(r"C:\Users\razmik.avetisyan\Downloads")
    print("Video Downloaded!")

ur = "https://youtu.be/D-Zvjhz3bRs"
download = downloadYouTube(ur)

