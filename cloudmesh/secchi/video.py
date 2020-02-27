class Video:

    def train(self, video):

        raise NotImplementedError

        # pop up LabelImag
        os.sysmem()

    def analyse(self):
        raise NotImplementedError


    def upload(self, video, kind="analyse"):
        # kind = training
        raise NotImplementedError

    def list(self, name=None):
        # lists videos and tesll us info about them in json format
        # is training
        # images
        # size
        # non = all, if name only that
        raise NotImplementedError

    def download(self, url, destination=None):
        # python requests to download
        # if none put it in cwd/dest
        raise NotImplementedError




