"""測試 Google Generative AI API 連線"""
import os

# 方法1: 直接設定 API key
api_key = "AIzaSyAb8RN6IYgL4wQF0dPwb_MC7P7GxOnurjx-d1e0l2LahZ2fPA_w"

# 方法2: 從環境變數讀取（如果有設定的話）
if not api_key:
    api_key = os.getenv('GOOGLE_GENERATIVE_AI_API_KEY') or os.getenv('GEMINI_API_KEY')

if api_key:
    print(f"✓ API key 已載入: {api_key[:20]}...")
else:
    print("✗ 找不到 API key")
    exit(1)
    
# 嘗試使用 Gemini API
try:
    import google.generativeai as genai
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content("請用繁體中文說：你好！")
    print(f"\n測試回應: {response.text}")
    print("\n✓ Gemini API 連線成功！")
    
except Exception as e:
    print(f"\n✗ 錯誤: {e}")
