import gradio as gr
from gradio_client import Client


DEBUG_MODE = True

MESAGE_HEADER = """
# 🔌👩🏻‍💻  2nd API Demo (Client component)  🔌👩🏻‍💻

Welcome to my simple demonstration of the gradio potential as an API.

This is an evolution of the first API demo. (Nuno-Tome/aPI_demo_client)

It is made of 2 components: An client that requests to a introduced server. This server should respont whith a JSON to a given text.
* Exemple Server: 🔌🌐 [Nuno-Tome/API_demo_server](Nuno-Tome/aPI_demo_server)

**Just write you message and watch it be returned by the server.**   
"""

INPUT_TEXT_DEFAULT = """
Não sou nada.
Nunca serei nada.
Não posso querer ser nada.
À parte isso, tenho em mim todos os sonhos do mundo.
(...)

- Alvaro de Campos, in Tabacaria (Fernando Pessoa)
"""

INPUT_SERVER_DEFAULT = "Nuno-Tome/API_demo_server"


def get_bmc_markdown():
    bmc_link = "https://www.buymeacoffee.com/nuno.tome"
    image_url = "https://helloimjessa.files.wordpress.com/2021/06/bmc-button.png" # Image URL
    image_size = "150" # Image size
    image_url_full = image_url + "?w=" + image_size
    image_link_markdown = f"[![Buy Me a Coffee]({image_url_full})]({bmc_link})"
    full_text = """
                ### If you like this project, please consider liking it or buying me a coffee. It will help me to keep working on this and other projects. Thank you!
                # """ + image_link_markdown
    return full_text

def send_request(input_text, input_server):
    server = Client(input_server) 
    result = server.predict(
        input_text,
        api_name = "/predict"
    )
    return result

with gr.Blocks() as demo:
  
    gr.Markdown(MESAGE_HEADER)
    gr.DuplicateButton()
    gr.Markdown(get_bmc_markdown())
     
    with gr.Row():
        with gr.Column():
            input_text = gr.TextArea(
                placeholder = INPUT_TEXT_DEFAULT,  
                label =  "**Type your message:**",
                lines = 8, 
                value = INPUT_TEXT_DEFAULT
                )
                
            input_server = gr.Textbox(
                lines = 1, 
                placeholder = INPUT_SERVER_DEFAULT, 
                label =  "**Type the server to call:**",
                value= INPUT_SERVER_DEFAULT
                )
        with gr.Column():
            gr.Markdown("**This is your gradio api request response:**")
            out = gr.JSON()  
    btn = gr.Button("Send request to server")
    btn.click(fn = send_request, inputs = [input_text, input_server], outputs = out)
 
demo.launch(share = True)