import sys
import time

import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/preet/Downloads"              
to_dir = "C:/Users/preet/Desktop/Downloaded_Files" 



class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hey,{event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"hey, someone modified {event.src_path}!")

    def on_moved(self, event):
        print(f"hey,{event.src_path} has been moved to a different folder")


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

