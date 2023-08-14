from shiny import ui
from htmltools import TagList


def clip_fun(
    func,
    id,
    label,
    clip_text,
    modal=False,
    **kwargs,
):
    html_attributes = {"data-clipboard-text": clip_text}

    if modal:
        script = f'new ClipboardJS(".btn", {{ container: document.getElementById("{id}") }} ); '
    else:
        script = f'new ClipboardJS(".btn", document.getElementById("{id}") );'

    return TagList(func(id, label, **html_attributes, **kwargs), ui.tags.script(script))


def clip_button(
    id: str,
    label: str,
    clip_text: str,
    modal: bool = False,
    **kwargs,
) -> TagList:
    return clip_fun(
        ui.input_action_button,
        id,
        label,
        clip_text,
        modal=modal,
        **kwargs,
    )


def clip_link(
    id: str,
    label: str,
    clip_text: str,
    modal: bool = False,
    **kwargs,
) -> TagList:
    return clip_fun(ui.input_action_link, id, label, clip_text, modal=modal, **kwargs)
