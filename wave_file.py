import os
import sys

def get_wav_files(directory):
        wav_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".wav"):
                     file_path = os.path.join(root, file)
                     wav_files.append((file, file_path))
        return wav_files
 # Example usage:
directory_path = "/home/pavithra/Telugu_Interspeech_Task1_Train_labelled_12-08-2021_13-09"
wav_files = get_wav_files(directory_path)
# Print the list of WAV files and their paths
for file_name, file_path in wav_files:
    with open('wave2.txt', 'a') as file:
       #sys.stdout = file
        print(f"{file_name}, {file_path}",file=file)