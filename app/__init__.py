from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

# 拡張機能の初期化
# ORM用のSQLAlchemy
db = SQLAlchemy()
# データベースマイグレーション用のMigrate
migrate = Migrate()


def create_app() -> Flask:
    """Flask アプリケーションインスタンスを作成し、設定を読み込むファクトリ関数。

    * この関数はアプリケーションの初期化中に実行されるべき設定の読み込みや、拡張機能の初期化、ルーティングの設定などを行います。

    Returns:
        Flask: Flaskアプリケーションのインスタンスを返します。

    Note:
        この関数は拡張機能を初期化し、アプリケーションの設定を行い、ルートを登録します。
    """

    # Flaskインスタンスを作成
    app = Flask(__name__)
    # 'config.Configクラスから設定を読み込む
    app.config.from_object(Config)

    # プラグインを初期化
    db.init_app(app)
    migrate.init_app(app, db)

    # ブループリントの登録
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
