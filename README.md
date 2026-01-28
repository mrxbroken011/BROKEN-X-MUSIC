<h1 align="center"><b>ʙʀᴏᴋᴇɴ ✘ ᴍᴜsɪᴄ</b></h1>

<p align="center">
    <a href="https://github.com/mrxbroken011/BROKEN-X-MUSIC/stargazers"><img src="https://img.shields.io/github/stars/mrxbroken011/BROKEN-X-MUSIC?color=black&logo=github&label=Stars" alt="Stars"/></a>
    <a href="https://github.com/mrxbroken011/BROKEN-X-MUSIC/fork"><img src="https://img.shields.io/github/forks/mrxbroken011/BROKEN-X-MUSIC?color=black&logo=github&label=Forks" alt="Forks"/></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-black?logo=python" alt="Python"/></a>
    <a href="https://telegram.dog/BROKENXNETWORK1"><img src="https://img.shields.io/static/v1?label=Join&message=Telegram&color=blue&logo=telegram" alt="Telegram"/></a>
</p>

<p align="center">
  <b>SAY NO TO COOKIES 🍪 | 0% HEADACHE | HIGH PERFORMANCE</b><br>
  A powerful, cookie-free Telegram Music Bot designed for stability, speed, and high-quality audio streaming.
</p>

<p align="center">
  <b>⚠️ REPO FORKING IS HIGHLY RECOMMENDED BEFORE DEPLOYING</b>
</p>

---

> [!CAUTION]
> **IMPORTANT NOTICE: API REQUIREMENT**
> 
> 🎥 **CUSTOM YOUTUBE API IS LIVE**
> 
> To ensure cookie-free playback, this bot requires a custom API Key.
> 
> 🔑 **Get your Free API KEY here:** [AboutBrokenX](https://t.me/Aboutbrokenx/53)
> 
> *Failure to add this key may result in playback errors.*

---

## 🛠 Config Vars

<details>
<summary>Click to view required Environment Variables</summary>
<br>

Copy these variables into your `.env` file or cloud configuration panel.

```bash
API_ID=123456
API_HASH=abcdef123456
BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
LOGGER_ID=-1001234567890
MONGO_DB_URI=mongodb+srv://user:pass@cluster0.mongodb.net/?retryWrites=true&w=majority
OWNER_ID=123456789
STRING_SESSION=AgAd...
YTAPIURL=[https://mrbroken-brokenxbots.hf.space](https://mrbroken-brokenxbots.hf.space)
YTKEY=Get_From_Link_Above

```

</details>

---

## 🚀 One-Click Deployment

Deploy the bot to your preferred cloud platform with a single click.

<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/mrxbroken011/BROKEN-X-MUSIC">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DDeploy%2Bon%26message%3DHeroku%26color%3Dpurple%26logo%3Dheroku" width="180" alt="Deploy on Heroku"/>
</a>
<a href="https://www.google.com/search?q=https://render.com/deploy%3Frepo%3Dhttps://github.com/mrxbroken011/BROKEN-X-MUSIC">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DDeploy%2Bon%26message%3DRender%26color%3Dwhite%26logo%3Drender%26logoColor%3Dblack" width="180" alt="Deploy on Render"/>
</a>
</p>

<p align="center">
<a href="https://www.google.com/search?q=https://railway.app/new/template%3Ftemplate%3Dhttps://github.com/mrxbroken011/BROKEN-X-MUSIC">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DDeploy%2Bon%26message%3DRailway%26color%3D0b0d16%26logo%3Drailway" width="180" alt="Deploy on Railway"/>
</a>
<a href="https://www.google.com/search?q=https://app.koyeb.com/deploy%3Ftype%3Dgit%26repository%3Dgithub.com/mrxbroken011/BROKEN-X-MUSIC">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DDeploy%2Bon%26message%3DKoyeb%26color%3Dblack%26logo%3Dkoyeb" width="180" alt="Deploy on Koyeb"/>
</a>
</p>

---

## 💻 Manual Deployment (VPS)

<details>
<summary><b>Click to expand VPS Installation Guide</b></summary>




Run the following commands in your terminal to set up the bot on Ubuntu/Debian.

```bash
# 1. Update System & Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl python3-pip python3-venv ffmpeg unzip tmux

# 2. Install Node.js 20 (LTS)
curl -fsSL [https://deb.nodesource.com/setup_20.x](https://deb.nodesource.com/setup_20.x) | sudo -E bash -
sudo apt install -y nodejs
source ~/.bashrc

# 3. Clone Repository
git clone [https://github.com/mrxbroken011/BROKEN-X-MUSIC](https://github.com/mrxbroken011/BROKEN-X-MUSIC)
cd BROKEN-X-MUSIC

# 4. Create Background Session
tmux new -s broken

# --- INSIDE TMUX SESSION ---

# 5. Setup Python Environment
python3 -m venv venv
source venv/bin/activate
pip install -U pip && pip install -r requirements.txt

# 6. Configure & Start
# Edit the config file if prompted, or ensure env vars are set
bash setup
bash start

```

**Useful Management Commands:**

```bash
tmux detach                # Exit session (Bot keeps running)
tmux attach-session -t broken   # Return to bot session
tmux kill-session -t broken     # Stop the bot completely
rm -rf BROKEN-X-MUSIC           # Delete the bot folder

```

</details>

---

## 🐳 Docker Deployment

<details>
<summary><b>Click to expand Docker Instructions</b></summary>




Recommended for advanced users seeking isolation.

**Method 1: Docker Compose (Recommended)**

1. Create a file named `docker-compose.yml` in the root directory:
```yaml
version: '3.8'
services:
  broken-music:
    build: .
    container_name: broken-music
    env_file:
      - .env
    restart: always

```


2. Create a `.env` file with your variables.
3. Start the bot:
```bash
docker-compose up -d

```



**Method 2: Standard Build**

```bash
# Build Image
docker build -t broken-music .

# Run Container
docker run -d --env-file .env --name broken-music broken-music

```

</details>

---

## 📞 Support & Updates

<p align="center">
<a href="https://telegram.me/BROKENXNETWORK1">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DJoin%26message%3DUpdate%2BChannel%26color%3Dblue%26logo%3Dtelegram" alt="Update Channel">
</a>





<a href="https://telegram.me/ABOUTBROKENX">
<img src="https://www.google.com/search?q=https://img.shields.io/static/v1%3Fstyle%3Dfor-the-badge%26label%3DJoin%26message%3DSupport%2BGroup%26color%3Dblue%26logo%3Dtelegram" alt="Support Group">
</a>
</p>

<p align="center">
© 2025 BROKEN X NETWORK | ALL RIGHTS RESERVED
</p>

```

