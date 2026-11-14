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