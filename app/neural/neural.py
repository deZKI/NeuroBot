import openai

class NeuralNetwork:
    def __init__(self, api_key: str, model_name: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model_name = model_name

    def generate_response(self, prompt: str, max_tokens: int = 100):
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
