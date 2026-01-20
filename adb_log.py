import subprocess
import datetime
import os

def capture_adb_error_logs(output_file="error_log.txt"):
    try:
        # 1. 檢查是否有設備連線
        devices = subprocess.check_output(["adb", "devices"]).decode("utf-8")
        if "device\n" not in devices.split("\n", 1)[1]:
            return print("錯誤：未偵測到已連線的 Android 設備。")

        # 2. 執行 ADB logcat 指令 (抓取目前緩衝區中的 Error 等級日誌)
        print("正在抓取 Error Log...")
        # -d: 輸出後結束, *:E: 過濾所有標籤的 Error 等級
        log_data = subprocess.check_output(["adb", "logcat", "-d", "*:E"]).decode("utf-8", errors="ignore")

        # 3. 存成檔案並加上時間戳記
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"--- 抓取時間: {timestamp} ---\n{log_data}")
        
        print(f"成功！日誌已儲存至: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"執行出錯: {e}")

if __name__ == "__main__":
    capture_adb_error_logs()