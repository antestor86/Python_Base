import random
from pytube import YouTube
def getTuple():
    numbers = [random.randint(1, 100) for _ in range(10)]
    pairs = [[(numbers[i],numbers[i+1])] for i in range(0,len(numbers),2)]
    print(numbers)
    return pairs

def sortTuple():
    numbers = [random.randint(1, 100) for _ in range(10)]
    main_tuple = tuple(numbers.sort())
    return main_tuple

def downloadYouTube(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download(r"C:\Users\razmik.avetisyan\Downloads")
    print("Video Downloaded!")





# ur = "https://youtu.be/D-Zvjhz3bRs"
# download = downloadYouTube(ur)



