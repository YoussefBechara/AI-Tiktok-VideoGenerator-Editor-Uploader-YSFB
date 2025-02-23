import moviepy.editor as mpy
import random
import whisper_timestamped
import time
from folder_management import clear_folder

video_path = r"assets\bg_video.mp4"
music_path = r"assets\bg_music.mp3"
tts_path = r"sounds\output_audio.wav"

video_duration = 62
width = 1080  # 1080
height = 1920  # 1920

def edit_video(video_path=video_path,video_duration=video_duration,music_path=music_path,width=width, height=height, tts_path=tts_path, fps=10,output_dir='output.mp4'):  
    clip = mpy.VideoFileClip(video_path)
    total_duration = clip.duration
    start_time = random.uniform(0, total_duration - video_duration)
    clip = clip.subclip(start_time, start_time + video_duration)

    resized_clip = clip.resize(height=height)

    video_width, video_height = resized_clip.size

    x_center = video_width / 2
    x_start = int(x_center - width / 2)

    cropped_clip = resized_clip.crop(x1=x_start, width=width)

    muted_clip = cropped_clip.set_audio(None)
    music_clip = mpy.AudioFileClip(music_path).set_duration(video_duration)
    music_clip = music_clip.volumex(0.3)
    tts_clip = mpy.AudioFileClip(tts_path).set_duration(video_duration)
    tts_clip = tts_clip.volumex(2)
    audio = mpy.CompositeAudioClip([music_clip, tts_clip])

    # Load the Whisper model
    model = whisper_timestamped.load_model("base")

    # Transcribe the audio
    results = whisper_timestamped.transcribe(model, tts_path)  # Use tts_path instead of "text.mp3"
    # Create subtitles
    start1 = time.time()
    subs = []
    for segment in results["segments"]:
        for word in segment["words"]:
            text = word["text"].upper()
            start = word["start"]
            end = word["end"]
            duration = end - start 

            # Create a TextClip for the word
            txt_clip = mpy.TextClip(txt=text, fontsize=width/10, color='white', stroke_color='black', font='tbf', align='center', stroke_width=width/200).set_duration(duration)
            
            # Create a background clip based on the length of the text
            bg_clip = mpy.ColorClip((int(len(text)*(width/2)), int(height/10)), col=(0,0,0,0)).set_duration(duration)
            
            # Overlay the text clip on the background clip
            final_clip = mpy.CompositeVideoClip([bg_clip, txt_clip.set_position('center')]).set_start(start).set_position(('center', 0.8))
            
            subs.append(final_clip)
    end1 = time.time()
    print(f'subs took {start1-end1}')
    # Overlay the subtitles on the video
    subtitles_clip = mpy.CompositeVideoClip(subs) # Use CompositeVideoClip to combine all the subtitle clips
    final_clip = mpy.CompositeVideoClip([muted_clip, subtitles_clip.set_position('center').set_duration(video_duration)]).set_audio(audio)
    while True:
        try:
            result = final_clip.write_videofile(output_dir, fps=fps)
            break
        except OSError as e:
            print(f"An error occurred: {e}")
    try:
            clear_folder('sounds')
    except Exception as e:
            print(e)

    


if __name__ == '__main__':
    ttsp = r"prolonged_output_audio2.mp3"
    edit_video(fps=24, video_duration=62,tts_path= ttsp) 

