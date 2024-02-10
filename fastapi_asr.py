import gradio as gr
from fastapi import FastAPI, UploadFile, File, HTTPException
from tempfile import NamedTemporaryFile
import speech_recognition as sr

# Initialize FastAPI
app = FastAPI()

# Initialize SpeechRecognizer
r = sr.Recognizer()

# Define ASR function
def calling_asr(wav_file, lid):
    try:
        with sr.AudioFile(wav_file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language=lid)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Speech Recognition service; {e}"

# Define Gradio interface
def asr_interface(audio_file, lang_id):
# Save uploaded audio file
    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio_path = temp_audio.name
        temp_audio.write(audio_file.read())

        # Perform ASR
        asr_out = calling_asr(temp_audio_path, lang_id)

        # Remove temporary audio file
        temp_audio.close()

        return asr_out

# Define routes for FastAPI
@app.post("/asr/")
async def perform_asr(lang_id: str, audio_file: UploadFile = File(...)):
    try:
        asr_out = asr_interface(audio_file.file, lang_id)
        return {"asr_out": asr_out}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Launch FastAPI server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)