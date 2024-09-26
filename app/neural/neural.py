from transformers import pipeline


class NeuralNetwork:
    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        # Инициализация нейросети с использованием предобученной модели
        self.model = pipeline("text-generation", model=model_name)

    def generate_response(self, prompt: str, max_length: int = 100):
        # Генерация ответа на основе входного текста
        response = self.model(prompt, max_length=max_length)
        return response[0]['generated_text']
