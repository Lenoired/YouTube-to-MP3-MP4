# YouTube-to-MP3-MP4
Python script for converting YouTube videos to .mp3 or .mp4. You can also search videos and download them. Pure python implementation (based on the requests module); no other special requirements are needed.
</br></br>
**NOTE:** Default download path is "./" (current script execution path), it is optional to edit it by modifying the variable "location" inside the script.

## Installation

```bash
git clone https://github.com/Lenoired/YouTube-to-MP3-MP4.git youtube-to-mp3 && cd youtube-to-mp3 && python3 youtube.py
```

## Dependencies

| Library | Recommended |
|---------|-------------|
|Python   |>=3.11         |
|Requests |>=2.30.0       |

## Examples


- _Download a video as MP3_
```bash
python3 youtube.py https://youtu.be/dQw4w9WgXcQ mp3
```

- _Download a video as MP4_
```bash
python3 youtube.py https://youtu.be/dQw4w9WgXcQ mp4
```

- _Search a video & download it as MP3_
```bash
python3 youtube.py 'Rick Astley' mp3
```

- _Search a video & download it as MP4_
```bash
python3 youtube.py 'Rick Astley' mp4
```
