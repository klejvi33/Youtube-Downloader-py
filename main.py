from pytube import YouTube

link = input("Enter the link: ")

video = YouTube(link)

print(video.title)

print(video.streams.filter(progressive=True))

stream = video.streams.get_by_itag(22)
stream.download()
print("Video downloaded")