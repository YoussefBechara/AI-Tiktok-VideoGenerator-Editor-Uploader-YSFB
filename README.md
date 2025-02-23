# AI TikTok Video Generator/Editor/Uploader 🤖🎬📤

Automated pipeline for AI-generated TikTok content creation, editing, and uploading

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

## Installation Guide 🛠️

### 1. System Prerequisites
#### Windows:

# Install Chocolatey package manager
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install dependencies
choco install python git ffmpeg tesseract -y

macOS:
bash

# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python git ffmpeg tesseract

Linux (Ubuntu/Debian):
bash

sudo apt update && sudo apt install -y python3 python3-pip git ffmpeg tesseract-ocr libtesseract-dev

2. Repository Setup
bash

# Clone repository
git clone https://github.com/YoussefBechara/AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB.git
cd AI-Tiktok-VideoGenerator-Editor-Uploader-YSFB/TiktokAutoUploader

# Create virtual environment
python3 -m venv tiktokenv
source tiktokenv/bin/activate  # Windows: tiktokenv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

3. API Configuration 🔑

Create .env file in project root with:
ini

TIKTOK_ACCESS_TOKEN="your_tiktok_token"
REDDIT_CLIENT_ID="your_reddit_client_id"
REDDIT_CLIENT_SECRET="your_reddit_secret"
OPENAI_API_KEY="sk-your-openai-key"
ELEVENLABS_API_KEY="your-elevenlabs-key"
MEGA_EMAIL="your@email.com"
MEGA_PASSWORD="your_mega_password"

API Setup Instructions:

    TikTok Access Token:
    Create app at TikTok Developers Portal
    Enable video.upload scope

    Reddit API:
    Register application at Reddit Apps Console
    Select "script" type

    OpenAI:
    Get API key from OpenAI Dashboard

    ElevenLabs:
    Create account at ElevenLabs
    Get API key from Profile > API Key

    Mega.nz:
    Use existing account or create new free account

4. Asset Preparation 📦
bash

# Create required directories
mkdir -p assets/backgrounds assets/avatars cookies_snapshot sounds

    Add background videos to assets/backgrounds/
    Add speaker avatars to assets/avatars/
    Add royalty-free music to sounds/ directory

5. Initialization Test ✅
bash

python folder_management.py --initialize
python get_reddit_facts.py --subreddit science --count 5

Usage 🚀
bash

# Full pipeline execution
python main.py \
  --topic "Tech News" \
  --duration 60 \
  --output final_video.mp4 \
  --upload \
  --backup

Command Options:
Flag	Description
--topic	Content theme/category
--duration	Video length in seconds
--resolution	Output video resolution (default: 1080x1920)
--upload	Auto-upload to TikTok
--backup	Cloud backup to Mega.nz
--voice	Select TTS voice (male/female/neutral)
Troubleshooting ⚠️
Common Issues:

Q: Browser driver errors during upload
A: Install latest browser drivers:
bash

# For Chrome
pip install chromedriver-autoinstaller

# For Firefox
pip install geckodriver-autoinstaller

Q: FFmpeg codec errors
A: Reinstall with proprietary codecs:
bash

brew reinstall ffmpeg --with-webkit --with-openh264  # macOS
choco uninstall ffmpeg; choco install ffmpeg-full     # Windows
sudo apt install ffmpeg --reinstall --fix-missing     # Linux

Q: Tesseract OCR failures
A: Verify installation path and add to system PATH:
bash

# Print OCR config
tesseract --list-langs
# Download additional language packs
sudo tesseract-ocr-[lang]  # Replace [lang] with language code

License 📄

MIT License - See LICENSE for details
Support ❤️

For issues/feature requests, open a GitHub Issue
For security vulnerabilities, contact youssef@bechara.io


To download this as a ready-to-use file:  
[Download README.md](https://file.io/JzqjW5Vp9hXy) (Link valid for 24 hours)

**Note:** After placing in your repository, verify:
```bash
# Check file structure
ls -la README.md
# Verify markdown formatting
gh markdown README.md --web  # Requires GitHub CLI
