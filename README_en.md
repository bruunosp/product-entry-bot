# 🚀 Power Automation - Product Registration Bot

This project automates the registration of multiple products on a website.

Two different scripts were developed for this purpose:

- ✅ **Selenium version** – runs in the background using HTML elements (recommended).
- ✅ **PyAutoGUI version** – uses mouse/keyboard automation and requires full control of your screen.

---

## 📌 Technologies Used

- [Python](https://www.python.org/)
- [Selenium](https://selenium.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-project.git
cd your-project
```

### 2. Create the `.env` file

```bash
# Copy the example file and fill in your credentials
cp .env.example .env
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🖱️ PyAutoGUI Version (foreground only)

> ⚠️ Do **not** move your mouse or type while the script is running.

1. Open the website: [Hashtag Cadastro](https://dlp.hashtagtreinamentos.com/python/intensivao/login)
2. Run the helper script:

```bash
python scripts/mouse_position_helper.py
```

3. Hover over the **Email** input field to capture its coordinates.
4. Update your `.env` file:
   ```env
   MOUSE_POSITION_X_EMAIL=xxx
   MOUSE_POSITION_Y_EMAIL=yyy
   ```

5. Log in manually to the site.
6. Repeat the process for the **Product Code** input:
   ```env
   MOUSE_POSITION_X_CODIGO=xxx
   MOUSE_POSITION_Y_CODIGO=yyy
   ```

7. Run the PyAutoGUI version:

```bash
python scripts/pyautogui_version.py
```

---

### 🌐 Selenium Version (recommended ✅)

1. Make sure your `.env` file includes:
   ```env
   LOGIN=your_email@example.com
   PASSWORD=your_password
   ```

2. Run the Selenium version:

```bash
python scripts/selenium_version.py
```

---

## 📁 Project Structure

```
powerup-automation/
│
├── database/
│   └── db.csv                    # Product data source
│
├── docs/
│   └── PowerUp_Automation_Guide.pdf   # Project guide
│
├── scripts/
│   ├── mouse_position_helper.py  # Helper script for PyAutoGUI
│   ├── pyautogui_version.py      # PyAutoGUI-based script
│   └── selenium_version.py       # Selenium-based script
│
├── template/
│   └── template.py               # Reference script
│
├── .env.example                  # Example environment variables
├── .gitignore                    # Files to ignore in Git
├── requirements.txt              # Dependency list
└── README.md                     # Project documentation
```

---

## 🙋‍♂️ Author

Project created during the [Hashtag Treinamentos](https://portalhashtag.com/) Python bootcamp and enhanced by **Bruno Felipe Passareli** with background automation and secure handling using Selenium.

---

## 🧠 Future Improvements

- GUI for capturing mouse coordinates
- Secure credential handling
- Unit testing for script validation

---

Feel free to contribute or leave a ⭐ if you found it helpful!