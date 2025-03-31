from fastapi import FastAPI, Request
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.post("/get_transcript")
async def get_transcript(req: Request):
    data = await req.json()
    video_id = data.get("videoId")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja', 'en'])
        text = "\n".join([seg["text"] for seg in transcript])
        return text
    except Exception:
        return ""
