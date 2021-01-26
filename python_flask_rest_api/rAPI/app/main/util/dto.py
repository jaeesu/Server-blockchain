#utility 기능
#dto : data transfer object

from flask_restplus import Namespace, fields

#user 데이터를 전달하는 함수

class UserDto:
    api = Namespace('user', description = 'user related operations')
    user = api.model('user',{
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

    #user라는 namespace를 만들고 api 변수 할당
    #api.model -> user 데이터 필드 -> flask 안에서 user 데이터를 담아서 전달할 수 있다.

