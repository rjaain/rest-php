import sys
import time
import logging
import os 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RjEventHandler(FileSystemEventHandler):
	"""Logs all the events captured."""
	def __init__(self,fname):
		super(RjEventHandler,self).__init__()
		self._fname=fname
		
	def on_moved(self, event):
        	super(RjEventHandler, self).on_moved(event)
		what = 'directory' if event.is_directory else 'file'
		print "Moved %s: %s to %s" %(what, event.src_path, event.dest_path)
	
	def on_created(self, event):
        	super(RjEventHandler, self).on_created(event)
                print event.is_directory
                print event.src_path
                print self._fname
	        if event.is_directory == False :
			"""if event.src_path == self._fname :"""
			sz1=os.path.getsize(event.src_path)
			time.sleep(10)
			sz2=os.path.getsize(event.src_path)
			if sz1 == sz2
				print 'File has been created %s' % event.src_path

	def on_deleted(self, event):
        	super(RjEventHandler, self).on_deleted(event)
		what = 'directory' if event.is_directory else 'file'
		print "Deleted %s: %s" % (what,event.src_path)

	def on_modified(self, event):
        	super(RjEventHandler, self).on_modified(event)
	        what = 'directory' if event.is_directory else 'file'
        	print "Modified %s: %s" %(what, event.src_path)

if __name__ == "__main__":
    event_handler = RjEventHandler(fname='potter.txt')
    observer = Observer()
    observer.schedule(event_handler,'.' , recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
