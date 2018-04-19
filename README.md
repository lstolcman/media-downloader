# media-downloader
![https://i.imgur.com/7YJLtR4.png](https://i.imgur.com/7YJLtR4.png)
## Description

Simple frontend to ![youtube-dl](https://github.com/rg3/youtube-dl) created because none of popular sites are able to simply download audio/video/subtitles from youtube and/or other websites, suggesting instead to download full-of-adware programs. This is not funny nor fast so I've created this small flask-app ;)

## Requirements

- Python 3
- Pip
- virtualenv

## Installation

Chain of commands:

```bash
python3 -m venv venv
venv\Scripts\activate # in Windows
source venv\bin\activate # in Linux
pip install --upgrade pip
pip install -r requirements.txt
```

## Basic usage
```bash
python main.py
```

### Enabling production mode
```
export ENV=prod #Linux
set ENV=prod #Windows
```
and additionally edit `config/prod.py`

