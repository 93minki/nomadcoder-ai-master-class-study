import yt_dlp

url = "https://www.youtube.com/watch?v=wQDHSDvgU54"

ydl_opts = {
    "format": "best[ext=mp4]/best",
    "outtmpl": "./temp.%(ext)s",
    "extractor_args": {
        "youtube": {
            "player_client": ["android"],
        }
    },
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    title = info.get("title", "Unknown")
    print(f"{title} 다운로드 완료")
