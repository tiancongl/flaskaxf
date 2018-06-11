class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY  = "askajd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_db_uri(dbinfo):
    ENGINE= dbinfo.get("ENGINE") or "mysql"
    DRIVER= dbinfo.get("DRIVER") or "pymysql"
    USER= dbinfo.get("USER") or "root"
    PASSWORD= dbinfo.get("PASSWORD") or "rock1204"
    HOST= dbinfo.get("HOST") or  "localhost"
    PORT= dbinfo.get("PORT") or  "3306"
    DB= dbinfo.get("DB") or  "XIAOBA"

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,DB)


class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"rock1204",
        "HOST":"localhost",
        "PORT":"3306",
        "DB":"XIAOBAYAHAHA"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": "3306",
        "DB": "XIAOBA"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StaingConfig(Config):
    DEBUG = True

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": "3306",
        "DB": "XIAOBA"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class ProductConfig(Config):
    DEBUG = True

    DATABASE = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": "3306",
        "DB": "XIAOBA"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

envs = {
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "staging":StaingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}


