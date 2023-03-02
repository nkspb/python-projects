import tkinter as tk
from pytube import YouTube
from os.path import expanduser

def download():
    '''Download with highest resolution for audio track combined'''
    yt = YouTube(url.get())
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(download_path.get())

home_path = expanduser("~")
window = tk.Tk()
window.title('YouTube Downloader')
window.geometry('375x120')
window.resizable(False, False)
window.configure(bg='#da2f4c')

url_lbl = tk.Label(text='Video URL: ', bg='#da2f4c', fg='white', padx=10)
url_lbl.grid(row=0, column=0, pady=10)

url = tk.Entry(width=45)
url.insert(0, str("https://www.youtube.com/watch?v="))

url.grid(row=0, column=1)

download_path_lbl = tk.Label(text='Save to: ', bg='#da2f4c', fg='white', padx=10)
download_path_lbl.grid(row=1, column=0)

download_path = tk.Entry(width=45)
download_path.insert(0, str(home_path + "\Videos\YouTube"))
download_path.grid(row=1, column=1)

download_btn = tk.Button(text='Download', width=10, height=2, command=download)
download_btn.grid(row=2, column=1, pady=10, sticky="e")

window.mainloop()
