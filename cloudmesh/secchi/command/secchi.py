from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.secchi.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class SecchiCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_secchi(self, args, arguments):
        """
        ::

          Usage:
                secchi upload VIDEO [--training]
                secchi list [VIDEO]
                sechhi delete VIDEOS
                secchi server start
                secchi server stop
                secchi server status
                secchi labeler install
                secchi labeler run

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        VERBOSE(arguments)




        if arguments.upload and arguments["--training"]:
            print ("training")

        if arguments.upload:
            print ("analyse")


        elif arguments.list:
            print ("list")

        return ""
