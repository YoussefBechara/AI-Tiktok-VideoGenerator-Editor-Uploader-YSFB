import subprocess
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from setup import get_credential
import os
current_path = os.getcwd()
script_path = os.path.join(current_path, 'mega_upload')
def upload_to_mega(file_path, description, email=get_credential("mega_email"), passwor=get_credential("mega_password"),script_path=script_path):
    print('Uploading To MEGA...')
    try:
        subprocess.run([python_interpreter, script_path, email, password, file_path, description], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    print('Successfully uploaded to MEGA !')

def upload_to_tiktok(video_path, username=get_credential("tiktok_repo_username"),  schedule=0, title='', proxy=''):
    start = time.time()
    upload_command = f'python cli.py upload --user {username} -v "{video_path}" -t "{title}" -sc {schedule} '
    subprocess.run(upload_command, shell=True, cwd="C:\\Users\\user\\Desktop\\tiktok_uploader")
    end = time.time()
    print(f'It took {end-start} to upload the video!')

def upload_short(file_path, title, description, tags):
    client_secrets_file = get_credential("youtube_client_secrets_file")
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]

    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_local_server(port=8080)

    youtube = build("youtube", "v3", credentials=credentials)
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False,
        },
    }

    media_file = MediaFileUpload(file_path, resumable=True)

    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    ).execute()

    print(f"Video uploaded successfully. Video ID: {response['id']}")

if __name__ == '__main__':
    choice = input("Where do you want to upload the video? (mega, youtube, tiktok): ")
    
    if choice.lower() == 'mega':
        script_path = r'mega_upload.py'
        python_interpreter = r"C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe"
        email = ''
        password = ''
        file_path = r"C:\Users\user\Desktop\TikTokAiFactsAutomater\output_videos\video0.mp4"
        description = 'Interesting video'
        upload_to_mega(email=email, password=password, file_path=file_path, script_path=script_path, description=description)
    
    elif choice.lower() == 'tiktok':   
        video_path = r"C:\Users\user\Desktop\TikTokAiFactsAutomater\output_videos\video0.mp4"
        title = 'Your Video Title'
        schedule = 3600
        upload_to_tiktok(username='business', video_path=video_path, schedule=schedule, title=title, proxy='http://sfcxovdw:eedrq5ffia67@38.154.227.167:5868')
    
    elif choice.lower() == 'youtube':
        video_file = r"C:\Users\user\Desktop\TikTokAiFactsAutomater\output_videos\video0.mp4"
        video_title = "My YouTube Short"
        video_description = "This is a short video uploaded via the YouTube API"
        video_tags = ["short", "youtube", "api"]
        upload_short(video_file, video_title, video_description, video_tags)