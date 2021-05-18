from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in ['http://127.0.0.1:8000']],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
with  open('./sample_post') as f:
    test_post = f.read()
with open('./app/SpamWordsCN.min.txt') as f:
    span_words = [line.rstrip() for line in f]
from app.myStringSearch import StringSearch

search = StringSearch()
search.SetKeywords(span_words)


@app.post("/find-first")
@app.get("/find-first")
async def find_first(text: str):
    is_found = False
    import time
    start_t = time.time()
    f = search.FindFirst(text)
    end_t = time.time()
    time_ms = (end_t - start_t) * 1000
    if f:
        is_found = True

    return {"is_found": is_found, "result": f, "excuted_time": time_ms}


@app.post('find-all')
@app.get('find-all')
async def find_all(text: str):
    is_found = False
    import time
    start_t = time.time()
    fs = search.FindAll(text)
    end_t = time.time()
    time_ms = (end_t - start_t) * 1000
    if fs and len(fs) > 0:
        is_found = True

    return {"is_found": is_found, "result": fs, "excuted_time": time_ms}


@app.post('contains-any')
@app.get('contains-any')
async def contains_any(text: str):
    import time
    start_t = time.time()
    b = search.ContainsAny(text)
    end_t = time.time()
    time_ms = (end_t - start_t) * 1000

    return {"result": b, "excuted_time": time_ms}


@app.post('replace')
@app.get('replace')
async def replace(text: str, replace_char: str = '*'):
    import time
    start_t = time.time()
    text_replaced = search.Replace(text, replace_char)
    end_t = time.time()
    time_ms = (end_t - start_t) * 1000

    return {"result": text_replaced, "excuted_time": time_ms}
