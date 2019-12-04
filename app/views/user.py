from flask import render_template, Blueprint, redirect, url_for, flash, request
from app.froms import RegisterForm, LoginForm, CheagePwdForm, CheageEmail
from app.models import Users
from app.extends import db
from app.email import send_mail
from flask_login import login_user, logout_user, login_required, current_user

user = Blueprint('user', __name__, template_folder='../templeates')


@user.route('/registered/', methods=['GET', 'POST'])
def registered():
    form = RegisterForm()
    if form.validate_on_submit():
        # 创建对象，写入数据
        user = Users(
            username=form.username.data,
            password=form.password.data,
            email=form.emial.data
        )
        db.session.add(user)
        db.session.commit()
        # 生成token
        token = user.generate_active_token()
        # 发送激活邮件
        send_mail(form.emial.data, "账户激活", "email/account_activate", token=token, username=form.username.data)
        flash("邮件已经发送，请点击链接激活", "ok")

        return redirect(url_for("main.index"))
    return render_template('/user/registered.html', form=form)


@user.route('/activate/<token>/')
def activate(token):
    print(Users.check_active_token(token))
    if Users.check_active_token(token):
        flash("激活成功，请登陆", "ok")
        return redirect(url_for("user.login"))
    else:
        flash("激活失败")
        return redirect(url_for("main.index"))


@user.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # print(form.password.data)
    if form.validate_on_submit():
        # try:
        #     u = Users.query.filter_by(username=form.username.data).first()
        # except:
        #     u = None
        # print(u.username)
        u = Users.query.filter_by(username=form.username.data).first()
        if u is None:
            flash("用户名错误", "err")
            # print(u)
        elif u.verity_password(form.password.data):
            # 验证通过,用户登陆,顺便可以完成记住我的功能
            # print(u.username)
            login_user(u, remember=form.remenber_me.data)
            # 如果有下一跳转地址，就跳转到下一跳的地址，如果没有，就跳转到主页
            return redirect(request.args.get("next") or url_for("main.index"))
        else:
            flash("密码错误", "err")
            # print("密码错误")
    return render_template('user/login.html', form=form)


@user.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("您已退出登陆", "ok")
    return redirect(url_for("main.index"))


@user.route('/profile/')
@login_required
def profile():
    return render_template("user/profile.html")


# 重置密码
@user.route('/cheage_password/', methods=['GET', 'POST'])
@login_required
def cheage_password():
    form = CheagePwdForm()
    if form.validate_on_submit():
        print(current_user)
        if current_user.verity_password(form.old_pwd.data):
            current_user.password = form.new_pwd.data
            db.session.add(current_user)
            db.session.commit()
            logout_user()
            flash("修改密码成功,请重新登陆", "ok")
            return redirect(url_for('user.login'))
        else:
            flash("原始密码有误", "err")
            return redirect(url_for('user.cheage_password'))
    return render_template("user/cheage_password.html", form=form)


# 修改邮箱
@user.route('/cheage_email/', methods=['GET', 'POST'])
@login_required
def cheage_email():
    form = CheageEmail()
    if form.validate_on_submit():
        token = current_user.generate_email_token()
        # 发送激活邮件
        send_mail(form.new_email.data, "修改邮箱", "email/cheage_email", token=token, username=current_user.username)
        flash("邮件已经发送，请点击链接修改", "ok")
    return render_template("user/cheage_email.html",form=form)


@user.route('/activate_email/<token>/')
def activate_email(token):
    if current_user.check_email_token(token):
        flash("修改成功",'ok')
        return redirect(url_for("user.profile"))
    else:
        flash("修改失败",'err')
        return redirect(url_for("user.cheage_email"))
