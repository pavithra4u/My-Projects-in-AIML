# pip install SpeechRecognition
# pip install joblib
import glob
import speech_recognition as sr
import joblib
import os
import sys
r = sr.Recognizer()
wav_path=sys.argv[1]
lang_id=sys.argv[2]

def calling_asr(wav_file,lid):
    AUDIO_FILE=wav_file
    # aud_name=AUDIO_FILE.split('/')[-1].split('.')[0]
    #file=open(wav_path+"/"+aud_name+".txt","w")
    text="cant read wav file"
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language=lid)
        #file.write(aud_name +"\t"+text)
        return text
    except:
        #file.write(" "+"Error in segement"+" ")
        return text
    #file.close()

asr_out=calling_asr(wav_path,lang_id)
print("asr_out",asr_out)




# 'te-IN' for telugu 
# usage python filename.py path to audio file lid
# python capstone_asr.py /home/data/audiofile.wav te-IN



