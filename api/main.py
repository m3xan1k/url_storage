from time import time
import json
from typing import List

from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import redis

from api.scheme import LinkData
from api.helpers import clean_data, valid_params


app = FastAPI()
r = redis.Redis('redis')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(content={'status': str(exc)},
                        status_code=status.HTTP_400_BAD_REQUEST)


@app.get('/visited_domains', name='domains')
async def get_visited_domains(request: Request) -> JSONResponse:
    _from = request.query_params.get('from')
    to = request.query_params.get('to')
    if not valid_params(_from, to):
        return JSONResponse(content={'status': "'from' and 'to' params invalid"},
                            status_code=status.HTTP_400_BAD_REQUEST)

    stored_data: List[bytes] = r.zrangebyscore('links', min=_from, max=to)
    cleaned_data: List[str] = clean_data(stored_data)
    content = {'domains': cleaned_data, 'status': 'ok'}
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@app.post('/visited_links', name='links')
async def post_visited_links(links: LinkData) -> JSONResponse:
    timestamp = int(time())
    stored_data = json.dumps(links.links)
    r.zadd('links', {stored_data: timestamp})
    return JSONResponse(content={'status': 'ok'},
                        status_code=status.HTTP_201_CREATED)
