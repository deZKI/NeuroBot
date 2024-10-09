from transformers import AutoModelForCausalLM, AutoTokenizer


class NeuralNetwork:
    def __init__(self, model_name: str = "EleutherAI/gpt-neo-1.3B"):
        # Load the GPT-Neo model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_response(self, prompt: str, max_tokens: int = 100):
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")

        # Generate the response from the model
        outputs = self.model.generate(inputs['input_ids'], max_length=max_tokens)

        # Decode the generated response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
