AI TikTok Video Generator, Editor & Uploader (YSFB)
Overview

An automated system that generates, edits, and uploads TikTok videos using AI. This project combines text-to-speech, video editing, and automated uploading capabilities to streamline content creation for TikTok.
Features

    Reddit fact scraping for content generation
    AI-powered text generation using LLM models
    Text-to-Speech synthesis
    Automated video editing and composition
    Direct TikTok upload integration
    MEGA cloud storage integration
    Folder management system

Prerequisites

    Python 3.8 or higher
    Git
    FFmpeg installed and added to system PATH
    TikTok account
    MEGA account (optional, for cloud storage)

Detailed Installation Guide
1. System Setup
Windows:
bash

# Install FFmpeg
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the archive
3. Add FFmpeg's bin folder to System Environment Variables PATH
4. Verify installation: ffmpeg -version

Linux/Ubuntu:
bash

# Install FFmpeg
sudo apt update
sudo apt install ffmpeg
ffmpeg -version

macOS:
bash

# Using Homebrew
brew install ffmpeg
ffmpeg -version

2. Project Setup
bash

# Clone the repository
git clone https://github.com/YoussefBechara/AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB.git
cd AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

3. Component Configuration
TikTok Authentication:
bash

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

Project Structure
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

Usage

    Configure your settings in each component
    Run the main script:

bash

python main.py

Configuration Options
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

Troubleshooting
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

License

This project is licensed under MIT License
Contributing

    Fork the repository
    Create feature branch
    Commit changes
    Push to branch
    Open pull request

Support

For issues and support:

    Open an issue on GitHub
    Check existing documentation
    Review closed issues for solutions

Disclaimer

Respect TikTok's terms of service and API usage guidelines. This tool is for educational purposes only.
