from pytube import YouTube

link = input("please provide link :  ")

check = int(input("press 1 for vedio : press 2 for audio :  "))

if check == 1:
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.filter(progressive = True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    strm = int(input("please provide your index you want to download"))
    videos[strm].download()
    print("successfully Downloaded   :  ")

if check == 2:
    youtube_1 = YouTube(link)
    audio = youtube_1.streams.filter(Only_audio = True)
    vid = list(enumerate(audio))
    for i in vid:
        print(i)
    strm = int(input("please provide your index you want to download"))
    audio[strm].download()
    print("successfully Downloaded   :  ")



