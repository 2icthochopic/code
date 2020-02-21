# ydl1.py
import youtube_dl

dl_url = input('URL: ')
dl_format = input('Download video or just audio? ')
if dl_format == 'video':
	format = 'mp4'
if dl_format == 'audio':
	format = 'm4a'

ydl_opts = {'noplaylist' : True}
ydl_opts['format'] = format

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	print(f'DOWNLOADING... {format} format')
	ydl.download([dl_url])