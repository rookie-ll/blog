from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField

from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
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
