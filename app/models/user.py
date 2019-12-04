from app.extends import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
    confiremd = db.Column(db.Boolean, default=False)

    # 保护字段，不让别人看我，比如xxx.password,直接报错
    @property
    def password(self):
        raise ArithmeticError("password是不可读字段")

    # 设置密码，加密，比如,xxx.password=xxxx
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 校验密码
    def verity_password(self, password):
        # print(self.password_hash,password)
        # print(type(self.password_hash),type(password))
        return check_password_hash(self.password_hash, password)

    # 生成激活的token
    def generate_active_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({"id": self.id})

    # 校验ｔｏｋｅｎ,检验时还不知到是谁，需要静态方法
    @staticmethod
    def check_active_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False

        user = Users.query.get(data.get("id"))

        if user is None:
            # 此用户不存在
            return False
        if not user.confiremd:
            # 用户没有激活才激活
            user.confiremd = True
            db.session.add(user)
            db.session.commit()
        return True

        # 生成修改邮箱的token

    def generate_email_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({"email": self.email})

    def check_email_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        print(self.email)
        print(data.get("email"))
        if self.email == data.get("email"):
            db.session.add(data.get("email"))
            db.session.commit()
            return True
        else:
            return False


@login_manager.user_loader
def user_login(user_id):
    return Users.query.get(int(user_id))
