import os

base_dir = os.path.abspath(os.path.dirname(__name__))


class Config:
    # mysql: // scott: tiger @ localhost / mydatabase
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY','sldfjl433lkfsLKSDFJ4lskdf')
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 邮件配置
    MAIL_SERVER = 'smtp.qq.com'
    #MAIL_USE_TLS = True,
    #MAIL_USE_SSL = False,
    MAIL_USERNAME = "2593676491@qq.com"
    MAIL_PASSWORD = "kjxkkeblhgiaeced"
    MAIL_DEBUG = True

    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "blog_dev.sqlite")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/blog"


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "blog_test.sqlite")


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/blog"


configs = {
    'development': DevelopmentConfig,
    'testingConfig': TestingConfig,
    'production': ProductionConfig
}
