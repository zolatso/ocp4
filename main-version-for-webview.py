import webview
import os
from model import list_of_players

class Api:
    def say_hello(self):
        return "Hello from Python backend!"
    def get_list_of_players(self):
        return list_of_players()

def get_html_path():
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Path to the HTML file
    return os.path.join(current_dir, 'views', 'index.html')
    

def main():
    api = Api()
    window = webview.create_window(
        'Python Desktop App',
        url=get_html_path(),  # Use local HTML file instead of html string
        js_api=api,
        width=800,
        height=600
    )
    webview.start()

if __name__ == '__main__':
    main()