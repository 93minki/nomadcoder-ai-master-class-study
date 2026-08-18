import yt_dlp


def extract_video():
    url = "https://www.youtube.com/watch?v=C35GV1MtJco"

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


if __name__ == "__main__":
    extract_video()
