# AI-helper — Browser Automation Framework

**English** | [Русская версия](#русская-версия)

AI-helper is a Python framework for building browser-automation and AI-assisted workflows. It brings together Selenium browser helpers, configurable browser profiles, session utilities, proxy configuration, and an LLM-backed orchestrator that can delegate tasks to specialized agents and interact with page elements.

Use it as a foundation for **authorized QA, UI testing, and automation in systems you own or have permission to test**. Extend the components to fit your project, and keep a human in the loop for consequential actions.

> **Responsible use:** Automate only websites, accounts, and environments where you have explicit authorization. Follow applicable terms, rate limits, privacy requirements, and access controls. Browser-profile configuration is intended for controlled testing and compatibility work—not for disguising automation, evading bot detection, bypassing CAPTCHAs, or circumventing a site's restrictions. This project does not guarantee that automation will go undetected or be accepted by any website.

## Features

- Selenium-based Chrome launch and shutdown helpers.
- Browser profile schemas, options, and presets for controlled compatibility testing.
- Cookie/session utilities and session persistence for orchestrated runs.
- Proxy configuration support for authorized test environments.
- An OpenAI-compatible LLM client configurable with an API key, base URL, and model.
- An agent orchestrator with task delegation and browser UI tools, including page inspection, text entry, clicks, and dropdown selection.
- SQLite-backed browser data utilities and pytest coverage.

## Repository layout

```text
AI-helper/
├── ai_engine/
│   ├── LLMclient.py
│   └── orchestrator/       # Agent definitions, tools, sessions, orchestration
├── browser_engine/
│   ├── BrowserOpen.py      # Selenium browser lifecycle
│   ├── SessionManager.py   # Cookie/session utilities
│   ├── database/           # SQLite data utilities
│   └── profile_creator/    # Profile schemas, presets, options
├── network/                # Proxy configuration helpers
├── tests_browser_engine/   # Browser-engine tests
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- Google Chrome and a compatible Selenium setup for browser runs
- An API key and an OpenAI-compatible endpoint/model when using the AI client

Some optional image-processing integrations may need additional system software. Install and configure those only if your authorized test workflow requires them.

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

Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Keep API keys and other secrets in environment variables or a secrets manager. Never commit them to the repository.

## Browser helper example

The public browser helpers can open a page and close the driver reliably. Use a URL in a test environment you are authorized to automate:

```python
from browser_engine import run_selenium_engine, close_selenium_engine

driver = run_selenium_engine("https://example.com")
if driver:
    try:
        print(driver.title)
    finally:
        close_selenium_engine(driver)
```

The browser launcher also accepts optional profile and proxy configuration. Review the corresponding modules before using them, and do not use profile settings or network routing to bypass a website's protections or policies.

## AI-assisted orchestration

The `ai_engine` package provides an `AIClient` and an `Orchestrator` for LLM-assisted UI workflows. Configure the client with an API key, compatible base URL, and model, then use the orchestrator only against a controlled test system. LLM output can be incorrect or unpredictable: validate actions, limit the agent's permissions, use test accounts and data, and supervise runs. Avoid submitting personal, confidential, or production data to an LLM unless your organization has approved that use.

The orchestrator and browser integrations are evolving; check the current module interfaces and tests before relying on them in a production workflow.

## Tests

Run the browser-engine test suite:

```bash
pytest tests_browser_engine/ -v
```

Tests that launch Chrome require a working browser installation. Consult `tests_browser_engine/pytest.ini` for test configuration and markers.

## Security and privacy

- Use only authorized test environments and accounts.
- Do not use the framework to evade access controls, bot-detection systems, rate limits, or other site restrictions.
- Do not commit credentials, API keys, cookies, proxy credentials, or browser profiles.
- Treat session files, browser profiles, logs, and test data as sensitive; protect and delete them when no longer needed.
- Prefer disposable test accounts and synthetic data. Review any external AI provider's data-handling terms before sending content.
- Add safeguards and explicit approval steps before allowing automation to perform consequential actions.

---

# Русская версия

AI-helper — Python-фреймворк для создания сценариев автоматизации браузера и процессов с участием ИИ. Он объединяет вспомогательные средства Selenium, настраиваемые профили браузера, работу с сессиями, конфигурацию прокси и оркестратор на базе LLM, который может делегировать задачи специализированным агентам и взаимодействовать с элементами страниц.

Используйте проект как основу для **авторизованного QA, тестирования интерфейсов и автоматизации систем, которыми вы владеете или которые имеете право тестировать**. Адаптируйте компоненты под свой проект и сохраняйте контроль человека над важными действиями.

> **Ответственное использование:** автоматизируйте только сайты, аккаунты и среды, для которых у вас есть явное разрешение. Соблюдайте условия использования, ограничения частоты запросов, требования к конфиденциальности и механизмы контроля доступа. Настройки профиля браузера предназначены для контролируемого тестирования и проверки совместимости, а не для маскировки автоматизации, обхода систем обнаружения ботов, CAPTCHA или ограничений сайта. Проект не гарантирует, что автоматизация останется незамеченной или будет принята каким-либо сайтом.

## Возможности

- Запуск и корректное закрытие Chrome через Selenium.
- Схемы, параметры и готовые профили браузера для контролируемой проверки совместимости.
- Утилиты для работы с cookies и сессиями, а также сохранение сессий оркестратора.
- Поддержка конфигурации прокси для авторизованных тестовых сред.
- Клиент LLM, совместимый с OpenAI API и настраиваемый через API-ключ, базовый URL и модель.
- Оркестратор агентов с делегированием задач и инструментами браузера: просмотр элементов страницы, ввод текста, нажатия и выбор пунктов меню.
- Утилиты работы с данными SQLite и тесты pytest.

## Структура репозитория

```text
AI-helper/
├── ai_engine/
│   ├── LLMclient.py
│   └── orchestrator/       # Агенты, инструменты, сессии и оркестрация
├── browser_engine/
│   ├── BrowserOpen.py      # Управление жизненным циклом Selenium-браузера
│   ├── SessionManager.py   # Утилиты cookies и сессий
│   ├── database/           # Утилиты SQLite
│   └── profile_creator/    # Схемы, пресеты и параметры профилей
├── network/                # Вспомогательные средства конфигурации прокси
├── tests_browser_engine/   # Тесты браузерного движка
├── requirements.txt
└── README.md
```

## Требования

- Python 3
- Google Chrome и совместимая конфигурация Selenium для запуска браузера
- API-ключ и совместимые endpoint/модель OpenAI API при использовании AI-клиента

Для некоторых необязательных интеграций обработки изображений может потребоваться дополнительное системное ПО. Устанавливайте и настраивайте его только при необходимости для разрешённых тестовых сценариев.

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

Установите зависимости Python:

```bash
python -m pip install -r requirements.txt
```

Храните API-ключи и другие секреты в переменных окружения или менеджере секретов. Не добавляйте их в репозиторий.

## Пример работы с браузером

Публичные вспомогательные функции позволяют открыть страницу и корректно закрыть драйвер. Используйте URL тестовой среды, автоматизировать которую вам разрешено:

```python
from browser_engine import run_selenium_engine, close_selenium_engine

driver = run_selenium_engine("https://example.com")
if driver:
    try:
        print(driver.title)
    finally:
        close_selenium_engine(driver)
```

Загрузчик браузера также принимает необязательные настройки профиля и прокси. Перед использованием изучите соответствующие модули и не применяйте настройки профиля или маршрутизацию трафика для обхода средств защиты и правил сайта.

## Автоматизация с помощью ИИ

Пакет `ai_engine` предоставляет `AIClient` и `Orchestrator` для LLM-управляемых сценариев работы с интерфейсом. Настройте клиент с API-ключом, совместимым базовым URL и моделью, а оркестратор запускайте только против контролируемой тестовой системы. Ответы LLM могут быть ошибочными или непредсказуемыми: проверяйте действия, ограничивайте права агента, используйте тестовые аккаунты и данные и контролируйте выполнение. Не передавайте персональные, конфиденциальные или производственные данные внешней LLM, если такое использование не одобрено вашей организацией.

Интерфейсы оркестратора и браузерных интеграций развиваются; перед использованием в производственном процессе проверьте актуальные модули и тесты.

## Тесты

Запустите тесты браузерного движка:

```bash
pytest tests_browser_engine/ -v
```

Тесты, запускающие Chrome, требуют установленного и настроенного браузера. Настройки тестов и маркеры см. в `tests_browser_engine/pytest.ini`.

## Безопасность и конфиденциальность

- Используйте только тестовые среды и аккаунты, автоматизация которых разрешена.
- Не используйте фреймворк для обхода контроля доступа, систем обнаружения ботов, ограничений частоты запросов или иных ограничений сайта.
- Не добавляйте в репозиторий пароли, API-ключи, cookies, учетные данные прокси и профили браузера.
- Считайте файлы сессий, профили браузера, логи и тестовые данные конфиденциальными; защищайте и удаляйте их, когда они больше не нужны.
- По возможности используйте временные тестовые аккаунты и синтетические данные. Перед передачей данных проверьте условия обработки данных внешним AI-провайдером.
- Добавляйте меры защиты и явное подтверждение пользователя перед действиями с серьёзными последствиями.
