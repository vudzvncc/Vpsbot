import os
import threading
import requests
from flask import Flask
import telebot

# -------------------------------------------------------------------
# 1. TẠO WEB SERVER FLASK ĐỂ GIỮ BOT HOẠT ĐỘNG 24/7 TRÊN HOSTING
# -------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Windows VPS Telegram Bot đang hoạt động 24/7!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# -------------------------------------------------------------------
# 2. CẤU HÌNH BOT TELEGRAM VÀ MÁY ẢO WINDOWS CẤU HÌNH MẠNH
# -------------------------------------------------------------------
# Thay TOKEN của bạn từ @BotFather vào đây (hoặc thiết lập biến môi trường BOT_TOKEN)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "DÁN_TOKEN_BOT_CỦA_BẠN_VÀO_ĐÂY")
bot = telebot.TeleBot(BOT_TOKEN)

# Thông tin Máy Ảo Windows Cấu Hình Cực Mạnh
VPS_INFO = {
    "ip": os.environ.get("VPS_IP", "103.179.188.45:3389"),
    "username": os.environ.get("VPS_USER", "Administrator"),
    "password": os.environ.get("VPS_PASS", "WinServer2022@PassCore64GB"),
    "cpu": "16 vCPU (Intel Xeon Platinum 8370C)",
    "ram": "64 GB RAM DDR4",
    "disk": "512 GB NVMe SSD High-Speed",
    "os": "Windows Server 2022 Datacenter (64-bit)",
    "bandwidth": "1 Gbps Unmetered (24/7)"
}

# -------------------------------------------------------------------
# 3. XỬ LÝ LỆNH TỪ BÀN PHÍM TELEGRAM
# -------------------------------------------------------------------
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "👋 **Chào mừng bạn đến với Bot Cấp Phát Máy Ảo Windows 24/7!**\n\n"
        "Gõ lệnh `/give` để nhận thông tin máy ảo Windows cấu hình cao."
    )
    bot.reply_to(message, welcome_text, parse_mode="Markdown")

@bot.message_handler(commands=['give'])
def give_vps(message):
    vps_text = (
        "🖥️ **THÔNG TIN MÁY ẢO WINDOWS (RDP) CẤU HÌNH MẠNH**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🌐 **IP máy:** `{VPS_INFO['ip']}`\n"
        f"👤 **Tên tài khoản:** `{VPS_INFO['username']}`\n"
        f"🔑 **Mật khẩu:** `{VPS_INFO['password']}`\n\n"
        "⚡ **Thông số cấu hình máy:**\n"
        f"• **Hệ điều hành:** {VPS_INFO['os']}\n"
        f"• **CPU:** {VPS_INFO['cpu']}\n"
        f"• **RAM:** {VPS_INFO['ram']}\n"
        f"• **Ổ cứng:** {VPS_INFO['disk']}\n"
        f"• **Băng thông:** {VPS_INFO['bandwidth']}\n\n"
        "📌 *Hướng dẫn kết nối:* Mở ứng dụng **Remote Desktop Connection** (`mstsc`) trên Windows hoặc ứng dụng Remote Desktop trên điện thoại, nhập IP và thông tin trên để truy cập."
    )
    bot.reply_to(message, vps_text, parse_mode="Markdown")

# -------------------------------------------------------------------
# 4. KHỞI CHẠY CHƯƠNG TRÌNH
# -------------------------------------------------------------------
if __name__ == "__main__":
    # Khởi chạy Flask Server ở luồng phụ (để giữ bot không bị treo)
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    print("Bot đang hoạt động...")
    bot.infinity_polling()
