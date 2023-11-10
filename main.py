from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Memo(BaseModel):
    id: int  # 통신이 문자열만 가능하다고해서 JSON.stringify로 문자열로보내기했는데 왜 숫자로 신호가와서 계속 에러나다가 int로 하니까 실행되는거지???????????????
    content: str


memos = []

app = FastAPI()


@app.post("/memos")
def create_memo(memo: Memo):
    memos.append(memo)
    return '메모 추가 완료'


@app.get('/memos')
def read_memo():
    return memos


@app.put("/memos/{memo_id}")
def put_memo(req_memo: Memo):
    for memo in memos:
        if memo.id == req_memo.id:
            memo.content = req_memo.content
            return '성공했습니다.'
    return '해당 메모는 없습니다.'


@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    # for index, memo이렇게 index랑 값을 같이 쓰려면 뒤 배열에enumerate함수로 감싸줘야함
    for index, memo in enumerate(memos):
        if memo.id == memo_id:
            memos.pop(index)  # POP은 날려버린다는 삭제의미
            return '성공했습니다.'
    return '해당 메모는 없습니다.'


app.mount("/", StaticFiles(directory='static', html=True), name='static')
