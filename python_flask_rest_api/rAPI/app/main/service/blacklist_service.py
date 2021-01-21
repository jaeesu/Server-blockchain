#토큰인증을 통한 로그인, 로그아웃

from app.main import db
from app.main.model.blacklist import BlacklistToken


#blacklist_token 테이블에 token 저
def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        #insert the token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object={
                'status': 'success',
                'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {장
                'status': 'fail',
                'message': e
        }
        return response_object, 200
