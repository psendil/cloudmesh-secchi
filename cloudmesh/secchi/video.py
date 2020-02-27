class Video:


    def ___init___(self, dest=None):
        # if none put it in cwd/dest
        self.dest = dest

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
        # use glob.glob in teh des dir
        raise NotImplementedError

    def download(self, url, name=None):
        # python requests to download
        # put the file into dest under name, if name is not specified put it in
        # what if file already exists?
        raise NotImplementedError




