from transformers import pipeline, set_seed, GPT2Tokenizer, GPT2Model
import torch

# Set manual seed for reproducibility
set_seed(42)

# Load GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Load GPT-2 tokenizer and model for feature extraction
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')

# Function to query the GPT-2 text generation model
def query_model(prompt, max_length=1024, num_return_sequences=5):
    # Generate text responses using the GPT-2 pipeline
    responses = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
    
    # Extract and return the generated texts
    generated_texts = [response['generated_text'] for response in responses]
    return generated_texts

# Function to extract features from a given text using GPT-2 model in PyTorch
def extract_features_from_text(text):
    # Encode the input text using the GPT-2 tokenizer
    encoded_input = tokenizer(text, return_tensors='pt')
    
    # Get the output features from the GPT-2 model
    output = model(**encoded_input)
    
    return output

# Function to generate AI response compatible with the rest of the pipeline
def generate_ai_response(prompt, max_length=1024):
    # Generate and return the first response
    generated_responses = query_model(prompt, max_length)  # Limit max_length to avoid excessive tokens
    return generated_responses[0]
