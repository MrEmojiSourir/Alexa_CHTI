import time
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("-----------------------------------")
    print("Logged in as :", client.user.name)
    print("ID:", client.user.id)
    print("-----------------------------------")
    await client.change_presence(game=discord.Game(name="help:`Alexa aide misote`|By MrEmojiSourir | Fait en python"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content == "ping":
        embed = discord.Embed(title=":ping_pong: **PONG! __TA MERE!__** :middle_finger: ", color=669999)

        await client.send_message(message.channel, embed=embed)
        print("La commande `ping`à était éffectuer par:", message.author)

    elif message.content == "Alexa":
        await client.send_message(message.channel, "Tu veux te battez?")
        print("La commande `Alexa`à était éffectuer par:", message.author)

    elif message.content == "Alexa quel temps fait-il ?" or message.content == "Alexa temps":
        embed = discord.Embed(title="T'as qu'à mettre ton cul dehors et aller voire!", color=669999)

        await client.send_message(message.channel, embed=embed)
        print("La commande `Alexa quel temps fait-il ?`à était éffectuer par:", message.author)

    elif message.content == "Alexa pourquoi tu fais pas ce que je dis":
        embed = discord.Embed(title="Car chui pas ta chienne!", color=669999)

        await client.send_message(message.channel, embed=embed)
        print("La commande `Alexa pourquoi tu fais pas ce que je dis`à était éffectuer par:", message.author)


    # `````````````` Commande ``````````````````````
    elif message.content == "Alexa aide misote":
        embed = discord.Embed(title="HELP Alexa_Chti", description="Parodie Alexa Ch'ti", color=0xeee657)

        embed.add_field(name="__**/!\**__INFO__**/!\**__", value="Vous pouvez sois la phrase entière comme ``Alexa qu'elle temps fait ils?`` ou ``Alexa temps``", inline=False)
        embed.add_field(name="Alexa temps", value="Alexa qu'elle temps fait ils?", inline=False)
        embed.add_field(name="!help", value="Commande utile", inline=False)

        await client.send_message(message.channel, embed=embed)
        print("La commande `Alexa aide misote`à était éffectuer par:", message.author)

    elif message.content == "!help":
        embed = discord.Embed(title="Les commandes utils du bot", color=0xeee657)

        embed.add_field(name="!servinfo", value="Sert a montrer les info du serveur", inline=False)
        #embed.add_field(name="pong", value="Avoir le ping du bot", inline=False)

        await client.send_message(message.channel, embed=embed)
        print("La commande `!help`à était éffectuer par:", message.author)

    #elif message.content == "pong":
        pingtime = time.time()
        pingms = await client.send_message(message.channel, "Pinging...")
        ping = time.time() - pingtime
        await client.edit_message(pingms, ":ping_pong:  time is `%.01f seconds`" % ping)
        print("La commande `pong`à était éffectuer par:", message.author)

    elif message.content == "!servinfo":
        server = message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)

        if role_length > 50:  # Just in case there are too many roles...
            roles = roles[:50]
            roles.append('>>>> Displaying[50/%s] Roles' % len(roles))

        roles = ', '.join(roles);
        channelz = len(server.channels);
        time = str(server.created_at);
        time = time.split(' ');
        time = time[0];

        join = discord.Embed(description='%s ' % (str(server)), title='Server Name', colour=0xFFFF);
        join.set_thumbnail(url=server.icon_url);
        join.add_field(name='__Owner__', value=str(server.owner) + '\n' + server.owner.id);
        join.add_field(name='__ID__', value=str(server.id))
        join.add_field(name='__Member Count__', value=str(server.member_count));
        join.add_field(name='__Text/Voice Channels__', value=str(channelz));
        join.add_field(name='__Roles (%s)__' % str(role_length), value=roles);
        join.set_footer(text='Created: %s' % time);

        print("La commande `!servinfo`à était éffectuer par:", message.author)
        return await client.send_message(message.channel, embed=join);



client.run("NDY5NTUzODk3Njk0OTUzNTAy.DjJZwQ.Y_nJ02x81k-eAIALqaHn1vTknR8")
