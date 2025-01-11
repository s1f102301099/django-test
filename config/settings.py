import os
import environ

# 環境変数を読み込む
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# セキュリティキー（環境変数から読み込む）
SECRET_KEY = env('SECRET_KEY')

# デバッグ設定
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['yourapp.onrender.com'])

# PostgreSQLの設定（RenderのデータベースURLを使います）
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://user:password@localhost/dbname')
}

# カスタムユーザー
AUTH_USER_MODEL = 'accounts.CustomUser'

# ストレージ設定（RenderではS3を使うことを推奨）
INSTALLED_APPS = [
    'storages',  # S3を使用する場合
    # その他のアプリケーション
]

# AWS S3の設定（環境変数から取得）
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

# 静的ファイルをS3にアップロード
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# メディアファイルの設定
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

# マイグレーションの設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ログイン後のリダイレクトURL設定
LOGIN_REDIRECT_URL = '/chat_room/'

# ログアウト後のリダイレクト先
LOGOUT_REDIRECT_URL = '/search/'

# ファイルアップロード用
MEDIA_URL = '/media/'
