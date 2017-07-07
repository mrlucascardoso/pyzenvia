import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


class MyHandler(FileSystemEventHandler):

    def dispatch(self, event):
        subprocess.call('clear', shell=True)
        subprocess.call('pytest -xv', shell=True)
        super(MyHandler, self).dispatch(event)



if __name__ == '__main__':
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    observer.schedule(MyHandler(), path=args[1] if args else '.')
    observer.start()
    subprocess.call('clear', shell=True)
    subprocess.call('pytest -xv', shell=True)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
