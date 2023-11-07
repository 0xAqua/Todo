from . import db


class Todo(db.Model):
    """単一のTODO項目を表すクラス。

    このクラスは、TODOアプリケーションにおける個々のTODO項目のデータモデルを定義します。

    Attributes:
        id (int): 主キーとしてのID。
        title (str): TODO項目のタイトル。空であってはならない。
        completed (bool): TODO項目が完了したかどうか。デフォルトはFalse。
    """
    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(100), nullable=False)
    completed: bool = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        """TODO項目の文字列表現を提供します。"""
        return f"<Todo '{self.title}'>"
