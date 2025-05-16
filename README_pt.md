# Power Automation - Cadastro de Produtos em um Site

Este projeto tem como objetivo automatizar o cadastro de diversos produtos em um site, utilizando duas abordagens diferentes: `PyAutoGUI` e `Selenium`. Cada abordagem possui suas vantagens e limitações, permitindo ao usuário escolher a mais adequada para o seu contexto.

- **PyAutoGUI** simula o uso humano do mouse e teclado, e por isso, requer que o usuário não mexa no computador durante a execução.
- **Selenium** interage diretamente com o HTML da página, o que permite que o script rode em segundo plano e o usuário continue utilizando o computador.

## Tecnologias Utilizadas

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Selenium](https://pypi.org/project/selenium/)
- [pandas](https://pypi.org/project/pandas/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seunome/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o ambiente
- Copie o arquivo `.env.example` e renomeie para `.env`
- Preencha os dados de `login`, `senha` e posições do mouse (para PyAutoGUI)

### 4. Execute um dos scripts

#### ✅ PyAutoGUI Version (não roda em segundo plano)
```bash
python scripts/mouse_position_helper.py
```
- Use esse script para obter as posições do mouse.
- Preencha essas posições no `.env`
- Faça login manualmente no site.
- Depois, execute:
```bash
python scripts/pyautogui_version.py
```

#### ✅ Selenium Version (roda em segundo plano)
- Certifique-se que `.env` contém o login e senha corretamente.
- Depois, execute:
```bash
python scripts/selenium_version.py
```

## 📁 Estrutura de Pastas

```
powerup-automation/
│
├── database/
│   └── db.csv                    # Base de dados com os produtos
│
├── docs/
│   └── PowerUp_Automation_Guide.pdf  # Apostila fornecida
│
├── scripts/
│   ├── mouse_position_helper.py     # Script para identificar posições do mouse
│   ├── pyautogui_version.py         # Script com automação PyAutoGUI
│   └── selenium_version.py          # Script com automação Selenium
│
├── template/
│   └── template.py               # Versão modelo esperada do script
│
├── .env.example                  # Exemplo de variáveis de ambiente
├── .gitignore                   # Arquivos a ignorar pelo Git
├── requirements.txt             # Dependências do projeto
└── README.md                    # Instruções do projeto
```

## 🙋‍♂️ Autor

Este projeto foi desenvolvido durante um intensivão de Python com a [Hashtag Treinamentos](https://portalhashtag.com/) e aprimorado por **Bruno Felipe Passareli**.

---
Sinta-se à vontade para contribuir ou enviar sugestões!