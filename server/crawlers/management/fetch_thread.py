import threading
import logging
logger = logging.getLogger('crawlers')


class FetchThread(threading.Thread):
    def __init__(self, site, command):
        self.site = site
        self.command = command
        threading.Thread.__init__(self)

    def run (self):
        try:
            if self.command == 'fetch_all':
                self.site.fetch_all()
            elif self.command == 'fetch_updated':
                self.site.fetch_updated()
        except Exception as e:
            logger.error(e)
