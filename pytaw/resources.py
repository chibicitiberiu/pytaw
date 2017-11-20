

class Resource(object):

    def __str__(self):
        return f"<YouTube Resource: {self.id_}>"


class Channel(Resource):

    def __init__(self, id_, title=None, published_at=None):
        self.id_ = id_
        self.title = title
        self.published_at = published_at

    def __str__(self):
        return f"<YouTube Channel: {self.id_} '{self.title}'>"


class Video(Resource):

    def __init__(self, id_, title=None, published_at=None):
        self.id_ = id_
        self.title = title
        self.published_at = published_at

    def __str__(self):
        return f"<YouTube Video: {self.id_} '{self.title}'>"
