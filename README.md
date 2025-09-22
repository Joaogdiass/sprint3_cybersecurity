# Sprint 3 — Cybersecurity  

## 📌 Descrição  
Este repositório contém os artefatos desenvolvidos como parte da **Sprint 3** da disciplina de **Cybersecurity**.  
O foco principal foi a implementação e documentação de testes de segurança, incluindo **SAST** (Static Application Security Testing), **DAST** (Dynamic Application Security Testing) e **SCA** (Software Composition Analysis).  

---

## 👨‍💻 Equipe  
- Júlio César Zampieri — RM98772  
- Gustavo Melo — RM98809  
- Carlos Augusto Campos Ganzerli — RM99840  
- Lucas Carlos Bandeira Teixeira — RM98640  
- João Gabriel Dias — RM99092  

---

## 🛠️ Atividades Realizadas  
- Configuração de **pipeline de CI/CD** com ferramentas de segurança.  
- Execução de **SAST** (análise estática de código) para identificação de vulnerabilidades no código-fonte.  
- Execução de **DAST** (análise dinâmica) com OWASP ZAP para validação da aplicação em execução.  
- Execução de **SCA** (análise de dependências) para detecção de bibliotecas vulneráveis.  
- Registro de **achados de segurança** em relatório consolidado.  

---

## 📑 Estrutura do Repositório  
- `.github/workflows/` → pipelines configurados no GitHub Actions (SAST, DAST, SCA).  
- `SECURITY-REPORT.md` → relatório com os resultados das análises de segurança.  
- `README.md` → este documento de apresentação.  

---

## ✅ Como Utilizar  
1. Acesse a aba **Actions** no GitHub para acompanhar a execução dos testes.  
2. Consulte os resultados em:  
   - **SAST** → GitHub Security (Code scanning alerts).  
   - **DAST** → Issue automático criado pelo ZAP + logs do workflow.  
   - **SCA** → Artifact `dependency-check-report.html` disponível nos workflows.  
3. Preencha o arquivo **SECURITY-REPORT.md** com os achados e recomendações.  

---

## 📌 Observações  
- Os testes foram realizados em ambiente controlado, conforme orientações da Sprint.  
- O objetivo é demonstrar a aplicação prática de ferramentas de segurança no ciclo de desenvolvimento de software.  
