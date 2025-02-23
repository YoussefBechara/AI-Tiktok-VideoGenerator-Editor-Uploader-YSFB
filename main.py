import time
from multiprocessing import Process
from get_reddit_facts import gather_reddit_facts
from TTS_synthesizer import generate_cloned_tts
from video_editor import edit_video
from video_uploader import upload_to_tiktok,upload_to_mega, upload_short
from LLM_models import send_message
from setup import get_credential
import os
import json

def upload_video_process(video_path, title, schedule, choice=['tiktok','youtube'], hashtags='#fyp'):
    if 'tiktok' in choice:
        try:
            upload_to_tiktok(video_path=video_path, schedule=schedule, title=title)
        except Exception as e:
            print(f"Error uploading video {video_path} to tiktok: {e}")
    if 'youtube' in choice:
        try:
            upload_short(file_path=video_path, title=title,description='Interesting Video',tags=hashtags)
        except Exception as e:
            print(f"Error uploading video {video_path} to youtube: {e}")
    if 'mega' in choice:
        try:
            upload_to_mega(file_path=video_path, description=title)
        except Exception as e:
            print(f"Error uploading video {video_path} to mega: {e}")
        
def generate_title_hashtags(facts):
    query = f"""generate me a catchy/hooky title for this video that contains facts so i can put it as a caption for my tiktok video, make it SEO optimized and add 10 hashtags to boost views, here are the facts in the video: {facts}"""
    response = send_message(query, llm='claude')
    title = response.split('"')[1]
    hashtags = []
    for i in range(len(response)):
        hashtag = ''
        if response[i] == '#':
            for c in range(i, len(response)):
                if response[c] == ' ' or response[c] == '\n':
                    break
                hashtag += response[c]
            hashtags.append(hashtag)            
    return title, hashtags

def main():
    start = time.time()
    
    num_of_vids_user_wants = int(input("How many videos do you want to generate?: "))
    num_of_facts_per_vid = int(input("How many facts in each video do you want?: "))
    num_of_vids_already_made = int(get_credential('videos already made'))
    num_of_facts_already_used = num_of_vids_already_made * num_of_facts_per_vid
    num_of_facts_to_get = num_of_facts_per_vid + num_of_vids_user_wants

    # Get reddit stories
    facts = []
    for i in range(num_of_facts_to_get):
        fc_li = gather_reddit_facts(num_of_facts=num_of_facts_per_vid, num_of_facts_to_skip=num_of_facts_already_used)
        facts.extend(fc_li)

    facts_titles = [fact['title'] for fact in facts]
    facts_list = [facts_titles[i:i+num_of_facts_per_vid] for i in range(0, len(facts_titles), num_of_facts_per_vid)]

    end = time.time()
    print(f'Fact gathering process: {end - start}')

    upload_processes = []

    for i in range(num_of_vids_user_wants):
        try:
            facts = facts_list[i]
            facts_in_str = "Did you know that " + ", ".join(facts)
            
            tts_path_wav = f"sounds/output_audio{i+num_of_vids_already_made}.wav"
            tts_path_mp3 = f"sounds/output_audio{i+num_of_vids_already_made}.mp3"
            #tts_path_prolonged = f"sounds/prolonged_output_audio{i+num_of_vids_already_made}.mp3"
            non_absolute_vid_out_path = f"output_videos/video{i+num_of_vids_already_made}.mp4"
            current_path = os.getcwd()
            video_out_path = os.path.join(current_path, non_absolute_vid_out_path)
            
            generate_cloned_tts(text=facts_in_str, output_dir=tts_path_wav)
            edit_video(tts_path=tts_path_mp3, fps=24, width=810, height=1440, video_duration=62, output_dir=video_out_path)
            
            #updating num of vids already made
            with open('credentials.json', 'r') as file:
                data = json.load(file)
            data["videos already made"] = str(num_of_vids_already_made+1)
            with open('credentials.json', 'w') as file:
                json.dump(data, file, indent=4)  # indent=4 is for pretty formatting

            #video_title = f"You won't believe the last fact!! Mind blowing facts part {i+1+num_of_vids_already_made}! #fyp #viral #facts #interesting #mindblowing"
            video_title, video_hashtags = generate_title_hashtags(facts_in_str)
            # Start a new process for uploading the video
            p = Process(target=upload_video_process, args=(video_out_path, video_title, 7200*i,video_hashtags))
            p.start()
            upload_processes.append(p)
            
            print(f"Video {i+1} processing complete. Upload started in background.")
        
        except Exception as e:
            print('Error in video processing:', e)
    
    # Wait for all upload processes to complete
    for p in upload_processes:
        p.join()
    
    print("All videos processed and uploads started.")

if __name__ == "__main__":
    main()