from Bot import *

from commands.Command import *

from file.GuildFile import *

from model.GuildModel import *

class CopyDiscordCommand(Command):
    def __init__(self, bot):
        Command.__init__(self, bot.config.getDiscordCopyCommand(), bot);


    async def run(self, msg):
        guild = msg.guild;

        guildModel = GuildModel();
        await guildModel.fillFromGuild(self.bot, guild);

        file = GuildFile(self.bot)
        file.saveGuild(guildModel);

        self.bot.log.info("Discord saved");
        await msg.channel.send("Discord copied!");
