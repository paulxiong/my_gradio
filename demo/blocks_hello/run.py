import gradio as gr
import logging
logging.basicConfig(filename='my_app.log',level=logging.DEBUG)

def update(name):
    # logging.debug('boostx debug ...')
    print('boostx debug ...')
    return f"Welcome to Gradio, {name}!"

demo = gr.Blocks()

with demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    """)
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()
    
    inp.change(fn=update, 
               inputs=inp, 
               outputs=out)

demo.launch()