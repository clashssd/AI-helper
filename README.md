# Browser Engine

A Python browser-automation project built around Selenium. It provides browser launch and shutdown helpers, reusable browser-profile and session-management components, and a SQLite data layer. The project is under active development.

> **Use responsibly:** Run automation only on websites and accounts you own or are authorized to test. Respect each site's terms of service and access controls. This project is not intended to evade anti-bot protections or access restrictions.

## Features

- Selenium browser launch and shutdown helpers.
- Reusable browser profile configuration for testing.
- Session and cookie management.
- SQLite data-management utilities.
- Pytest test suite, including optional browser integration tests.

## Project structure

```text
AI-helper/
├── browser_engine/
│   ├── BrowserOpen.py       # Browser launch and shutdown
│   ├── session_manager.py   # Session and cookie management
│   └── profile_creator/     # Browser profile configuration
├── database/
│   └── db_manager.py        # SQLite data-management utilities
├── tests/                   # Pytest tests
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- Google Chrome (needed for browser integration tests and browser runs)

## Installation

```bash
git clone https://github.com/clashssd/AI-helper.git
cd AI-helper
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Basic usage

The project exposes browser helpers from `browser_engine`. This example opens a page on a site you are authorized to test and closes the browser reliably:

```python
from browser_engine import run_selenium_engine, close_selenium_engine

driver = run_selenium_engine("https://example.com")

if driver:
    try:
        print(driver.title)
    finally:
        close_selenium_engine(driver)
```

See the modules under `browser_engine/` for the available profile and session-management interfaces.

## Running tests

Run tests that do not require launching a browser:

```bash
pytest tests/ -v -m "not integration"
```

Run the browser integration tests (Chrome required):

```bash
pytest tests/test_browser.py -v -m integration
```

## Security and privacy

- Use test data and authorized accounts only.
- Do not commit credentials, cookies, or other secrets to the repository.
- Avoid storing real passwords in a local database; use a secrets manager or environment variables where credentials are required.
- Treat browser profiles and session data as sensitive, and remove them when no longer needed.

## Русская версия

# Browser Engine

Проект автоматизации браузера на Python с использованием Selenium. Он включает вспомогательные функции для запуска и закрытия браузера, компоненты для повторно используемой конфигурации профилей и управления сессиями, а также слой работы с SQLite. Проект находится в активной разработке.

> **Используйте ответственно:** запускайте автоматизацию только на сайтах и аккаунтах, которыми вы владеете или которые вам разрешено тестировать. Соблюдайте условия использования сайтов и ограничения доступа. Проект не предназначен для обхода антибот-защиты или ограничений доступа.

## Возможности

- Функции запуска и закрытия браузера Selenium.
- Повторно используемая конфигурация профиля браузера для тестирования.
- Управление сессиями и cookies.
- Утилиты для работы с данными в SQLite.
- Набор тестов pytest, включая необязательные интеграционные тесты с браузером.

## Структура проекта

```text
AI-helper/
├── browser_engine/
│   ├── BrowserOpen.py       # Запуск и закрытие браузера
│   ├── session_manager.py   # Управление сессиями и cookies
│   └── profile_creator/     # Конфигурация профилей браузера
├── database/
│   └── db_manager.py        # Утилиты для работы с данными SQLite
├── tests/                   # Тесты pytest
├── requirements.txt
└── README.md
```

## Требования

- Python 3
- Google Chrome (для запуска браузера и интеграционных тестов)

## Установка

```bash
git clone https://github.com/clashssd/AI-helper.git
cd AI-helper
python -m venv .venv
```

Активируйте виртуальное окружение:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows Command Prompt
.venv\Scripts\activate.bat

# Linux/macOS
source .venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

## Пример использования

В проекте доступны функции управления браузером из `browser_engine`. Пример открывает страницу сайта, который вы уполномочены тестировать, и гарантированно закрывает браузер:

```python
from browser_engine import run_selenium_engine, close_selenium_engine

driver = run_selenium_engine("https://example.com")

if driver:
    try:
        print(driver.title)
    finally:
        close_selenium_engine(driver)
```

Интерфейсы профилей и управления сессиями см. в модулях каталога `browser_engine/`.

## Запуск тестов

Запуск тестов, которым не требуется браузер:

```bash
pytest tests/ -v -m "not integration"
```

Запуск интеграционных тестов браузера (требуется Chrome):

```bash
pytest tests/test_browser.py -v -m integration
```

## Безопасность и конфиденциальность

- Используйте только тестовые данные и аккаунты, автоматизация которых разрешена.
- Не добавляйте в репозиторий пароли, cookies и другие секреты.
- Не храните реальные пароли в локальной базе данных; если учетные данные необходимы, используйте менеджер секретов или переменные окружения.
- Считайте профили браузера и данные сессий конфиденциальными и удаляйте их, когда они больше не нужны.
