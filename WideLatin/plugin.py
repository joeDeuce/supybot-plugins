"""
Idea by Scott Garrett
Plugin written by Joe Langston
Use at your own risk, blah blah blah.
Do whatever you want with it, just don't blame me.
"""

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import re

class WideLatin(callbacks.Privmsg):
    def widen(self, irc, msg, args):
        """<string>
        Widens <string>.
        Idea by wintervenom; Implementation by joeDeuce
        """
        wideOffset = 65248
        text = " ".join(args)
        newtext = ""

        text = re.sub('[^!-~ ]*', '', text)
        lenMessage = len(text)

        for i in range(0,lenMessage):
            if text[i] == " ":
                newtext += "  "
            elif re.match('[^!-~]', text[i]):
                newtext += text[i]
            else:
                newtext += unichr(ord(text[i]) + wideOffset)
        else:
            if newtext != "":
                irc.reply(newtext.encode('utf8'), prefixNick=False)
            else:
                irc.reply("Nah bro, widen it your damn self!", prefixNick=False)

Class = WideLatin

