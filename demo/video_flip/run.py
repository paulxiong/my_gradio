import gradio as gr


def video_flip(video):
    return video


demo = gr.Interface(video_flip, gr.Video(), "playable_video")

if __name__ == "__main__":
    demo.launch()
