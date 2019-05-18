#import youtube_dl
#very basic version. Downloads full video
"""
ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=TVcLIfSC4OE'])
"""

import pafy

#single video download
"""
url = 'https://www.youtube.com/watch?v=TVcLIfSC4OE'
video = pafy.new(url)
print("Title: " + video.title)
print("Author: " + video.author)
print("Duration: " + video.duration)

best = video.getbest(preftype="mp4")
best.download(quiet=True)
"""

#whole playlist download

url = 'https://www.youtube.com/playlist?' \
      'list=PLycc1MSxGszrZk7S9tdhqhd0_K8aA5UfS'

playlist = pafy.get_playlist(url)
for item in playlist['items']:
    print("Title: " ,item['pafy'].title)
    print("Author: ", item['pafy'].author)
    print("Duration: ", item['pafy'].duration)

    try:
        best = item['pafy'].getbest(preftype="mp4")
        best.download(quiet=True)
    except Exception as e:
        print(item['pafy'].title , " couldn't be downloaded")
