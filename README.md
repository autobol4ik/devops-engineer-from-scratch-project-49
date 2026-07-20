# Игры разума

### Hexlet tests and linter status:

[![Actions Status](https://github.com/autobol4ik/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/autobol4ik/devops-engineer-from-scratch-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=autobol4ik_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=autobol4ik_devops-engineer-from-scratch-project-49)

«Игры разума» — набор из пяти консольных игр для тренировки базовых
арифметических и логических навыков. В каждой игре нужно правильно ответить
на три вопроса подряд. Первый неправильный ответ завершает игру.

## Требования

- Python 3.10 или новее
- [uv](https://docs.astral.sh/uv/)
- GNU Make

## Установка

```bash
git clone https://github.com/autobol4ik/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
make install
make build
make package-install
```

Команда `uv tool install` устанавливает исполняемые файлы в пользовательский
каталог. Убедитесь, что этот каталог (обычно `~/.local/bin`) добавлен в `PATH`.

## Использование

После установки игры запускаются напрямую из терминала:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

Доступные игры:

| Команда | Игра |
| --- | --- |
| `brain-even` | Проверка числа на чётность |
| `brain-calc` | Вычисление случайного арифметического выражения |
| `brain-gcd` | Поиск наибольшего общего делителя |
| `brain-progression` | Поиск пропущенного элемента прогрессии |
| `brain-prime` | Проверка числа на простоту |

Команда `brain-games` запускает приветствие пользователя.

## Демонстрации

### Проверка на чётность

Установка и сборка пакета, запуск `brain-even`, успешное прохождение и ошибка:

[![Демонстрация brain-even](https://asciinema.org/a/wjzWiD5sfMTR6mYn.svg)](https://asciinema.org/a/wjzWiD5sfMTR6mYn)

### Калькулятор

Успешное и неуспешное прохождение `brain-calc`:

[![Демонстрация brain-calc](https://asciinema.org/a/9ivnIJhGaf7JO4XW.svg)](https://asciinema.org/a/9ivnIJhGaf7JO4XW)

### Наибольший общий делитель

Успешное и неуспешное прохождение `brain-gcd`:

[![Демонстрация brain-gcd](https://asciinema.org/a/CUoFkGPeGRSGqOU8.svg)](https://asciinema.org/a/CUoFkGPeGRSGqOU8)

### Арифметическая прогрессия

Успешное и неуспешное прохождение `brain-progression`:

[![Демонстрация brain-progression](https://asciinema.org/a/0N7JyBvOyxSQfNZg.svg)](https://asciinema.org/a/0N7JyBvOyxSQfNZg)

### Простое ли число?

Успешное и неуспешное прохождение `brain-prime`:

[![Демонстрация brain-prime](https://asciinema.org/a/JrwFGfFB3xnkiffu.svg)](https://asciinema.org/a/JrwFGfFB3xnkiffu)
