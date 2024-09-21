import requests
import time
import unittest

class TestAPIAccess(unittest.TestCase):
    def test_api_reachability(self):
        start_time = time.time()  # テスト開始時間を記録
        try:
            response = requests.get("https://www.google.com")  # Googleのエンドポイントにリクエストを送信
            self.assertEqual(response.status_code, 200)  # ステータスコードが200であることを確認
        except requests.exceptions.RequestException as e:
            self.fail(f"Request failed: {e}")  # リクエストエラーを処理
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")  # その他のエラーを処理
        finally:
            end_time = time.time()  # テスト終了時間を記録
            duration = end_time - start_time  # 実行時間を計算
            print(f"Test execution time: {duration:.2f} seconds")  # 実行時間を表示
            with open('test_duration.txt', 'w') as f:
                f.write(f"Test execution time: {duration:.2f} seconds\n")  # 実行時間をファイルに保存
                print("test_duration.txt created successfully.")  # ファイル作成確認メッセージ developer-add
