import discord
from discord.ext import commands
import os
import json

crusty = commands.Bot(command_prefix='+')

@crusty.command()
async def hello(ctx):
  await ctx.send('Привет!')

@crusty.command()
async def clear( ctx, amount : int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.purge(limit = amount)
    await ctx.send(embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщений(я)'))

@crusty.event
async def on_server_join(server):
    activity = discord.Game(name="cr!help | {len(guilds)} серверов.", type=3)
    await crusty.change_presence(status=discord.Status.idle, activity=activity)

@crusty.command()
async def info(ctx):
    embed = discord.Embed(
        title = '**Информация о боте. <:discord_bot_dev:845942679904845854>**',
        description = '''Название бота: **Crusty**
Хостинг: **Heroku** <:heroku:845934460855386123>
Пинг: **В разработке...**
Сокет: **18ms**
ЯП: Python <:python:845935931030372372>
Python3.9 Web
DiscordPY19.3.1
Префикс: `cr!` 
Алиасы: `10` (cr!aliases в разработке)''',
        colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)

@crusty.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
  
@crusty.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Информация о сервере",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Владелец", value=owner, inline=True)
  embed.add_field(name="Айди сервера", value=id, inline=True)
  embed.add_field(name="Регион", value=region, inline=True)
  embed.add_field(name="Количество участников", value=memberCount, inline=True)

  await ctx.send(embed=embed)

@crusty.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует!**', color=0x0c0c0c))

@crusty.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)

@crusty.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason):
    channel = Bot.get_channel(789968921432031272)
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=0)
    emb = discord.Embed(color=344462)
    emb.add_field(name='✅ Ban пользователя', value='Пользователь {} был забанен!'.format(member.mention))
    await channel.send(embed = emb)

@crusty.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    channel = Bot.get_channel(789968921432031272)
    banned_users = await ctx.guild.bans()
    await ctx.channel.purge(limit=0)

    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        emb = discord.Embed(color=344462)
        emb.add_field(name='✅ UnBan пользователя', value='Пользователь {} был разбанен.'.format(member))
        await channel.send(embed = emb)
        return

@crusty.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, reason):
 await ctx.send("Изгоняем участника {0} по причине: {1}".format(member, reason))
 await member.kick(reason=f'{ctx.author} Выгнал {member}')

@crusty.command()
async def commds(ctx):
    embed = discord.Embed(
        title = 'Все команды бота:',
        description = '''**Привет, я бот Crusty. Вот все мои команды**



**Модерирование**
`ban`, `kick`, `clear`, `say`.



**Утилиты**
`clear`, `info`, `serverinfo`, `avatar`.


**Системные команды**

`say`, `clear`.

*Команды в доработке...*

**[Поддержать(Донат)](https://www.donationalerts.com/r/frame11)''',
        colour = discord.Colour.from_rgb(106, 192, 245)
    )
    await ctx.send(embed=embed)
    
@crusty.command()
async def say(ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}')

@crusty.command(name='dm',pass_context=True)
async def dm(ctx, *argument):
    #creating invite link
    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
    #dming it to the person
    await ctx.author.send(invitelink)



token = os.environ.get('BOT_TOKEN')

crusty.run(str(token))
