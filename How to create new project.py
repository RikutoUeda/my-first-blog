#仮想環境用のディレクトリ作成と移動
mkdir djangogirls
cd djangogirls

#仮想環境の作成
python -m venv myvenv

#仮想環境の起動
myvenv\Scripts\activate

#Djangoのインストール
python -m pip install --upgrade pip

#以下のディレクトリにrequirements.txtを作成
djangogirls/requirements.txt

#requirements.txtに以下を記入
Django~=2.2.4

#以下を実行しDjangoをインストール
pip install -r requirements.txt

#仮想環境が起動された状態で以下のコマンドを実行しDjangoのプロジェクトを作成
django-admin.exe startproject mysite .

#mysite/settings.pyのソースコードを以下に修正
TIME_ZONE = 'Asia/Tokyo'
LANGUAGE_CODE = 'ja'
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

#mysite/settings.pyの最下部に追記
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#以下を実行しデータベースの作成
python manage.py migrate

#ウェブサーバーの起動
python manage.py runserver

#UnicodeDecodeErrorで失敗した場合は以下で起動
python manage.py runserver 0:8000

#ブラウザ
http://127.0.0.1:8000/

------------------------------------------------------------------------

#既に仮想環境とデータベースなどが作成済みである場合
#対象の仮想環境ディレクトリに移動
cd djangogirls

#仮想環境の起動
myvenv\Scripts\activate

#必要であればDjangoのアップグレード
python -m pip install --upgrade pip

#ウェブサーバーの起動
python manage.py runserver

#UnicodeDecodeErrorで失敗した場合は以下で起動
python manage.py runserver 0:8000

#ブラウザ
http://127.0.0.1:8000/
