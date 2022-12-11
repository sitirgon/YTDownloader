import pytube as pt
from tkinter import *

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

        self.download_button = Button(master, text='Download', border=1,font=('Lucida Console', 12), command=self.download)
        self.download_button.place(x=125,y=85)

        self.comit = Label(master, text='', font=('Lucida Console',12), border=0, background='#808080')
        self.comit.pack(pady=1)


    def download(self):
        yt = self.urlString.get()
        print(yt)
        try:
            ytSingle = pt.YouTube(yt)
            self.comit.config(text='Single', fg='BLACK')
        except pt.exceptions.RegexMatchError:
            ytPlay = pt.contrib.playlist.Playlist(yt)
            print('Playlist')
            print(ytPlay.length)
            self.comit.config(text='Single', fg='BLACK')
        except KeyError:
            self.comit.config(text='Puste Pole', fg='RED')


if __name__ == '__main__':
    Main(root)
    root.mainloop()
