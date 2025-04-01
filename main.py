from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 任意：CORSの設定（GASやローカルなど外部から叩くときに必要になることがある）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 必要に応じて制限可能
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_transcript")  # ← FastAPIではこう書きます！
async def get_transcript(videoId: str = None):
    if not videoId:
        return JSONResponse(content={"error": "videoId is required"}, status_code=400)

    try:
        # YouTubeTranscriptAPI を使って字幕取得
        transcript_data = YouTubeTranscriptApi.get_transcript(videoId)
        transcript_text = "\n".join([item["text"] for item in transcript_data])
        return {"transcript": transcript_text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

