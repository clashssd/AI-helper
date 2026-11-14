# Browser Engine

**Browser Engine** is a module for advanced browser automation (Selenium) that supports the generation of anti-detect profiles, fingerprint spoofing, and session management.

The project is currently under active development. The current version includes a core for launching the browser, generating unique profiles, and injecting JavaScript to bypass basic anti-bot protection systems.

## Key Features (Current)

*   **Profile Generator (Anti-Detect):** Creates unique digital fingerprints based on 50+ realistic presets (Windows, macOS, Linux, Android, iOS).
*   **Smart Jitter:** Randomizes parameters (CPU cores, RAM, screen resolution) while maintaining the logical consistency of the device configuration.
*   **WebGL and Canvas Spoofing:** Masks the graphics card and other rendering parameters by injecting JavaScript before the page loads.
*   **Session Management:** Persists cookies and cache using `user-data-dir` to maintain authentication across sessions.
*   **Database:** Logs account information (usernames, passwords, statuses) into a local SQLite database. ## Project Structure

```text
AI-helper/
├── browser_engine/          # Browser engine core
│   ├── BrowserOpen.py       # Launching and closing the browser
│   ├── session_manager.py   # Cookie management (saving/loading)
│   └── profile_creator/     # Profile generation
│       ├── ProfileSchema.py # Profile data schema (dataclass)
│       ├── Presets.py       # Database of 50+ device presets
│       ├── BuilderProfile.py# Logic for creating unique profiles
│       └── OptionsBuilder.py# Generation of ChromeOptions and JS scripts
├── database/                # Database operations (SQLite)
│   └── db_manager.py        # Account management functions
├── tests/                   # Unit tests (pytest)
├── requirements.txt         # Dependencies
└── README.md                # Documentation
```
## Installation
```code
1. Clone the repository
git clone https://github.com/your_username/AI-helper.git
cd AI-helper
2. Create and activate a virtual environment:
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
3. Install dependencies:
pip install -r requirements.txt
```
## Usage Example:
```code
from browser_engine.profile_creator import BuilderProfile
from browser_engine import run_selenium_engine, close_selenium_engine
from database import add_account

# 1. Generate a random anti-detect profile (e.g., MacBook)
profile = BuilderProfile.build_profile(preset_name="mac_m1_air")
print(f"Launching profile: {profile.profile_name}")

# 2. Save the account to the database (if necessary)
add_account(profile.profile_id, "https://example.com", "my_login", "my_password")

# 3. Open the browser with fingerprint masking
driver = run_selenium_engine("https://browserleaks.com/webgl", profile=profile)

if driver:
try:
# Perform your actions on the website
input("Press Enter to close the browser...")
finally:
close_selenium_engine(driver)
```
## Running tests
``` code
# Quick tests (without launching an actual browser)
pytest tests/ -v -m "not integration"

# Tests involving an actual Chrome launch
pytest tests/test_browser.py -v -m integration
```
# Disclaimer
This tool is created solely for educational purposes. The author is not responsible for any misuse of this code.
## Ru версия
# Browser Engine

**Browser Engine** — это модуль для продвинутой автоматизации браузера (Selenium) с поддержкой генерации антидетект-профилей, маскировки отпечатков (Fingerprint Spoofing) и управления сессиями.

Проект находится в активной разработке. Текущая версия включает в себя ядро для запуска браузера, генерации уникальных профилей и внедрения JavaScript-скриптов для обхода базовых систем антибот-защиты.

## Основные возможности (Текущие)

*   **Генератор профилей (Anti-Detect):** Создание уникальных цифровых отпечатков на основе 50+ реалистичных пресетов (Windows, macOS, Linux, Android, iOS).
*   **Умный джиттер:** Рандомизация параметров (ядра CPU, RAM, разрешение экрана) без нарушения логической связности устройств.
*   **Маскировка WebGL и Canvas:** Подмена видеокарты и других параметров рендеринга через внедрение JS-скриптов до загрузки страницы.
*   **Управление сессиями:** Сохранение куки и кэша с помощью `user-data-dir` для поддержания авторизации между запусками.
*   **База данных:** Логирование аккаунтов (логины, пароли, статусы) в локальную БД SQLite.

## Структура проекта

```text
AI-helper/
├── browser_engine/          # Ядро движка браузера
│   ├── BrowserOpen.py       # Запуск и закрытие браузера
│   ├── session_manager.py   # Работа с куки (сохранение/загрузка)
│   └── profile_creator/     # Генерация профилей
│       ├── ProfileSchema.py # Схема данных профиля (dataclass)
│       ├── Presets.py       # База из 50+ пресетов устройств
│       ├── BuilderProfile.py# Логика создания уникального профиля
│       └── OptionsBuilder.py# Генерация ChromeOptions и JS-скриптов
├── database/                # Работа с БД (SQLite)
│   └── db_manager.py        # Функции управления аккаунтами
├── tests/                   # Юнит-тесты (pytest)
├── requirements.txt         # Зависимости
└── README.md                # Документация
```
## Установка
```code
1. Клонируйте репозиторий
git clone https://github.com/ваш_никнейм/AI-helper.git
cd AI-helper
2. Создайте виртуальное окружение и активируйте его:
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
3.Установите зависимости:
pip install -r requirements.txt
```
## Пример использования:
```code
from browser_engine.profile_creator import BuilderProfile
from browser_engine import run_selenium_engine, close_selenium_engine
from database import add_account

# 1. Генерируем случайный антидетект-профиль (например, MacBook)
profile = BuilderProfile.build_profile(preset_name="mac_m1_air")
print(f"Запускаем профиль: {profile.profile_name}")

# 2. Записываем аккаунт в БД (при необходимости)
add_account(profile.profile_id, "https://example.com", "my_login", "my_password")

# 3. Открываем браузер с маскировкой
driver = run_selenium_engine("https://browserleaks.com/webgl", profile=profile)

if driver:
    try:
        # Ваши действия на сайте
        input("Нажмите Enter для закрытия браузера...")
    finally:
        close_selenium_engine(driver)
```
## Запуск тестов
``` code
# Быстрые тесты (без запуска реального браузера)
pytest tests/ -v -m "not integration"

# Тесты с реальным запуском Chrome
pytest tests/test_browser.py -v -m integration
```
# Дисклеймер
Данный инструмент создан исключительно в образовательных целях.Автор не несет ответственности за неправомерное использование данного кода.