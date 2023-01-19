import tkinter as tk
from pytube import YouTube

def download_video():
    yt = YouTube(address.get())
    ys = yt.streams.get_highest_resolution()
    ys.download(save_path.get())

window = tk.Tk()

frame_1 = tk.Frame()
frame_2 = tk.Frame()

# address input
address = tk.Entry(master=frame_1, width=50)
address.insert(0, "https://")

dl_button = tk.Button(master=frame_1, text="Download", command=download_video)
address.pack(side=tk.LEFT)
dl_button.pack(side=tk.LEFT)

save_path = tk.Entry(master=frame_2, width=50)
save_path.insert(0, "C:\Temp")
save_path.pack()

frame_1.pack()
frame_2.pack()

window.mainloop()