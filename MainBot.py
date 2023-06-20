import discord
from discord import app_commands
import Globals
import requests
import time
import os
from ChatBot import OpenaiChat
from Upscale import ImageUpscale
from snowflake import SnowflakeGenerator
from discord import Attachment
import random
import io


gen = SnowflakeGenerator(42)
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
Chat = OpenaiChat()
image_upscale = ImageUpscale()


scaleby = 10  #Default scale which will be set on start of the bot


#Event which is triggered if the bot is ready to go

@bot.event
async def on_ready():

    await tree.sync(guild=discord.Object(id=Globals.SERVER_ID))

    print(f'We have logged in as {bot.user}')



#Event which is triggered when a message is send

@bot.event
async def on_message(message):

    #If the message was created by the bot it will return

    if message.author == bot.user:
        return
    
    # If the message doesnt contain Components the U1 to U4 buttons will be pressed(if these are contained in the message)

    if message.components != []:

        await click_button(message, ["U1", "U2", "U3", "U4"])



#Command to create a picture by sending the prompt to chatGPT beforehand. If no prompt is given a picture of food is created

@tree.command(name = "create_gpt_picture", description = "Create pictures by providing a prompt or using the dafault one and sending it to chatGPT!", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def create_gpt_picture(interaction, prompt : str ="Create one description of a food picture inspired by the following description. Instead of a croissant use any type of food or dish and write it at the beginnig in (): Golden croissant, whimsical layers, delicate mood, rustic props, soft lighting, pastel colors, elegant presentation, shallow depth of field, asymmetric composition, Nikon D850 with 50mm lens, golden hour, in the style of Dominique Ansel, capturing exquisite detail in full HD.", attributes : str=""):

    await interaction.response.defer()

    try:
        imagePrompt = Chat.Create_Prompt(prompt)
        await interaction.followup.send(prompt + " " + attributes, ephemeral=True)
        await ImagineApi(imagePrompt + " " + attributes, interaction.channel_id)
    except:

        await interaction.followup.send(prompt + "\n Error, pleas try again later!", ephemeral=True)



#Command to creat a picture of a cerain prompt. The prompt is needed

@tree.command(name = "create_picture", description = "Create pictures by providing a prompt!", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def create_picture(interaction, prompt : str, attributes : str=""):

    await interaction.response.defer()

    try:
        await interaction.followup.send(prompt + " " + attributes, ephemeral=True)
        await ImagineApi(prompt + " " + attributes, interaction.channel_id)
    except:

        await interaction.followup.send(prompt + "\n Error, pleas try again later!", ephemeral=True)



#Command that asks chatGPT for a random image description and creating a picture of that

@tree.command(name = "random_picture", description = "Create a random picture. You dont have to be creative, ChatGPT for sure is!", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def random_picture(interaction, attributes : str=""):

    await interaction.response.defer()

    prompt = "Create a random Image description of a situation and/or object and/or landscape and/or and/or sifi that needs to be captured. Add things like camera angle, perspective, lighting, zoom, used camera and so on."

    try:
        imagePrompt = Chat.Create_Prompt(prompt)
        await interaction.followup.send(prompt  + " " + attributes, ephemeral=True)
        await ImagineApi(imagePrompt + " " + attributes, interaction.channel_id)
    except:

        await interaction.followup.send("Error, pleas try again later!", ephemeral=True)



#Command to create 3 random hex colors and sendinf them to chatGPT to create a description of these colors

@tree.command(name = "random_color_picture", description = "Create a random picture using random colors!", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def random_color_picture(interaction, attributes : str=""):

    await interaction.response.defer()

    prompt = "Create a random Image description of a situation and/or object and/or landscape and/or and/or sifi using these colors: "+ random_hex() + ", "+ random_hex() + ", " + random_hex() + ". Add things like camera angle, perspective, lighting, zoom, used camera and so on."

    try:
        imagePrompt = Chat.Create_Prompt(prompt)
        await interaction.followup.send(prompt + " " + attributes, ephemeral=True)
        await ImagineApi(imagePrompt + " " + attributes, interaction.channel_id)
    except:

        await interaction.followup.send("Error, pleas try again later!", ephemeral=True)



#Command to upscale any picture. A picture is needed for the command to work.

@tree.command(name = "upscale", description = "Submit a picture to upscale it! (change scale with /set_upscale)", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def upscale(interaction, file: discord.Attachment):

    await interaction.response.defer()

    if isinstance(file, Attachment):
        # Retrieve file data from the Attachment object
        file_data = await file.read()

        # Create a file-like object using the file data
        image_file = io.BytesIO(file_data)

        # Call the UpscaleByX method
        link = image_upscale.UpscaleByX(image_file, scaleby)

        await interaction.followup.send(link + " scaled by: " + str(scaleby), ephemeral=True)
    else:
        # Handle cases where the file is not an Attachment object
        await interaction.followup.send("Error, pleas try again later!", ephemeral=True)
    


#Command to change the scale by which the Upscale command upscales the picture
    
@tree.command(name = "set_upscale", description = "Set the scale the Upscale command should use!", guild=discord.Object(id=Globals.SERVER_ID)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def set_upscale(interaction, scale:int):

    global scaleby

    await interaction.response.defer()

    if scale < 4:
        scaleby = 4
    elif scale > 10:
        scaleby = 10
    else:
        scaleby = scale

    await interaction.followup.send("Set scale to " + str(scaleby) +"x!", ephemeral=True)



#Asyncrone function which is responsible for pressing buttons of a sent message

async def click_button(message, button_label):

    containsU = False

    for action_row in message.components:
        buttons = action_row.children
        for button in buttons:
            if isinstance(button, discord.Button) and button.label in button_label:
                if button:
                    containsU = True
                    header = {
                      'authorization': Globals.ACCOUNT_TOKEN
                    }

                    data = {
                            "type": 3,
                            "guild_id": message.guild.id,
                            "channel_id": message.channel.id,
                            "message_id": message.id,
                            "session_id": 123412341234,
                            "application_id": message.author.id, #the id of the bot to which i want to interact
                            "data": {
                                    "component_type": 2,
                                    "custom_id": button.custom_id
                            }
                    }

                    r = requests.post('https://discord.com/api/v9/interactions', json = data, headers = header)
                    time.sleep(0.5)
    
    if containsU == False and message.attachments != []:
        for attachment in message.attachments:
            await attachment.save(os.getcwd() + "/images/" + attachment.filename, seek_begin=False)
                


#Asyncrone function which calls a http request to the MJ bot to create a picture (/imagine)

async def ImagineApi(prompt, channel_id):

    header = {
        'authorization': Globals.ACCOUNT_TOKEN
        }

    payload = {
        "type": 2,
        "application_id": "936929561302675456",
        "guild_id": Globals.SERVER_ID,
        "channel_id": channel_id,
        "session_id": 123412341234,
        "data": {
            "version": "1118961510123847772",
            "id": "938956540159881230",
            "name": "imagine",
            "type": 1,
            "options": [
                {
                    "type": 3,
                    "name": "prompt",
                    "value": prompt
                }
            ],
            "application_command": {
                "id": "938956540159881230",
                "application_id": "936929561302675456",
                "version": "1118961510123847772",
                "default_permission": True,
                "default_member_permissions": None,
                "type": 1,
                "nsfw": False,
                "name": "imagine",
                "description": "Create images with Midjourney",
                "dm_permission": True,
                "options": [
                    {
                        "type": 3,
                        "name": "prompt",
                        "description": "The prompt to imagine",
                        "required": True
                    }
                ]
            },
            "attachments": []
        },
        "nonce": str(next(gen))
    }
    
    r = requests.post('https://discord.com/api/v9/interactions', json = payload, headers = header)



#function which creates a random hex color value

def random_hex():

    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))
    

bot.run(Globals.BOT_TOKEN)