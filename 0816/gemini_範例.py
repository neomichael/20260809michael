"""
Google Gemini API 使用範例
請先設定有效的 API key 才能執行
"""

import os

# ============================================
# 步驟 1: 設定您的 API Key
# ============================================
# 請將下方的 "您的API_Key" 替換成您從 Google AI Studio 取得的真實 key
# 網址: https://aistudio.google.com/app/apikey

API_KEY = "您的API_Key"  # 請替換成真實的 key

# 或從環境變數讀取（如果您已設定 .env 檔案）
if API_KEY == "您的API_Key":
    API_KEY = os.getenv('GOOGLE_GENERATIVE_AI_API_KEY') or os.getenv('GEMINI_API_KEY')

if not API_KEY or API_KEY == "您的API_Key":
    print("⚠️  請先設定 API Key！")
    print("1. 前往 https://aistudio.google.com/app/apikey 取得 API key")
    print("2. 將 key 貼到此程式的 API_KEY 變數，或")
    print("3. 在 .env 檔案中設定 GOOGLE_GENERATIVE_AI_API_KEY")
    exit(1)

# ============================================
# 步驟 2: 使用 Gemini API
# ============================================
try:
    import google.generativeai as genai
    
    # 設定 API
    genai.configure(api_key=API_KEY)
    
    # 建立模型
    model = genai.GenerativeModel('gemini-pro')
    
    print("✓ Gemini API 已成功連線！\n")
    print("=" * 50)
    
    # 範例 1: 簡單對話
    print("\n【範例 1】簡單對話")
    print("-" * 50)
    response = model.generate_content("請用繁體中文介紹自己")
    print(response.text)
    
    # 範例 2: 數學問題
    print("\n【範例 2】數學計算")
    print("-" * 50)
    response = model.generate_content("請計算費氏數列的前 10 項，並用 Python 程式展示")
    print(response.text)
    
    # 範例 3: 程式碼生成
    print("\n【範例 3】程式碼生成")
    print("-" * 50)
    response = model.generate_content("寫一個 Python 函式來判斷質數")
    print(response.text)
    
    print("\n" + "=" * 50)
    print("✓ 所有範例執行完成！")
    
except ImportError:
    print("✗ 錯誤：找不到 google.generativeai 模組")
    print("請執行：uv pip install google-generativeai")
    
except Exception as e:
    print(f"✗ 錯誤：{e}")
    print("\n可能的原因：")
    print("1. API key 無效或已過期")
    print("2. 網路連線問題")
    print("3. API 配額已用完")
