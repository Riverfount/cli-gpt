import openai


class MyChatGPT:
    def __init__(
        self,
        api_key: str,
        model: str = 'text-davinci-003',
        max_tokens: int = 1024 * 2,
        temperature: float = 0.9,
    ):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        openai.api_key = self.api_key

    def call_gpt(
        self,
        prompt: str,
        n: int = 1
    ):
        responses = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            n=n,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        return [responses.choices[index].text for index in range(n)]
