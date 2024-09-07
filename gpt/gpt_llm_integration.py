import openai

# Replace with your API key
openai.api_key = "your_openai_api_key_here"

def analyze_response(response):
    prompt = f"Analyze the following response for educational insights: {response}"
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        analysis = completion.choices[0].text.strip()
        return analysis
    except Exception as e:
        return f"Error analyzing response: {str(e)}"
