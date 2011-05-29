import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import output, expect, anything, something, yn
    conf.registerPlugin('WideLatin', True)
    if advanced:
        output("""The WideLatin plugin converts text to cool characters
        """)

WideLatin = conf.registerPlugin('WideLatin')

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
