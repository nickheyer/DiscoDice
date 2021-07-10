import discord
import random
from random import sample

TOKEN = "INSERT DISCORD API TOKEN HERE"
keyword = "!r"
  
client = discord.Client()
embed = discord.Embed()

@client.event
async def on_ready():
  print("Bot is ready to party, logged in as {0.user}.".format(client))
 
@client.event
async def on_message(message):
  global keyword
  if message.author == client.user:
    return
  elif message.content.lower().startswith(keyword.lower()):
    try:  
      param_unsplit = message.content.lower()[len(keyword):].strip()
      param_unspace = ""
      for x in param_unsplit:
        if x == " ":
              pass
        else:
              param_unspace += x
      if param_unspace[0].isnumeric() == True:  
        param_split = param_unspace.split("d")
        qty_dice = param_split[0]
        dice_sides = param_split[1]
      elif param_unspace[0] == "d":
        qty_dice = 1
        dice_sides = param_unspace[1:]
      if int(qty_dice) <= 0:
            raise ValueError
      list_of_rolls = []
      for x in range(int(qty_dice)):
        list_of_rolls.append(random.randint(1, int(dice_sides)))
      roller_name = message.author.nick
      if roller_name == None:
        roller_name = message.author.name   
      await message.channel.send(f"{roller_name}'s roll: `{sorted(list_of_rolls, reverse=True)}` Result: `{sum(list_of_rolls)}`")
    except:
      await message.channel.send("Invalid input, try it like this ('!r 20d20' or '!r d30)")  
  elif message.content.startswith("!set keyword"):
    keyword = message.content.strip()[13:]
    await message.channel.send(f"You can roll your dice with '{keyword}'.")
  else:
    return

client.run(TOKEN)