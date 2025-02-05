import discord
from PIL import Image
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
import os

try:
    import config
    config.token
except ImportError:
    print("No config.py file found")
    exit()
except AttributeError:
    print("No token found in config.py")
    print("Please add your token to config.py")
    exit()
target_image_path = None
output_path = None
bot = discord.Client(intents=discord.Intents.all())
def percent_of(num, per):
    return int(((num/100) * per)//1)
@bot.event
async def on_ready():
    print("Bot is ready")
    
@bot.event
async def on_message(ctx):
    if not ctx.content.startswith("!convert"):
        return
    if not ctx.attachments:
        await ctx.channel.send("No image attached")
        return
    attachment = ctx.attachments[0]
    dir_before = set(os.listdir())
    await attachment.save(attachment.filename)
    dir_after = set(os.listdir())-dir_before
    target_image_path = dir_after.pop()
    speechbubble = Image.open("speechbubble.png")
    image_name = target_image_path.split("/")[-1].split(".")[0]
    target_image = Image.open(target_image_path)
    speechbubble = speechbubble.resize((target_image.width, percent_of(target_image.height, 35)))
    target_image.paste(speechbubble, (0, 0), speechbubble)
    target_image.save(f"{image_name}.gif")
    await ctx.channel.send(file=discord.File(f"{image_name}.gif"))
    os.remove(target_image_path)
    os.remove(f"{image_name}.gif")
    
bot.run(config.token)