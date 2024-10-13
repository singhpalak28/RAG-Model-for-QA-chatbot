from backend import qa_bot
import gradio as gr

# Function to handle chatbot interaction
def chatbot_interface(query, pdf_file=None, chat_history=[]):
    pdf_status = None
    # If a PDF is uploaded, ingest its content and retrieve relevant documents
    if pdf_file is not None:
        pdf_status, answer = qa_bot(query, pdf_file)
    else:
        # If no PDF is uploaded, just answer the question using general knowledge
        pdf_status, answer = qa_bot(query)

    # Append the new question-answer pair to the chat history
    chat_history.append((query, answer))

    # Return the chat history along with PDF ingestion status (if applicable)
    return chat_history, "", pdf_status

# Gradio interface setup with custom CSS
with gr.Blocks(css=".small-upload-btn .btn {padding: 2px 8px;}") as ui:
    # Set up the header
    gr.Markdown("<h1 align='center'>QA Chatbot</h1>")

    # Display the chat history
    chatbot_output = gr.Chatbot(label="Chat History")

    # Input components: text box for questions, small file uploader for PDF, and submit button
    with gr.Row():
        # Question input box
        question_input = gr.Textbox(
            placeholder="Ask me any question",
            label="Your Question",
            show_label=False,
        )

        # Small PDF upload button
        # Update the File component without 'elem_classes'
        pdf_uploader = gr.File(label="", type="file", show_label=False)


    # Submit button below the question input
    submit_btn = gr.Button(value="Submit", variant="primary")

    # Hidden textbox for managing chat history
    chat_history_state = gr.State([])

    # Status box for PDF ingestion
    pdf_status_box = gr.Textbox(label="PDF Status", placeholder="Upload a PDF to ingest it.", interactive=False)

    # Set the button functionality
    submit_btn.click(
        fn=chatbot_interface,
        inputs=[question_input, pdf_uploader, chat_history_state],
        outputs=[chatbot_output, question_input, pdf_status_box]
    )

# Launch the Gradio interface
ui.launch(server_name="0.0.0.0", server_port=7860)
