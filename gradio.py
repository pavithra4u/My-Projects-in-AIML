import gradio as gr
import speech_recognition as sr

# Initialize SpeechRecognizer
r = sr.Recognizer()

# Define ASR function
def calling_asr(audio_file, lang_id):
    try:
        with sr.AudioFile(audio_file.name) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language=lang_id)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# Define Gradio interface
def asr_interface(audio_file, lang_id):
    asr_out = calling_asr(audio_file, lang_id)
    return asr_out

# Define inputs and outputs for Gradio interface
inputs = [
    gr.inputs.File(label="Upload Audio File"),
    gr.inputs.Textbox(label="Language ID", placeholder="Enter language ID (e.g., en-US)"),
]
output = gr.outputs.Textbox(label="ASR Output")

#output = gr.outputs.Textbox(label="ASR Output")

# Create Gradio interface
interface = gr.Interface(
    fn=asr_interface,
    inputs=inputs,
    outputs=output,
    title="Speech to Text Conversion",
    description="Upload an audio file to convert speech to text.",
    allow_flagging=False
)

# Launch Gradio interface
interface.launch()