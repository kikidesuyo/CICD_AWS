from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import boto3

# ヘッドレスモードでChromeを起動
options = webdriver.ChromeOptions()
options.binary_location = "/usr/local/bin/chrome-linux/chrome-linux/chrome"  # 実行ファイルのパスを指定
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# ドライバーのセットアップ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

screenshot_path = 'search_results.png'  # スクリーンショットの保存パス

try:
    # Googleのトップページにアクセス
    driver.get('https://www.google.com')

    # 検索ボックスにキーワードを入力
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('OpenAI')
    search_box.submit()

    # 検索結果が表示されるまで待機
    time.sleep(2)

    # 検索結果のスクリーンショットを取得
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')

except Exception as e:
    print(f'Test failed: {e}')
finally:
    driver.quit()
