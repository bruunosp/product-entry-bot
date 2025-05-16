
# 🚀 Power Automation - Bot de Cadastro de Produtos

Este projeto automatiza o cadastro de múltiplos produtos em um site.

Dois scripts diferentes foram desenvolvidos para esse propósito:

- ✅ **Versão Selenium** – roda em segundo plano utilizando elementos HTML (recomendado).
- ✅ **Versão PyAutoGUI** – usa automação de mouse/teclado e requer controle total da sua tela.

---

## 📌 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Selenium](https://selenium.dev/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/yourusername/your-project.git
cd your-project
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Crie o arquivo `.env`

```bash
# Copie o arquivo de exemplo e preencha com suas credenciais
cp .env.example .env
```

---

## ▶️ Executando o Projeto

### 🖱️ Versão PyAutoGUI (apenas em primeiro plano)

> ⚠️ **Não** mova o mouse ou digite enquanto o script estiver rodando.

1. Acesse o site: [Hashtag Cadastro](https://dlp.hashtagtreinamentos.com/python/intensivao/login)
2. Rode o script auxiliar:

```bash
python scripts/mouse_position_helper.py
```

3. Passe o mouse sobre o campo **Email** para capturar as coordenadas.
4. Atualize o seu arquivo `.env`:
   ```env
   MOUSE_POSITION_X_EMAIL=xxx
   MOUSE_POSITION_Y_EMAIL=yyy
   ```

5. Faça login manualmente no site.
6. Repita o processo para o campo **Código do Produto**:
   ```env
   MOUSE_POSITION_X_CODIGO=xxx
   MOUSE_POSITION_Y_CODIGO=yyy
   ```

7. Rode a versão PyAutoGUI:

```bash
python scripts/pyautogui_version.py
```

---

### 🌐 Versão Selenium (recomendada ✅)

1. Certifique-se de que o seu `.env` inclui:
   ```env
   LOGIN=seu_email@example.com
   PASSWORD=sua_senha
   ```

2. Rode a versão Selenium:

```bash
python scripts/selenium_version.py
```

---

## 📁 Estrutura do Projeto

```
powerup-automation/
│
├── database/
│   └── db.csv                    # Fonte de dados dos produtos
│
├── docs/
│   └── PowerUp_Automation_Guide.pdf   # Guia do projeto
│
├── scripts/
│   ├── mouse_position_helper.py  # Script auxiliar para PyAutoGUI
│   ├── pyautogui_version.py      # Script baseado em PyAutoGUI
│   └── selenium_version.py       # Script baseado em Selenium
│
├── template/
│   └── template.py               # Script de referência
│
├── .env.example                  # Exemplo de variáveis de ambiente
├── .gitignore                    # Arquivos ignorados pelo Git
├── requirements.txt              # Lista de dependências
└── README.md                     # Documentação do projeto
```

---

## 🙋‍♂️ Autor

Projeto criado durante o bootcamp de Python da [Hashtag Treinamentos](https://portalhashtag.com/) e aprimorado por **Bruno Felipe Passareli** com automação em segundo plano e manipulação segura com Selenium.

---

## 🧠 Melhorias Futuras

- Interface para capturar coordenadas do mouse
- Tratamento seguro de credenciais
- Testes unitários para validação dos scripts

---

Sinta-se livre para contribuir ou deixar uma ⭐ se achou útil!
