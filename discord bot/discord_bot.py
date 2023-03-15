
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} 起動しました Discord!')

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 1085540047593414698:  # リアクションをつけたメッセージのIDを指定
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        target_role1 = guild.get_role(1078716552691585114)
        target_role2 = guild.get_role(1078716625588596797)   # 男の子
        channel_name =f"{member.name}の部屋"
        category = guild.get_channel(1085538630640078848)

        # すでにプライベートチャンネルを持っている場合は既存のチャンネルを表示する
    for channel in category.text_channels:
       if channel.name == channel_name and member in channel.members:
         await channel.send(f'{member.mention} あなたは既に作成しています。')
         
         return


        # リアクションを押したユーザーが target_role1 を持っていた場合、target_role2 が新しいチャンネルにアクセスできる
    if target_role1 in member.roles:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                target_role1: discord.PermissionOverwrite(read_messages=False),
                target_role2: discord.PermissionOverwrite(read_messages=True),
                member: discord.PermissionOverwrite(read_messages=True)
            }
        # リアクションを押したユーザーが target_role2 を持っていた場合、target_role1 が新しいチャンネルにアクセスできる
    elif target_role2 in member.roles:
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(read_messages=True),
                target_role1: discord.PermissionOverwrite(read_messages=True),
                target_role2: discord.PermissionOverwrite(read_messages=False),
                member: discord.PermissionOverwrite(read_messages=True)
            }
        # それ以外の場合は処理を終了する
    else:
            return

        # チャンネルを作成する
         
    new_channel = await guild.create_text_channel(name=channel_name, overwrites=overwrites, category=category)



        # チャンネルにメッセージを送信する
    await new_channel.send(f'{member.mention} さんの部屋が作成されたよ')

        # リアクションを押したユーザーにはチャンネルにアクセスする権限を付与する
    await new_channel.set_permissions(member, read_messages=True)

bot.run('MTA4NTE4NzgyMTY1ODE4NTc1OA.GPrcva.iW8wzPlTaX-Q_KiMFhsfTuxLCYld7gTTrmNkzM')
