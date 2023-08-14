from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui
from buttons import clip_button

app_ui = ui.page_fluid(
    ui.include_js("clipboard.min.js"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_ui("clip"),
)


def server(input: Inputs, output: Outputs, session: Session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    @output
    @render.ui
    def clip():
        return clip_button(
            id="clipbtn", label="Copy Text!", clip_text=input.n(), modal=True
        )


app = App(app_ui, server)
