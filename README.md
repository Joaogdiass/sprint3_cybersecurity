# Sprint 3 Cybersecurity — Starter Kit

Este repo mínimo te dá SAST (Semgrep), DAST (OWASP ZAP) e SCA (Dependency-Check) prontos no GitHub Actions,
mesmo sem ter um projeto existente. Inclui uma app Flask simples.

## Como usar

1) Crie um repositório no GitHub e faça upload de todos os arquivos deste kit (ou dê push com git).
2) Vá em **Actions** (no GitHub) e ative workflows se for solicitado.
3) Faça um commit/push em `main` ou abra um Pull Request para disparar:
   - SAST — Semgrep
   - DAST — ZAP Baseline (vai subir a app Flask no CI)
   - SCA — Dependency-Check

### Rodar local (opcional)

Crie um Python venv e instale dependências:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/app.py
# acesse http://localhost:8000
```

ZAP Baseline local (requer Docker):
```bash
docker run --rm -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:8000 -r zap-baseline.html
```

Edite **SECURITY-REPORT.md** depois do primeiro run com os achados e ações.

## Estrutura
- app/app.py — pequena aplicação Flask (porta 8000)
- requirements.txt — dependências
- .github/workflows/ — CI (SAST/DAST/SCA)
- SECURITY-REPORT.md — modelo de relatório
- zap-rules.tsv — supressões/downgrades do ZAP
```