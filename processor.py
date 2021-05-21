# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from pytube import YouTube
from pytube import Stream
import youtube_dl
import os

class Processor(QObject):    # Main Processor check proxy...
    
    length = QtCore.pyqtSignal(str, str, str)
    receiv = QtCore.pyqtSignal(int)

    def __init__(self, title = None, url = None, path = None):    # Main Processor check proxy...
        super().__init__()
        
        self.title = title
        self.url = url
        self.path = path

                
    def running(self):
        dl = youtube_dl.YoutubeDL()
        result = dl.extract_info(self.url, download=False)
        if 'entries' in result:
            video = result['entries'][0]
        else:
            video = result

        video_title = video['title']
        video_description = video['description']
        video_thumbnail = video['thumbnail']
        video_url = video['webpage_url']

        self.length.emit(video_title, video_description, video_thumbnail)
        print(video_thumbnail)


    def download(self):
        dl_options = {'format': 'best', 'outtmpl': self.path + "/" + self.title + ".mp4", 'progress_hooks': [self.progress]}
        with youtube_dl.YoutubeDL(dl_options) as dl:
            dl.download([self.url])


    def progress(self, percent):
        if percent['status'] == 'downloading':
            result = round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1)

            print(round(percent['downloaded_bytes'] / percent['total_bytes'] * 100, 1))
            self.receiv.emit(result)


           
    def on_progress(self, stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
       
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        self.receiv.emit(percent)
        print(bytes_received, filesize)


   
  