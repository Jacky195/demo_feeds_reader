class BaseSite(object):

    @classmethod
    def save_item(cls, item):
        raise NotImplementedError()

    def fetch_all(self):
        raise NotImplementedError()
