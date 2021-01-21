#user 테이블 생성 후, user 처리에 대한 기능 생성

#1.새로운 user 생성
#2.등록된 user의 public_id 확인
#3.등록된 모든 user 불러오기

import uuid
import datetime

from app.main import db
from app.main.model.user import User

#신규 유저 추가, email 중복확인
def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
                public_id=str(uuid.uuid4()),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow()
            )
        save_changes(new_user)
        response_object={
            'status': 'success',
            'message': 'Successfully registered.'
         }
        return response_object, 201

    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
         }
        return response_object, 409

#모든 user의 정보를 불러오는 기능
def get_all_users():
    return User.query.all()

#public_id를 조회해서 user 정보를 불러옴
def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

#user 데이터 저장
def save_changes(data):
    db.session.add(data)
    db.session.commit()

