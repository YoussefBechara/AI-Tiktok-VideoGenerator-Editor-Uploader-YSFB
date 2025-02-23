# AI TikTok Video Generator/Editor/Uploader By Youssef Bechara 🤖🎬📤

Automated program for batch AI-generated TikTok content creation, editing, and uploading

## Disclaimer: 
This project was completed by me in Feb2024 but decided to not make it public for business reasons.

# Example output
Watch the example.mp4 in the repository

## Features ✨
- 🧠 AI-powered content generation (LLM models)
- 🎙️ Text-to-Speech synthesis
- 📝 Automated Reddit fact scraping
- ✂️ Intelligent video editing & composition
- ⚡ TikTok API integration for auto-uploading
- ☁️ Mega.nz cloud backup integration

## Requirements 📋
- Python 3.9+
- FFmpeg
- Tesseract OCR
- Chrome/Firefox browser
- 4GB+ free disk space

## API Configuration 🔑
    Run setup.py to create credentials.json file that will automatically store all the credtials in one place and its reusable
    TIKTOK_ACCESS_TOKEN="your_tiktok_token"
    REDDIT_CLIENT_ID="your_reddit_client_id"
    REDDIT_CLIENT_SECRET="your_reddit_secret"
    OPENAI_API_KEY="sk-your-openai-key"
    ELEVENLABS_API_KEY="your-elevenlabs-key"
    MEGA_EMAIL="your@email.com"
    MEGA_PASSWORD="your_mega_password"

## API Setup Instructions:
    Reddit API:
    Register application at Reddit Apps Console
    Select "script" type

    OpenAI API for whisper:
    Get API key from OpenAI Dashboard

    Coqui TTS:
    install coqui TTS module 
    
    Mega.nz:
    Use existing account or create new free account

# Asset Preparation 📦
    Prepare a high quality background video that you will be showing (put it in assets folder) 
    Prepare a .wav clean longa udio of the voice you want to clone (optional theres another option than cloning)
    Prepare background music (put it in assets folder)

# Detailed Installation Guide

## Install FFmpeg
    1. Download FFmpeg from https://ffmpeg.org/download.html
    2. Extract the archive
    3. Add FFmpeg's bin folder to System Environment Variables PATH
    4. Verify installation: ffmpeg -version

### Linux/Ubuntu:
    sudo apt update
    sudo apt install ffmpeg
    ffmpeg -version

### Using Homebrew
    brew install ffmpeg
    ffmpeg -version

## Project Setup

### Clone the repository
    git clone https://github.com/YoussefBechara/AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB.git
    cd AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB

## Install dependencies
pip install -r requirements.txt

## Component Configuration
    TikTok Authentication:
    cd TiktokAutoUploader
    python setup.py install

    Login to TikTok through the browser
    Save cookies to the cookies_snapshot directory

LLM Model Setup:

    Open LLM_models.py
    Configure your preferred AI model API keys
    Adjust model parameters as needed

Text-to-Speech Configuration:

    Open TTS_synthesizer.py
    Set up your preferred TTS service credentials
    Configure voice settings

MEGA Storage (Optional):

    Open mega_upload.py
    Enter your MEGA account credentials
    Configure upload preferences

# Project Structure
mipsasm

├── TiktokAutoUploader/    # TikTok upload automation
├── assets/               # Video assets and resources
├── sounds/              # Audio files and music
├── LLM_models.py        # AI language model integration
├── TTS_synthesizer.py   # Text-to-speech functionality
├── folder_management.py # File organization
├── get_reddit_facts.py  # Content scraping
├── main.py             # Main execution file
├── mega_upload.py      # MEGA cloud integration
├── video_editor.py     # Video editing functions
└── video_uploader.py   # Upload management

# Usage

    Configure your settings in each component
    Run the main script:
    python main.py

## Configuration Options
Video Settings

    Adjust video resolution, framerate, and quality
    Modify transition effects
    Configure background music settings

Content Settings

    Set content categories
    Adjust AI generation parameters
    Configure fact filtering options

Upload Settings

    Set upload schedule
    Configure post descriptions
    Manage hashtag preferences

# Troubleshooting
Common Issues:

    FFmpeg Error: Ensure FFmpeg is properly installed and in PATH
    TikTok Login Failed: Clear cookies and try re-authentication
    API Rate Limits: Adjust request timing in settings

Error Resolution:

    Check log files in project directory
    Verify all API keys are valid
    Ensure sufficient system resources

Security Notes

    Store API keys securely
    Use environment variables for sensitive data
    Regularly update dependencies
    Monitor TikTok API usage
    
## Support:
You can support me by contacting me on my email youssefbechara,ap@gmail,com

For issues and support:

    Open an issue on GitHub
    Check existing documentation
    Review closed issues for solutions

# Disclaimer
Respect TikTok's terms of service and API usage guidelines. This tool is for educational purposes only.
