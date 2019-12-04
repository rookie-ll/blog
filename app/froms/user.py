# 导入表单基类
from flask_wtf import FlaskForm
# 导入字段
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
# 导入验证器类
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Users


class RegisterForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[DataRequired(), Length(6, 18, message="用户名必须是6～18个字符")],
    )

    password = PasswordField(
        '用户密码',
        validators=[DataRequired(), Length(6, 18, message="密码必须是6～１８个字符")],
        render_kw={
            "class": "form-control",
        }
    )
    configrm = PasswordField(
        '确认密码',
        validators=[DataRequired(), EqualTo("password", message="俩次密码不一致")],
        render_kw={
            "class": "form-control",
        }
    )
    emial = StringField(
        '邮箱',
        validators=[DataRequired(), Email("邮箱格式不正确")]
    )
    submit = SubmitField(
        '立即注册',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    # 自定义验证器,验证用户名,field为当前字段
    def validate_username(self, field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名以存在,请选择其他用户名')

    def validate_emial(self, field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已被注册')


# 登陆表单
class LoginForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
        }
    )
    password = PasswordField(
        '用户密码',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
        })
    remenber_me = BooleanField('记住我')
    submit = SubmitField(
        '登陆',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


# 修改密码
class CheagePwdForm(FlaskForm):
    old_pwd = PasswordField(
        "旧密码",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
        }
    )
    new_pwd = PasswordField(
        "新密码",
        validators=[DataRequired(), Length(6, 18, message="密码必须是6～１８个字符")],
        render_kw={
            "class": "form-control",
        }
    )
    configrm = PasswordField(
        '确认密码',
        validators=[EqualTo("new_pwd", "俩次密码不一致")]
    )
    submit = SubmitField(
        '确认修改',
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )


# 修改邮箱
class CheageEmail(FlaskForm):
    new_email = StringField(
        "请输入邮箱",
        validators=[DataRequired(), Email("邮箱格式不正确")],
        render_kw={
            "class": "form-control",
        }
    )
    submit = SubmitField(
        "提交",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat"
        }
    )

    def validate_emial(self, field):
        print(Users.query.filter_by(email=field.data).first())
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError("邮箱与初始邮箱相同")
