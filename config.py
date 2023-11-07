import os
from dotenv import load_dotenv
from typing import Optional


load_dotenv()


class Config:
    """アプリケーションの設定を管理するクラス。

    環境変数を使用して設定をロードし、不足している設定がある場合はデフォルト値を使用します。

    Attributes:
        SECRET_KEY (str): シークレットキー。環境変数から取得するか、デフォルト値を使用。
        SQLALCHEMY_DATABASE_URI (Optional[str]): データベース接続のためのURI。必要な環境変数がない場合はNone。
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flask-SQLAlchemyの設定。トラッキングのオン/オフ。
    """
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'fallback-secret-key')

    SQLALCHEMY_DATABASE_URI: Optional[str] = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    ) if all(os.getenv(var) for var in ['MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_HOST', 'MYSQL_DB']) else None

    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
