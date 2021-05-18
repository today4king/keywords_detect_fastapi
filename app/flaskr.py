from flask import Flask

app = Flask(__name__)
with  open('./sample_post') as f:
    test_post = f.read()
with open('./app/SpamWordsCN.min.txt') as f:
    span_words = [line.rstrip() for line in f]
from app.myStringSearch import StringSearch

search = StringSearch()
search.SetKeywords(span_words)
@app.route('/find-first',methods=['POST'])
def find_first():
    is_found = False
    import time
    start_t = time.time()
    f = search.FindFirst(test_post)
    end_t = time.time()
    time_ms = (end_t - start_t) * 1000
    if f:
        is_found = True

    return {"is_found": is_found, "excuted_time": time_ms}