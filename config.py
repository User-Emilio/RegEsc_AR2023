class DevelopmentConfig():

    # Configuracion de Desarrollo y pruebas

    DEBUG = True
    SERVER_NAME = '127.0.0.1:5000'
    SECRET_KEY = 'e6e4a417c079412c90c67760505f8a7b'
    TEMPLATE_FOLDER = 'views/templates/'
    STATIC_FOLDER = 'views/static/'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sa:nova-123@127.0.0.1/RegEsc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TOKEN_BOT = '5599230099:AAGOwPuKSEKstMDZ_wa6T6hDEQ0l8PMCLLw'