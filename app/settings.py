import os

base_dir = os.path.abspath(os.path.dirname(__file__))
b = os.getcwd()


class Config:
    # mysql: // scott: tiger @ localhost / mydatabase
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sldfjl433lkfsLKSDFJ4lskdf')
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 邮件配置
    MAIL_SERVER = 'smtp.qq.com'
    # MAIL_USE_TLS = True,
    # MAIL_USE_SSL = False,
    MAIL_USERNAME = "2593676491@qq.com"
    MAIL_PASSWORD = "kjxkkeblhgiaeced"
    MAIL_DEBUG = True

    # 文件上传
    # 文件上传大小
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    # 文件存储位置
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, "static/upload")


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

# print("emmm" + os.path.join(base_dir, "static/upload"))
# print(base_dir)
# print(__name__)
# print(b)
# print(__file__)
