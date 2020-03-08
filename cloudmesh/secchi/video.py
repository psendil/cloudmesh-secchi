import os
import cv2
import shutil
from cloudmesh.common.util import path_expand


class Video:
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    dest = os.path.join(dir_path, 'input')

    def ___init___(self, dest=None):
        # if none put it in cwd/dest
        self.dest = dest

    def train(self, video):

        raise NotImplementedError

        # pop up LabelImag
        os.sysmem()

    def analyse(self):
        raise NotImplementedError


    def upload(self, filepath=None, kind="analyse"):
        # kind = training
        filepath = path_expand("~/testfile.txt")
        print(filepath)
        #path = os.path.join(os.getcwd(),video)
        #path = os.path.expanduser(filename)
        source = path_expand(filepath)

        file = os.path.split(source)[1]
        #os.path.dirname
        #os.path.pathname
        extn = file.split(".")[1]
        if extn in ["mp4", "avi", "txt"]:
            print("supported file format")
            #move file to input folder
            shutil.move(source,self.dest)
        else:
            print("Not a supported video file")
        #raise NotImplementedError

    def list(self, name=None):
        # lists videos and tells us info about them in json format
        # is training
        # images
        # size
        # non = all, if name only that
        # use glob.glob in teh des dir

        # list all files in input folder

        raise NotImplementedError

    def download(self, url, name=None):
        # python requests to download
        # put the file into dest under name, if name is not specified put it in
        # what if file already exists?
        raise NotImplementedError

    def imageCapture(self,input_dir):

        scaling_factorx = 0.5
        scaling_factory = 0.5
        input_archive = 'input_archive/'
        path = 'output/image/'
        files = os.listdir(input_dir)

        for file in files:

            name = file.split(".")

            # cap = cv2.VideoCapture(file)
            cap = cv2.VideoCapture(os.path.join(input_dir, file))

            i = 0
            while (True):
                # Capture frame-by-frame
                ret, frame = cap.read()

                # exit loop after capturing every video file
                if frame is None:
                    break
                # changing frame to gray scale.
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # resizing frame
                resize = cv2.resize(gray, None, fx=scaling_factorx, fy=scaling_factory, interpolation=cv2.INTER_AREA)

                # saving every 100th frame

                if i % 100 == 0:
                    # cv2.imwrite('Img' + str(i) + '.jpg', gray,)
                    cv2.imwrite(os.path.join(path, (name[0] + "_" + str(i // 100) + '.jpg')), gray)
                i += 1
                # Display the resulting frame
                cv2.imshow('frame', resize)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # When everything done, release the capture
            cap.release()

        cv2.destroyAllWindows()
        self.move_to_archive(files, input_dir, input_archive)

    def move_to_archive(self, files, input_dir, dest):

        for file in files:
            shutil.move(input_dir + file, dest)


if __name__== "__main__":
    #print(__import__("Video"))
    v= Video()
    v.upload()


