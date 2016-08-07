import os

class Config(object):
    # ����������, ������� �� ����� �������
    # � ������ ���� �������, flask ����� ����������
    # ��������� ���������� ����������. ���� �������� -
    # - 500 ������ ��� ����� ���� �������������� ����������.
    DEBUG = False
    # ��������� ������ ������ "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True
    # ��������� ����, ������� ����� ������������� ��� �������
    # ������, �������� cookies.
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'
    # URI ������������ ��� ����������� � ���� ������
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True