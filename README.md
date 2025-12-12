# Weather API

API simples para consulta de dados climáticos de uma cidade utilizando OpenWeather, PostgreSQL e Flask.

## Estrutura

- `app.py` – lógica da API e extração de dados
- `models.py` – modelo do banco de dados
- `requirements.txt` – dependências Python
- `Dockerfile` – container da API
- `docker-compose.yml` – configuração do ambiente com PostgreSQL
- `.gitignore` – arquivos ignorados pelo Git
- API Flask + PostgreSQL + Docker.

Execute com:
```
docker-compose up --build
```

Endpoint:
- GET /weather
