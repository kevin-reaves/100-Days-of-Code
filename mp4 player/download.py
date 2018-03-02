#import youtube_dl
#very basic version. Downloads full video
"""
ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=lqURPBtGJzg'])
"""

import pafy

url = 'https://www.youtube.com/watch?v=lqURPBtGJzg'
video = pafy.new(url)
print("Title: " + video.title)
print("Author: " + video.author)
print("Duration: " + video.duration)

best = video.getbest(preftype="mp4")
best.download(quiet=True)
