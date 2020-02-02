from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField,StringField

from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField(
        "",
        validators=[
            DataRequired(),
            Length(0 - 255, message="标题不能太长哦")
        ],
        render_kw={
            "placeholder": "请输入标题"
        }
    )
    conent = TextAreaField(
        "",
        validators=[
            DataRequired(),
            Length(0 - 255, message="说话不能太多也不能太少，你懂我意思吧")
        ],
        render_kw={
            "placeholder":"你此刻的想法..."
        }
    )

    submit = SubmitField(
        "发表"
    )
