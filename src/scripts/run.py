import uvicorn

def dev():
    uvicorn.run('src.main:app', reload=True , host='127.0.0.1' ,port=8000)