from fastapi import FastAPI
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/get_transcript")
async def get_transcript(videoId: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(videoId)
        text = "\n".join([item["text"] for item in transcript])
        return JSONResponse(content={"transcript": text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
