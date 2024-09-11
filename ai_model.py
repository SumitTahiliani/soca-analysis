from transformers import GPT2Tokenizer, GPT2Model, pipeline, set_seed

# Load the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

# Create a text generation pipeline using GPT-2
generator = pipeline('text-generation', model='gpt2')

# Set a seed for reproducibility
set_seed(42)

def query_model(prompt, max_length=1024, num_return_sequences=1):
    # Generate text using the GPT-2 pipeline
    generated_responses = generator(
        prompt, 
        max_length=max_length, 
        num_return_sequences=num_return_sequences
    )
    
    # Extract the generated text from the response
    generated_texts = [response['generated_text'] for response in generated_responses]
    
    return generated_texts

# Function to generate AI response
def generate_ai_response(prompt, max_length=512, num_return_sequences=1):
    return query_model(prompt, max_length, num_return_sequences)
