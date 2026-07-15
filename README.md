# Job Scraper Python

Scraper de ofertas de empleo en Python que utiliza [JobSpy](https://github.com/speedyapply/JobSpy) para consultar múltiples plataformas de búsqueda de empleo (actualmente Indeed y LinkedIn), filtrando por término de búsqueda, antigüedad de la publicación y país. Los resultados se consolidan en un único DataFrame, se eliminan duplicados y se almacenan tanto en una base de datos SQLite como en un archivo CSV.

## Características

- Búsqueda simultánea en múltiples sitios de empleo (Indeed, LinkedIn)
- Filtrado por antigüedad de la publicación (`hours_old`) y país
- Eliminación automática de duplicados por ID de oferta
- Exportación a SQLite (`jobs.db`) y CSV (`jobs.csv`)
- CI/CD con GitHub Actions (lint, tests y scraping automatizado)

## Requisitos

- Python 3.11+ (recomendado; evitar 3.14 por posibles incompatibilidades con numpy/pandas)
- `pandas`
- `python-jobspy`

## Instalación

\`\`\`bash
# Crear y activar entorno virtual

python -m venv venv
venv\Scripts\activate   # Windows
venv/bin/activate   # Linux/Mac

# Instalar dependencias

pip install -r requirements.txt
\`\`\`

## Uso

\`\`\`bash
python main.py
\`\`\`

Editá las variables `searches`, `sites`, `results`, `old` y `country` en `main.py` según tus necesidades de búsqueda.

## Estructura del proyecto

\`\`\`
job-scraper-python/
├── .github/
│   └── workflows/
│       ├── lint.yml
│       ├── tests.yml
│       └── scrape.yml
├── tests/
│   └── test_scraper.py
├── utils/
│   └── scraper.py
├── main.py
├── requirements.txt
├── jobs.db
├── jobs.csv
└── README.md
\`\`\`

## Actualizar dependencias (`requirements.txt`)

\`\`\`bash
pip freeze > requirements.txt
\`\`\`
Se recomienda ejecutar este comando dentro del entorno virtual (`venv`) para evitar incluir paquetes globales ajenos al proyecto.

## GitHub Actions

Este proyecto cuenta con 3 workflows automatizados en `.github/workflows/`:

### 1. `lint.yml` — Linting

Se ejecuta en cada `push` y `pull request`. Verifica el estilo y la sintaxis del código con `ruff`, evitando que se introduzcan errores básicos antes de mergear cambios.

### 2. `tests.yml` — Tests unitarios

Se ejecuta en cada `push` y `pull request`. Corre los tests de `tests/` usando `pytest`, simulando (`mock`) las respuestas de `scrape_jobs` para validar la lógica interna (por ejemplo, el deduplicado de resultados por `id`) sin depender de la disponibilidad real de Indeed/LinkedIn.

### 3. `scrape.yml` — Scraping automatizado

Corre el scraper de forma programada (`cron`, todos los días a las 9am UTC) y también puede dispararse manualmente desde la pestaña **Actions** de GitHub (`workflow_dispatch`). Al finalizar, sube `jobs.csv` y `jobs.db` como **artifacts** descargables desde la misma corrida.

## Próximas mejoras

- [ ] Soporte para proxies (evitar bloqueos 403 en Glassdoor, ZipRecruiter, etc.)
- [ ] Configuración vía archivo `.env` o `config.yaml`
- [ ] Logging estructurado
- [ ] Notificaciones (email/Slack) cuando el scraping automatizado encuentra nuevas ofertas

## Licencia

MIT
