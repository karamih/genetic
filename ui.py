import gradio as gr
from genetic import calculate

demo = gr.Interface(fn=calculate,
                    inputs=['text', gr.Number(), gr.Number(), gr.Number(), gr.Number(),
                            gr.Number(), gr.Number(), gr.Number(), 'text'],
                    outputs=[gr.Number(), gr.Number(), gr.Number()])

demo.launch(debug=True)