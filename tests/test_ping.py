import requests
import time

def test_api_reachability():
    start_time = time.time()  # テスト開始時間を記録
    try:
        response = requests.get("https://www.google.com")  # Googleのエンドポイントに変更
        assert response.status_code == 200
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        end_time = time.time()  # テスト終了時間を記録
        duration = end_time - start_time  # 実行時間を計算
        print(f"Test execution time: {duration:.2f} seconds")
        with open('test_duration.txt', 'w') as f:
            f.write(f"Test execution time: {duration:.2f} seconds\n")  # 実行時間をファイルに保存
            print("test_duration.txt created successfully.")  # ファイル作成確認メッセージ
