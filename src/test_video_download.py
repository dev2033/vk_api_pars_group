import youtube_dl


url = "https://vk.com/video_ext.php?oid=-72614618&id=456240590&hash=24036da7" \
      "a7fb8a99&__ref=vk.api&api_hash=16090122009b476561690ec079df" \
      "_GQZTQNZUGQ3DEOA"

try:
    ydl_opts = {"outtml": "post_id"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=False)
        video_duration = video_info["duration"]
        if video_duration > 300:
            print("Видео слишком долгое")
        else:
            print(f"Видео длиться {video_duration} секунд. Сохраняем видео")
            ydl.download([url])
except Exception:
    print("Не удалось скачать видео")
