import os
from dotenv import load_dotenv
import replicate



class ImageUpscale(object):

    def __init__(self):

        load_dotenv()

        self.REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')



    def UpscaleByX(self, image, scale=4):

        output = replicate.run(
            "nightmareai/real-esrgan:42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b",
            input={"image": image,        #open(r"C:\Users\leoco\Downloads\0_2.png", "rb")
                   "scale": scale}
        )

        return output