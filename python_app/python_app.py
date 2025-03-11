from fastapi import FastAPI
import threading
import uvicorn

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'Hello World!'}

def run_api():
    uvicorn.run(app, host='127.0.0.1', port=8000)

if __name__ == '__main__':
    # threading allows the api to run in the background
    threading.Thread(target=run_api).start()
