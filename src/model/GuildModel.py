from model.ChannelModel import *
from model.GuildModel import *
from model.EmojiModel import *
from model.MemberModel import *
from model.PermissionsModel import *
from model.RoleModel import *

class GuildModel:

    #Missing in Discord.py
    #Overview -> Notification
    #Overview -> Welcome Channel
    #Moderation -> Message filter
    #Integration
    #Webhooks
    #Widget
    def __init__(self):
        self.id = None;
        self.name = None;
        self.region = None;
        self.icon = None;
        self.icon_url = None;
        self.afkTimeout = None;
        self.afkChannel  = None;
        self.verificationLevel = None;
        self.mfaLevel = None;
        self.roles = None;
        self.emojis = None;
        self.channels = None;
        self.bans = None;
        self.members = None;


    async def fillFromGuild(self, bot, guild):
        self.id = guild.id;
        self.name = guild.name;
        self.region = guild.region.value;
        self.icon = guild.icon;
        self.icon_url = guild.icon_url;
        self.afkTimeout = guild.afk_timeout;
        self.afkChannel  = guild.afk_channel.id;
        self.verificationLevel = guild.verification_level.value;
        self.mfaLevel = guild.mfa_level;

        self.roles = list();
        for role in guild.roles:
            roleModel = RoleModel();
            roleModel.fillFromRole(role);

            self.roles.append(roleModel.__dict__);

        self.emojis = list();
        for emoji in guild.emojis:
            emojiModel = EmojiModel();
            emojiModel.fillFromEmoji(emoji);

            self.emojis.append(emojiModel.__dict__);

        self.channels = list();
        for channel in guild.channels:
            channelModel = ChannelModel();
            channelModel.fillFromChannel(channel);

            self.channels.append(channelModel.__dict__);

        self.members = list();
        for member in guild.members:
            memberModel = MemberModel();
            memberModel.fillFromMember(member);

            self.members.append(memberModel.__dict__);

        self.bans = list();
        for banMember in await bot.get_bans(guild):
            self.bans.append(banMember.id);
