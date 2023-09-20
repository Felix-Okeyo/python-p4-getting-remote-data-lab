import requests  # Import the requests library for making HTTP requests
import json  # Import the json library for working with JSON data

class GetRequester:
  
    def __init__(self, url):
        self.url = url  # Initialize the class with a URL attribute
    
    def get_response_body(self):
        # Method to send an HTTP GET request to the URL and return the response content
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        # Method to load JSON data from the response content obtained from the URL
        response_body = self.get_response_body()
        return json.loads(response_body)
