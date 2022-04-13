from datetime import datetime, timedelta
from fastapi import FastAPI, Response
import uvicorn


app = FastAPI()

@app.get("/")
def index():
    now = datetime.utcnow() + timedelta(hours=9)
    return Response(content=now.strftime("%Y-%m-%d %H:%M:%S.%f"))



if __name__ == "__main__":
    uvicorn.run("api:app", debug=True, port=5000, host="0.0.0.0", workers=1)