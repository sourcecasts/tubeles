# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from pytube import YouTube
from pytube import Stream
import os

class Processor(QObject):    # Main Processor check proxy...
    
    length = QtCore.pyqtSignal(str, str, str)
    receiv = QtCore.pyqtSignal(int)

    def __init__(self, url = None, path = None):    # Main Processor check proxy...
        super().__init__()
                 
        self.url = url
        self.path = path

                
    def running(self):
    
        meta = YouTube(self.url)
        self.length.emit(meta.title, meta.description, meta.thumbnail_url)
        print(meta.title)

    def download(self):
    
        dl = YouTube(self.url, on_progress_callback = self.on_progress)
        dl = dl.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()       
        dl.download(self.path)

           
    def on_progress(self, stream: Stream, chunk: bytes, bytes_remaining: int) -> None:
       
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        percent = round(100.0 * bytes_received / float(filesize), 1)
        self.receiv.emit(percent)
        print(bytes_received, filesize)


   
  