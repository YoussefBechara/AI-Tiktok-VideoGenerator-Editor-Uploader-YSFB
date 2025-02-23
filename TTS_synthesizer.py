from TTS.api import TTS
import numpy as np
import soundfile as sf
from setup import get_credential
from pydub import AudioSegment
from pydub.silence import split_on_silence
import subprocess

text = "My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment.My 28 year old sister gave birth to her first daughter 2 weeks ago. I 17f was in the hospital together with my parents and her husband. The birth went pretty smooth, although she was screaming so loud.. I was so excited to be an auntie and holding my newborn niece in my arms was a precious moment."
ex_output_file = 'output_audio.wav'
ex_prolonged_path = 'output_audio_prolonged.mp3'
model_path = "tts_models/multilingual/multi-dataset/xtts_v2"

def join_multiple_wav_files(list_of_audio_paths, output_path):
        # Initialize an empty AudioSegment to hold the combined audio
        combined_audio = AudioSegment.empty()
        
        # Loop through each audio file path and concatenate the audio
        for wav_path in list_of_audio_paths:
            audio_segment = AudioSegment.from_wav(wav_path)
            combined_audio += audio_segment
        
        # Export the combined audio to a new wav file
        combined_audio.export(output_path, format="wav")
        
        print(f"Combined audio saved to {output_path}")

def split_text(text):
    result = []
    while len(text) > 249:
        split_index = text[:249].rfind('.')
        if split_index == -1:
            split_index = 249
        result.append(text[:split_index + 1])
        text = text[split_index + 1:].lstrip()
    if text:
        result.append(text)
    return result

def remove_silences(audio_path, min_silence_len=20, silence_thresh=-45):
    audio = AudioSegment.from_file(audio_path, format="mp3")
    
    # Split audio on silences
    audio_chunks = split_on_silence(
        audio, 
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )
    
    # Concatenate non-silent chunks with short fades
    cleaned_audio = AudioSegment.empty()
    for chunk in audio_chunks:
        cleaned_audio += chunk.fade_in(10).fade_out(10)
    
    return cleaned_audio, audio.frame_rate * audio.frame_width * 8

def improve_audio(output_dir):
    data, samplerate = sf.read(output_dir)

    # Calculate the duration of the silence needed
    duration_of_silence = max(0, 62 - len(data) / samplerate)

    # Calculate the number of samples of silence needed
    silence = np.zeros(int(duration_of_silence * samplerate))

    # Append the silence to the end of the audio
    prolonged_data = np.concatenate([data, silence])

    # Save the prolonged audio
    sf.write(output_dir, prolonged_data, samplerate)
    
    cleaned_audio, original_bitrate = remove_silences(output_dir)
    cleaned_audio.export(output_dir, format="mp3", bitrate=f"{original_bitrate}k")

def generate_cloned_tts(text=text, output_dir=ex_output_file):
    if get_credential('gpu usage (True or False)') == 'True':
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
    elif get_credential('gpu usage (True or False)') == 'False':
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

    list_of_splitted_text = split_text(text)
    out_list = []
    for i in range(len(list_of_splitted_text)):
        out_list.append(f'{output_dir[:-4]}{i}.wav')
    for i in range(len(list_of_splitted_text)):
        tts.tts_to_file(text=list_of_splitted_text[i],
                        speaker_wav=get_credential("speaker_wav_path"),
                        language="en",
                        file_path=out_list[i],
                        split_sentences=False)
    print(f"Speech synthesized and saved to '{output_dir}'")
    
    join_multiple_wav_files(out_list, output_dir)

    improve_audio(output_dir)
    
def generate_tts(model_path="tts_models/en/vctk/vits", text=text, output_dir=ex_output_file, prolonged_path=ex_prolonged_path):
    subprocess.run(['tts', '--text', str(text), '--model_name', model_path, '--out_path', output_dir, '--speaker_idx', 'p230'])
    print(f"Speech synthesized and saved to '{output_dir}'")
    audio = AudioSegment.from_wav(output_dir)
    audio.export(output_dir, format="mp3")
    print(f"Audio converted and saved to '{output_dir}'")
    data, samplerate = sf.read(output_dir)
    duration_of_silence = max(0, 62 - len(data) / samplerate)
    silence = np.zeros(int(duration_of_silence * samplerate))
    prolonged_data = np.concatenate([data, silence])
    sf.write(output_dir, prolonged_data, samplerate)
    improve_audio(output_dir)
    
if __name__ == '__main__':
    generate_cloned_tts("It took me a long time to develop a voice, and now that I have it I'm not going to be silent.")
