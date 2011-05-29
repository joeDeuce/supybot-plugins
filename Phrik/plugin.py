###
# Copyright (c) 2010 Joe Langston
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###
# This is an attempt at a plugin for supybot that abuses phrik, the arch bot.
#

import re
import math
import time

import supybot.conf as conf
import supybot.utils as utils
import supybot.ircdb as ircdb
import supybot.ircmsgs as ircmsgs
from supybot.commands import *
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.irclib as irclib

#Some of this really needs to be fixed, but for now, it is what it is...

class Phrik(callbacks.Privmsg):

    def inFilter(self, irc, msg):
        if msg.nick == 'phrik' and msg.args[0] == irc.nick:

            newmessage, sendToChannel = msg.args[1].split('SpLxJ', 1)

            if re.search("RQUASSRQUASS", msg.args[1]):

                newmessage = re.sub("( RQUASSRQUASS)", "", newmessage)
                newmessage = re.sub("[(\:D)(\:P)(\:p)\!\.\,\:\;\(\)\-\[\]\{\}\=\s\?]*$", "", newmessage) + " up my ass!"

            elif re.search("QGETQGET", msg.args[1]):

                newmessage = re.sub("( QGETQGETQGET)", "", newmessage)
                newmessage = re.sub("(\(Said by:).*$" , "", newmessage)

            elif re.search("RRRRQQQQ", msg.args[1]):

                newmessage = re.sub("( RRRRQQQQ)", "", newmessage)

            elif re.search("QQQQQQQQ", msg.args[1]):

                newmessage = re.sub("( QQQQQQQQ)", "", newmessage)

            elif re.search("SSAQRSSAQR", msg.args[1]):

                newmessage = re.sub("( SSAQRSSAQR)", "", newmessage)
                newmessage = re.sub("[(\:D)(\:P)(\:p)\!\.\,\:\;\(\)\-\[\]\{\}\=\s\?]*$", "", newmessage) + " in my ass!"

            elif re.search("UPTHEIRSUPTHEIRS", msg.args[1]):

                newmessage = re.sub("( UPTHEIRSUPTHEIRS)", "", newmessage)
                newmessage = re.sub("[(\:D)(\:P)(\:p)\!\.\,\:\;\(\)\-\[\]\{\}\=\s\?]*$", "", newmessage) + " up their asses!"

            else:

                newmessage = msg.args[1]

            # if msg.args[1] ends with in my ass!
            # newmessage = msg.args[1] #.translate(None, '.!')
            irc.queueMsg(ircmsgs.privmsg(sendToChannel, newmessage))
            # irc.queueMsg(ircmsgs.privmsg('joeDeuce', newmessage))

        return msg

    def outFilter(self, irc, msg):
        return msg

    def rqq(self, irc, msg, args):
        """[nick]

        Retrieves random quote from phrik.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            person = ''
        message = 'echo [rq ' + person + '] RRRRQQQQ SpLxJ' + sendBackTo

        irc.reply(message, to=target, private=True)

    def qq(self, irc, msg, args):
        """<nick>

        Gets last quoted by <nick> from phrik.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            raise callbacks.ArgumentError()
        message = 'echo [q ' + person + '] QQQQQQQQ SpLxJ' + sendBackTo

        irc.reply(message, to=target, private=True)

    def rqqass(self, irc, msg, args):
        """[nick]

        Retrieves random quote from phrik, then outputs response + "in my ass!"
        Now removes trailing punctuation from quotes.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            person = ''
        message = 'echo [rq ' + person + '] SSAQRSSAQR SpLxJ' + sendBackTo

        irc.reply(message, to=target, private=True)

    def qqass(self, irc, msg, args):
        """<nick>

        Retrieves last quote from [nick], then outputs response + "in my ass!"
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            raise callbacks.ArgumentError()
        message = 'echo [q ' + person + '] SSAQRSSAQR SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

    def sget(self, irc, msg, args):
        """<quote number>

        Retrieves quote from phrik, then outputs response minus garbage"
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            quotenum = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            raise callbacks.ArgumentError()
        message = 'echo [qget ' + quotenum + '] QGETQGET SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

    def rqquass(self, irc, msg, args):
        """[nick]

        Retrieves random quote from phrik, then outputs response + "up my ass!"
        Now removes trailing punctuation from quotes.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            person = ''
        message = 'echo [rq ' + person + '] RQUASSRQUASS SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

    def rqqutass(self, irc, msg, args):
        """[nick]

        Retrieves random quote from phrik, then outputs response + "up their asses!"
        Now removes trailing punctuation from quotes.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            person = ''
        message = 'echo [rq ' + person + '] UPTHEIRSUPTHEIRS SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

    def qqutass(self, irc, msg, args):
        """[nick]

        Retrieves last quote from [nick], then outputs response + "up their asses!"
        Now removes trailing punctuation from quotes.
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            person = ''
        message = 'echo [q ' + person + '] UPTHEIRSUPTHEIRS SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

    def qquass(self, irc, msg, args):
        """<nick>

        Retrieves last quote from [nick], then outputs response + "up my ass!"
        """
        calledcommand = msg.args[1].split(' ', 1)[0]
        target = 'phrik'

        if msg.args[0] == irc.nick:
            sendBackTo = msg.nick
        else:
            sendBackTo = msg.args[0]

        try:
            person = msg.args[1].split(calledcommand.join(' '), 1)[1]
        except Exception:
            raise callbacks.ArgumentError()
        message = 'echo [q ' + person + '] RQUASSRQUASS SpLxJ' + sendBackTo
        irc.reply(message, to=target, private=True)

Class = Phrik

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
