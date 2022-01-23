from fastapi import FastAPI, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm

import services.content_service as content_service
import services.user_service as user_service
from auth import AuthHandler
from models.content_model import get_content_list
from models.user_model import get_user_by_id
from pydantic_schema import WholeContentRecord

app = FastAPI()

auth_handler = AuthHandler()


# Normally we would break these up with a router  system, but theres only 6

# User routes

@app.post('/register', status_code=201)
def register(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_service.register_user(form_data)


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return user_service.login(form_data)



# Content Routes
@app.get('/getcontent', dependencies=[Depends(auth_handler.auth_wrapper)])
def getcontent(offset: int = 0, limit: int = Query(default=10, le=15)):
    content = get_content_list(offset, limit)
    return content


@app.get('/getwholerecord/', dependencies=[Depends(auth_handler.auth_wrapper)], response_model=WholeContentRecord)
def getwholerecord(content_id):
    content = content_service.assemble_whole_record(content_id)
    return content


@app.post('/updatetitlebyid', dependencies=[Depends(auth_handler.auth_wrapper)])
def updatetitlebyid(content_id, new_title):
    returnable = content_service.change_content_title(content_id, new_title)
    return returnable


@app.get('/aggregated', dependencies=[Depends(auth_handler.auth_wrapper)])
def aggregated(offset: int = 0, limit: int = Query(default=100, le=1000)):
    return content_service.aggragate_the_data(offset, limit)
