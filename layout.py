import gradio as gr
from ui.handlers import (
    ui_create_collection,
    ui_add_text,
    ui_update_metadata,
    ui_delete,
    ui_search
)


def build_ui():
    with gr.Blocks() as app:

        gr.Markdown("# 🔍 Simple Vector Database (JSON + MiniLM)")

        with gr.Tab("Create Collection"):
            name = gr.Textbox(label="Collection Name")
            create_btn = gr.Button("Create")
            out_msg = gr.Textbox(label="Output")
            out_list = gr.Textbox(label="Collections")

            create_btn.click(
                ui_create_collection,
                inputs=[name],
                outputs=[out_msg, out_list]
            )

        with gr.Tab("Add Text"):
            c_name = gr.Textbox(label="Collection Name")
            text = gr.Textbox(label="Text to Embed")
            add_btn = gr.Button("Add")
            out = gr.Textbox(label="Output")

            add_btn.click(ui_add_text, inputs=[c_name, text], outputs=out)

        with gr.Tab("Update Metadata"):
            ucol = gr.Textbox(label="Collection Name")
            uid = gr.Textbox(label="Record ID")
            utxt = gr.Textbox(label="New Metadata Text")
            btn = gr.Button("Update")
            out = gr.Textbox(label="Output")

            btn.click(ui_update_metadata, inputs=[ucol, uid, utxt], outputs=out)

        with gr.Tab("Delete"):
            dcol = gr.Textbox(label="Collection Name")
            did = gr.Textbox(label="Record ID")
            dbtn = gr.Button("Delete")
            dout = gr.Textbox(label="Output")

            dbtn.click(ui_delete, inputs=[dcol, did], outputs=dout)

        with gr.Tab("Search"):
            scol = gr.Textbox(label="Collection Name")
            squery = gr.Textbox(label="Search Query")
            sk = gr.Number(label="Top K", value=3)
            sbtn = gr.Button("Search")
            sout = gr.Textbox(label="Results", lines=8)

            sbtn.click(ui_search, inputs=[scol, squery, sk], outputs=sout)

    return app
