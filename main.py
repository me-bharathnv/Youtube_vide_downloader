import pytube
link = ""     # youtube video link
yt = pytube.YouTube(link)
stream = yt.streams.get_by_resolution(resolution="720p")
stream.download()
