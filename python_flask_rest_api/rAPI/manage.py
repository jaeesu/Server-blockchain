#API 서버의 entry point
#user 테이블까지 만들고 User_Controller, blueprint를 이용해 swagger를 실행 -> 데이터 입력 및 출력

import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint    #blueprint 모듈 추가
from app.main import create_app, db
from app.main.model import user, blacklist     #db 작성 후, import 해주기  #blacklist추가
#blacklist 추가 후, db를 변경했으니 migrate와 upgrade 명령을 실행해줌

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)     #blueprint 추가

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

@manager.command
def test():
    #runs the unit tests
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__=='__main__':
    manager.run()

