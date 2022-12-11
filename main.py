import pytube as pt
from pytube import Playlist
from tkinter import *
import threading

root = Tk()
root.title('Youtube Downloader')
root.geometry('350x200')
root.configure(background='#808080')
root.resizable(False,False)

class Main:

    def __init__(self, master):
        self.master = master

        self.myLabel = Label(master, text='URL:', font=('Lucida Console',12), background='#808080')
        self.myLabel.place(x=50, y=60)
        self.urlString = Entry(width=30)
        self.urlString.place(x=95, y=60)

        self.download_button = Button(master, text='Download', border=1, font=('Lucida Console', 12), command=self.start_threading)
        self.download_button.place(x=125,y=85)

        self.comit = Label(master, text='', font=('Lucida Console', 12), border=0, background='#808080')
        self.comit.pack(pady=1)

        self.comu = Label(master, text='', font=('Lucida Console', 8), border=0, background='#808080')
        self.comu.place(x=10,y=120)

    def start_threading(self):
        self.test = threading.Thread(target=self.download)
        self.test.start()

    def download(self):
        yt = self.urlString.get()
        try:
            ytPlaylist = pt.Playlist(yt)
            self.comit.config(text='')
#            print(ytSingle.streams.filter(only_audio=True))
#            print(ytSingle.streams.first())
#            ytSingle.streams.get_audio_only().download()
            for video in ytPlaylist.videos:
                self.comu.config(text=f'Downloading>> {video.title}', fg='BLACK')
                video.streams.get_audio_only().download()
        except pt.exceptions.RegexMatchError:
            self.comit.config(text='Puste Pole', fg='RED')
        except KeyError:
            ytSingle = pt.YouTube(yt)
            self.comu.config(text=f'Downloading>> {ytSingle.title}', fg='BLACK')
            ytSingle.streams.get_audio_only().download()
        self.comu.config(text='', fg='BLACK')
        self.comit.config(text='COMPLETE', fg='GREEN')


if __name__ == '__main__':
    Main(root)
    root.mainloop()
