import openai
import os
import json

import textwrap

class MelvinBot():
    def __init__(
        self,
        model, 
        temperature, 
        max_tokens, 
        top_p, 
        frequency_penalty, 
        presence_penalty,
    ):
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.max_tokens = max_tokens

    def completions(self, prompt):
        try:
            response = openai.Completion.create(
                prompt=prompt,
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
            )
            return self._extract_answer(response)

        except Exception as error:
            print(f"Error making completion request: {error}")

    def _extract_answer(self, response):
        text = response['choices'][0].text
        self._print_text(text)
        return text

    def _print_text(self, text):
        LINE_LENGTH = 100
        border = ''
        for x in range(LINE_LENGTH):
            border += '='
        print(f"\n{border}")
        print(f"\033[92m\n{text.lstrip()}\033[00m\n")
        print(f"{border}\n")