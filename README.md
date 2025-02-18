# Instagram DMs Sender

🚀 **Automated Instagram DM Sender** using `instagrapi`. A fast and lightweight tool to send bulk messages without relying on Selenium or a web browser.

---

## ✨ Features
✅ **No Selenium Required** – Runs without WebDriver or a browser.  
✅ **Session Management** – Avoids repeated logins by saving & loading session cookies.  
✅ **Human-Like Behavior** – Mimics real user actions to prevent detection.  
✅ **Bulk Messaging** – Reads usernames and messages from text files.  
✅ **Auto-Pause Mechanism** – Avoids Instagram's spam detection.  
✅ **Lightweight & Fast** – Optimized for performance and efficiency.  

---

## 📦 Installation

### **Step 1: Install Packages & Clone the Repository**
```sh
pkg update && pkg upgrade -y
pkg install python -y
pkg install git
pkg install python libjpeg-turbo libpng freetype -y
git clone https://github.com/MarketingT3ch/MarketingT3ch-IG-Messenger.git
cd MarketingT3ch-IG-Messenger
```

### **Step 2: Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🛠️ How to Use

### **Step 1: Add Instagram Accounts**
Create a file `account.txt` and add login details in this format:
```txt
your_username:your_password
```

### **Step 2: Add Recipients**
Create a file `usernames.txt` and list usernames (one per line):
```txt
username1
username2
username3
```

### **Step 3: Write Your Message**
Create a file `message.txt` and add your full message:
```txt
Hello! This is a test message.
Hope you are doing well!
```

### **Step 4: Run the Script**
```sh
python InstaDM_Pro.py
```

---

## 🛡️ Anti-Blocking Measures
🔹 **Session cookies** prevent frequent logins.  
🔹 **Randomized delays** mimic human behavior.  
🔹 **Pauses after sending multiple messages** to avoid spam detection.  
🔹 **Handles Instagram’s temporary restrictions automatically.**  

---

## 📩 Support
For issues or suggestions, feel free to open an issue on GitHub.

---

🔥 **Automate Instagram Messaging Easily & Safely!**

