from threading import Thread

from source.console.Preview import Preview
from source.main.Main import Main

Preview.preview()

MT = Thread(target=Main.init)
MT.start()
