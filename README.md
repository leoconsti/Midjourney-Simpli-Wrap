# Midjourney-Simlpi-Wrap

Welcome to the Midjourney-Simply-Wrap documentation! This bot allows users to interact with the Midjourney Bot and generate image descriptions using ChatGPT. Below you will find information about the fundamentals and the available commands and their usage.

Midjourney-Simlpi-Wrap is an all-in-one bot that brings your imaginative prompts to life with stunning visuals. With the power of **Midjourney and ChatGPT**, it effortlessly generates captivating images based on your prompts, unlocking a world of creativity at your fingertips. Every image is automatically upscaled to four large versions. Want to go even bigger? With the '**Replicate**' feature, you can further upscale the images to amplify their impact.


## Requirements

To get started with Midjourney-Simpli-Wrap, ensure you have the following:

- ChatGPT API authentication Token
- Midjourney subscription account
- Replicate authentication Token

Make sure to run the MainBot.py file and provide the relevant data in .env and Globals.py files.


## Command List:

### * /create_picture [prompt]

Description: This command takes a prompt as a variable and directly sends it to the Midjourney Bot. It allows you to be creative and think of a good description for an image.

Usage: **/create_picture [prompt]**

Example: **/create_picture Cat with space helmet sitting on rock floating in space, dark, low light, realistic, 32k**

Result:

![image](https://github.com/leoconsti/Midjourney-Simpli-Wrap/assets/82519358/8099e726-6689-4338-a7a3-f89ed1f988de)



### * /create_gpt_picture [prompt] [attribute]

Description: This command takes a prompt as a variable and sends it to ChatGPT, a GPT-2 language model. The returned description from ChatGPT is then sent to the Midjourney Bot, which generates an image based on the description. You can also include additional attributes to refine the generated description, such as aspect ratio, using the attribute parameter.

Usage: **/create_gpt_picture [prompt] [attribute]**

Example: **/create_gpt_picture Create a image description of a big and modern spacestation floating in space.**

Returned description: A gigantic space station, modern and luminous, is floating in the vast darkness of space. Made of hundreds of interconnected modules, it is surrounded by various spacecraft, its metallic surface reflecting light from the stars. The view is breathtaking, with the station covering the whole screen.

Result:

![image](https://github.com/leoconsti/Midjourney-Simpli-Wrap/assets/82519358/dff5af3f-add0-43a2-90ae-96be766cc410)



### * /random_picture [attribute]

Description: This command generates a random image description using ChatGPT. The optional attribute parameter can be used to modify certain attributes of the generated description, such as changing the aspect ratio using "--ar 16:9".

Usage: **/random_picture [attribute]**

Example: **/random_picture --ar 16:9**



### * /random_color_picture [attribute]

Description: This command generates three random colors and uses ChatGPT to create a random image description based on those colors. You can optionally provide attributes, such as aspect ratio, using the attribute parameter.

Usage: **/random_color_picture [attribute]**

Example: **/random_color_picture --ar 16:9**



### * /upscale [file]

Description: This command scales up an image. You need to provide the image file as an attachment when using this command.

Usage: **/upscale [file]**

Example: **/upscale image.jpg**



### * /set_upscale [scale]

Description: This command sets the value by which the image will be upscaled when using the /upscale command. The scale parameter can be set from 4 to 10.

Usage: **/set_upscale [scale]**

Example: **/set_upscale 6**

Result: **The upscale value will be set to 6, and future use of the /upscale command will upscale images by a factor of 6.**

**Note:** Please ensure that the image file provided for the /upscale command is in a compatible format (e.g., JPEG, PNG) and adheres to any size restrictions imposed by the bot or Discord platform.



**Note:** After sending either of the above commands, please be patient as it may take a few minutes for the Midjourney Bot to generate the image. Once the image is ready, the Bot will automatically create four upscaled versions of the picture.


## Important Tips:

* **Avoid Overflow: **To ensure proper display of the images, please avoid causing overflow in the channel. Excessive text, emojis, or other large content may disrupt the image display.

* **Be Creative:** When using the /create_picture command, try to come up with engaging and descriptive prompts to get interesting and diverse image results.

* **Specify Image Description with ChatGPT:** You want the ChatGPT model to return an image description specifically! Use the /create_gpt_picture command and provide a prompt that indicates the desired image description.


## Used Modules:
- openai
- pandas
- discord.py
- requests
- snowflake-id
- replicate


### We greatly appreciate your ideas and suggestions!
