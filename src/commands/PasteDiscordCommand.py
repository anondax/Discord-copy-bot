from commands.Command import *

from files.ConfigFile import *

class PasteDiscordCommand(Command):
	def __init__(self, bot):
		Command.__init__(self, bot.config.getDiscordPasteCommand(), bot);


	async def run(self, msg):
		pass;
