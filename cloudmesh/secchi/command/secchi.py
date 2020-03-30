from __future__ import print_function

from cloudmesh import shell
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.secchi.video import Video
from cloudmesh.secchi.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand, banner
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
import os

from src.predict import Predict


class SecchiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_secchi(self, args, arguments):
        """
        ::

          Usage:
                secchi upload [VIDEO] [--training][--validate][--predict]
                secchi list [VIDEO]
                sechhi delete VIDEOS
                secchi server start
                secchi server stop
                secchi server status
                secchi labelImg install
                secchi labelImg run
                secchi captureImage
                secchi run [--predict][--training]

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        map_parameters(arguments,
                       'training',
                       'validate',
                       'predict')

        VERBOSE(arguments)




        if arguments.upload and arguments.training:
            # upload training image set to training folder
            print ("training")
        elif arguments.upload and arguments.validate:
            # upload validation image set to validation folder
            print("validation")
        elif arguments.upload and arguments.predict:
            # validate extension and file size. Max size=125 MB
            # upload video file in for prediction.
            file = path_expand(arguments.VIDEO)
            size = os.path.getsize(file)/(1024*1024)
            if size > 100:
                print("Size limit 100MB exceeds. End upload")
            # validate extension:
            else:
                v = Video()
                if(v.validateFileFormat(file,'predict')):
                    # valid format
                    print("format is valid")
                    v.upload(file)


        elif arguments.captureImage:
            print("capture image from videos for training purpose")

        elif arguments.list:
            banner("THis is list command")
            Console.okay("okay")
            print("list")
        elif arguments.run and arguments.predict:
            print("run prediction")
            # check if video file exists in src location
            v = Video()
            file = v.getVideoFile()
            if(file is not None):
                # run predict.py
                # execute predict.py
                print("Hola!")
                # change ENV to ENVTF
                shell.run("C:\\Users\\dmall\\ENVTF1.3\\Scripts\\activate")
                p = Predict()
                p.run

        elif arguments.run and arguments.training:
            print("run training")
        return ""


