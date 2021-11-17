#python -m pip install pytube ======> install library pytube

from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=MIazavfywBo').streams.filter(res="720p").first().download()
