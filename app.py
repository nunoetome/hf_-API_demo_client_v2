import gradio as gr
from gradio_client import Client


DEBUG_MODE = True

MESAGE_HEADER = """
# 🔌👩🏻‍💻  API Demo (Client component)  🔌👩🏻‍💻


Welcome to my simple demonstration of the gradio potential as an API.

It is made of 2 components: *API_demo_server* and *API_demo_client*.

* Server component: 🔌🌐 [Nuno-Tome/API_demo_server](Nuno-Tome/aPI_demo_server)

* Client component: 🔌👩🏻‍💻 [Nuno-Tome/API_demo_client](Nuno-Tome/aPI_demo_client)

**Just write you message and watch it be returned by the server.**   
                
"""


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

   
def send_request(text):
    client = Client("Nuno-Tome/API_demo_server")
    result = client.predict(
        text,
        api_name="/predict"
    )
    return result

with gr.Blocks() as demo:
  
    gr.Markdown(MESAGE_HEADER)
    gr.DuplicateButton()
    gr.Markdown(get_bmc_markdown())
     
    with gr.Row():
        with gr.Column():
            gr.Markdown("**Type your message:**")
            inp = gr.TextArea(placeholder="What is your name?")
        with gr.Column():
            gr.Markdown("**This is your gradio api request response:**")
            out = gr.JSON()  
    btn = gr.Button("Send request to server")
    btn.click(fn=send_request, inputs=inp, outputs=out)
 
demo.launch(share=True)