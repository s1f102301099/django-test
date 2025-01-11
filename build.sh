#!/bin/bash

# 仮想環境の作成（もしまだ作成していなければ）
python3 -m venv venv
source venv/bin/activate

# 必要なパッケージのインストール
pip install -r requirements.txt

# マイグレーションの適用
python manage.py migrate

# 静的ファイルの収集
python manage.py collectstatic --noinput

# サーバーの起動準備完了
echo "Build completed successfully."
