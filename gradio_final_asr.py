import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
import os

# Initialize SpeechRecognizer
r = sr.Recognizer()

LANGUAGE_MAPPING = {
    "Telugu": "te-IN"
}

# Define ASR function
def calling_asr(audio_file, lang_id):
    try:
        #audio = AudioSegment.from_file(audio_file.name)
        #audio.export("temp.wav", format="wav")
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        language_code = LANGUAGE_MAPPING.get(lang_id, lang_id)
        text = r.recognize_google(audio, language=language_code)
        return text
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        # Clean up temporary WAV file
        if os.path.exists("temp.wav"):
            os.remove("temp.wav")

# Define Gradio interface
def asr_interface(audio_file, lang_id):
    asr_out = calling_asr(audio_file, lang_id)
    return asr_out

# Define inputs and outputs for Gradio interface
inputs = [
    gr.Audio(type="filepath"),
    gr.Textbox(label="Language", placeholder="Enter language  (eg : Telugu)"),
]
output = gr.Textbox(label="ASR Output")

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