# for predicting dark pattern

# Method 1 : using Gradio web app

from gradio_client import Client

# Create a Gradio client
client = Client("4darsh-Dev/dark_pattern_detector_app_v2")

def find_dark_pattern(sentence):
    result = client.predict(
        text_to_predict=sentence,
        api_name="/predict"
    )
    return result

    



