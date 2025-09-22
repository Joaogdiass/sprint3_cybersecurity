# Challenge Cybersecurity – Sprint 3

## Pipeline
- SAST: Semgrep (`p/security-audit` + `p/python`)
- DAST: OWASP ZAP Baseline (target `http://localhost:8000`)
- SCA: Dependency-Check (CVSS ≥ 7 falha)

## Achados (preencha após o 1º run)
### SAST
- [arquivo/linha] — Risco — Ação

### DAST
- [Alerta] — Evidência/endpoint — Mitigação

### SCA
- [Pacote versão] — CVE — Upgrade sugerido

## Portões de qualidade
- SAST/DAST/SCA falham PR em severidade alta.