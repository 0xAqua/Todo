from flask import Blueprint, render_template, request, redirect, url_for, Response
from typing import Union

from .models import Todo
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index() -> str:
    """ルートページにアクセスした際に実行されるビュー関数。

    * 登録されている全てのTODO項目をデータベースから取得し、
    * 'index.html' テンプレートに渡して表示します。

    Returns:
        Response: クライアントに返すレスポンスオブジェクト。
    """
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@main.route('/add', methods=['POST'])
def add() -> Response:
    """TODO項目を追加するためのビュー関数。

    * ユーザーが入力したタイトルを受け取り、新しいTODO項目をデータベースに追加します。
    * 処理の後、ルートページにリダイレクトします。

    Returns:
        Redirect: ルートページへのリダイレクトオブジェクト。
    """
    title: str = request.form['title']
    new_todo: Todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id: int) -> Union[str, Response]:
    """指定されたIDのTODO項目を編集するビュー関数。

    * GETリクエストでは編集フォームを表示し、POSTリクエストでは実際に変更を保存します。
    * 保存後はルートページにリダイレクトします。

    Args:
        todo_id (int): 編集するTODO項目のID。

    Returns:
        Response: クライアントに返すレスポンスオブジェクト。編集フォームまたはリダイレクト。
    """
    todo: Todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        todo.title = request.form['title']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', todo=todo)


@main.route('/delete/<int:todo_id>')
def delete(todo_id: int) -> Response:
    """指定されたIDのTODO項目を削除するビュー関数。

    * 項目をデータベースから削除した後、ルートページにリダイレクトします。

    Args:
        todo_id (int): 削除するTODO項目のID。

    Returns:
        Redirect: ルートページへのリダイレクトオブジェクト。
    """
    todo: Todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))
