
import ollama
def analyze_image_with_ollama(uploaded_file, model='llama3.2-vision'):
    """
    Analyzes text in the provided image using the Ollama API and returns the structured Markdown response.
    
    Parameters:
    uploaded_file (file-like object): The image file to analyze.
    model (str): The name of the model to use for analysis. Default is 'llama3.2-vision'.

    Returns:
    response (dict): The response from the Ollama API containing the extracted Markdown content.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{
                'role': 'user',
                'content': """Analyze the text in the provided image. Extract all readable content
                            and present it in a structured Markdown format that is clear, concise, 
                            and well-organized. Ensure proper formatting (e.g., headings, lists, or
                            code blocks) as necessary to represent the content effectively.""",
                'images': [uploaded_file.getvalue()]
            }]
        )
        return response.message.content
    except Exception as e:
        return f"Error processing image: {str(e)}"