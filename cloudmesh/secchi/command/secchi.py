from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.secchi.Video import Video
from cloudmesh.secchi.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand, banner
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters

class SecchiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_secchi(self, args, arguments):
        """
        ::

          Usage:
                secchi upload [VIDEO] [--training]
                secchi list [VIDEO]
                sechhi delete VIDEOS
                secchi server start
                secchi server stop
                secchi server status
                secchi labelImg install
                secchi labelImg run
                secchi captureImage

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        map_parameters(arguments,
                       'training')

        VERBOSE(arguments)




        if arguments.upload and arguments.training:
            print ("training")


        if arguments.upload:
            filename = arguments.VIDEO
            print ("analyse")
            file = path_expand("~/textfile.txt") #use Pathlib
            v = Video()
            v.upload(file)

        if arguments.captureImage:
            print("capture image from videos for training purpose")

        if arguments.list:
            banner("THis is list command")
            Console.okay("okay")
            print("list")

        return ""


