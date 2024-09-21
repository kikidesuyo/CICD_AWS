import requests
import time

def test_api_reachability():
    start_time = time.time()  # テスト開始時間を記録
    try:
        response = requests.get("https://www.google.com")  # Googleのエンドポイントにリクエストを送信
        assert response.status_code == 200  # ステータスコードが200であることを確認
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")  # リクエストエラーの詳細を表示
    except AssertionError:
        print("Received non-200 response")  # 非200ステータスコードのエラーメッセージ
    finally:
        end_time = time.time()  # テスト終了時間を記録
        duration = end_time - start_time  # 実行時間を計算
        print(f"Test execution time: {duration:.2f} seconds")  # 実行時間を表示
        with open('test_duration.txt', 'w') as f:
            f.write(f"Test execution time: {duration:.2f} seconds\n")  # 実行時間をファイルに保存
            print("test_duration.txt created successfully.")  # ファイル作成確認メッセージ

# スクリプトが直接実行されたときにテストを呼び出す
if __name__ == "__main__":
    test_api_reachability()
