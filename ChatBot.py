import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import openai
import pandas as pd
import Globals

class OpenaiChat(object):

    def __init__(self):

        openai.api_key = Globals.CHATGPT_TOKEN

        self.model_engine = "text-davinci-003"


    def Create_Prompt(self, prompt):
        completion = openai.Completion.create(
        engine=self.model_engine, 
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.9,
        )

        response = completion.choices[0].text

        return response

