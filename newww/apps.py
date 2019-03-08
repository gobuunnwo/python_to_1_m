# django.appsモジュールのAppConfig(設定ファイルをまとめて入れるディレクトリ)クラスの活用
from django.apps import AppConfig

# NewwwディレクトリのConfigクラス（AppConfig）の設定
class NewwwConfig(AppConfig):
    name = 'newww'
