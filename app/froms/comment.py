from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, length


class CommentForm(FlaskForm):
    body = TextAreaField(
        "评论",
        validators=[
            DataRequired(),
            length(1, 255, "你废话太多了")
        ],
        render_kw={
            "placeholder": "请输入标题"
        }
    )
    sbumit = SubmitField(
        "提交",
        render_kw={

            "class": "glyphicon glyphicon-edit"
        }

    )
