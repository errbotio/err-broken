from errbot import BotPlugin, botcmd

import borken # fails

class Broken(BotPlugin):
    @botcmd
    def hello(self, mess, args):
        """ this command says hello """
        return 'Hello World !'
