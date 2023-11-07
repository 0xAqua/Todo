import os
from app import create_app

# Flaskアプリケーションのインスタンスを作成します
app = create_app()

if __name__ == '__main__':
    """main

    * このスクリプトがコマンドラインから直接実行されたときに、Flask開発サーバーを起動します。
    """

    # Flaskの設定のための環境変数を設定します
    os.environ['FLASK_APP'] = 'run.py'  # Flaskアプリケーションのエントリーポイントを指定
    os.environ['FLASK_ENV'] = 'development'  # アプリケーションの環境を開発モードに設定

    # Flaskの開発サーバーを起動します
    app.run()  # デフォルトではローカルの5000ポートでサーバーが実行されます
