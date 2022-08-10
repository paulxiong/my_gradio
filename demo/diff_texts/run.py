import os
from difflib import Differ

import gradio as gr
def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    inp = tf.keras.applications.mobilenet_v2.preprocess_input(inp)
    prediction = inception_net.predict(inp).flatten()
    return {labels[i]: float(prediction[i]) for i in range(1000)}


def diff_texts(text1, text2):
    breakpoint()
    d = Differ()
    return [
        (token[2:], token[0] if token[0] != " " else None)
        for token in d.compare(text1, text2)
    ]

image = gr.inputs.Image(shape=(224, 224))
label = gr.Label(num_top_classes=3)
demo = gr.Interface(
    diff_texts,
    [
        gr.Textbox(
            label="Initial text",
            lines=3,
            value="The quick brown fox jumped over the lazy dogs.",
        ),
        gr.Textbox(
            label="Text to compare",
            lines=3,
            value="The fast brown fox jumps over lazy dogs.",
        ),
    ],
    gr.HighlightedText(label="Diff", combine_adjacent=True),
)
demo1 = gr.Interface(
    fn=classify_image,
    inputs=image,
    outputs=label,
    examples=[
        os.path.join(os.path.dirname(__file__), "images/cheetah1.jpg"),
        os.path.join(os.path.dirname(__file__), "images/lion.jpg")
        ]
    )
if __name__ == "__main__":
    # breakpoint()
    demo.launch()
