# Student Tools — ДЗ

Учебный проект на Python 3.10+. Программа вычисляет среднее значение списка оценок и выводит результат с двумя знаками после запятой.

## Запуск на Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Если PowerShell запрещает активацию окружения, можно использовать CMD:
`.venv\Scripts\activate.bat`.

## Запуск на macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Ожидаемый результат:

```text
Средний результат: 4.40
```

## Запуск тестов

```bash
python -m unittest discover -s tests -v
```

Должны успешно пройти три теста.

## Структура проекта

- `main.py` — точка входа для запуска проекта.
- `app/main.py` — логика запуска приложения.
- `app/services/calculater.py` — вычисление среднего значения.
- `app/utils/formatter.py` — форматирование результата.
- `tests/` — автоматические тесты.
- `requirements.txt` — зависимости проекта.

Папка `.venv` создаётся локально и не загружается в Git.
