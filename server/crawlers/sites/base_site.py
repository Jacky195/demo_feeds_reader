class BaseSite(object):

    @classmethod
    def save_feed(cls, feed):
        raise NotImplementedError()

    def fetch_all(self):
        raise NotImplementedError()
