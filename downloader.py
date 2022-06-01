import yt_dlp
import os
from pathlib import Path
from sys import argv

# Creates file paths
songsDir = Path.cwd().joinpath('Songs') 
listDir = Path.cwd().joinpath(argv[1]) 

# song directory
if not songsDir.is_dir():
	songsDir.mkdir() # makes directory
else:
	os.chdir('Songs') # change cwd to directory

# Downloads data and configs
download_options = {
	'format' : 'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s', # '{path}/%(title)s.%(ext)s'.format(path = songsDir)
	'nocheckcertificate': True,
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}
    
# download songs
with yt_dlp.YoutubeDL(download_options) as dl:
	with open(listDir , 'r') as f:
		for song_url in f:
			dl.download([song_url])