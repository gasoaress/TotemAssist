
# 🏥 TotemAssist - Automação Inteligente com OCR para Sistema Tasy

**TotemAssist** é um sistema de automação que utiliza **OCR** (Reconhecimento Óptico de Caracteres) e **Selenium WebDriver** para interagir automaticamente com a interface do sistema hospitalar **Tasy**, da **Unimed**.  
O projeto foi desenvolvido para agilizar o uso de totens de autoatendimento, executando ações com base nas informações exibidas na tela.

---

## ⚙️ Funcionalidades

- 🧠 Reconhecimento de texto na interface gráfica via captura de tela (OCR com EasyOCR)
- 🤖 Automação da navegação no Tasy usando Selenium WebDriver
- 🔐 Preenchimento automático de credenciais de login
- 🖱️ Ações baseadas em contexto da tela (ex: clique em “Autoatendimento” ou “Monitor”)
- 🛡️ Identificação de falhas e recuperação automática (reload da interface)
- 📸 Captura de tela para análise e decisão automatizada

---

## 📌 Tecnologias Utilizadas

- Python 3.x
- Selenium
- EasyOCR
- Pillow (PIL)

---

## 🛠️ Pré-requisitos

- Python instalado
- Google Chrome instalado
- Pacotes Python instalados:

```bash
pip install selenium easyocr pillow
```

### Estrutura de pastas esperada:

- Perfil do Chrome em: `C:\selenium\ChromeProfile`
- Chrome em: `C:\Program Files\Google\Chrome\Application\chrome.exe`


## 🚀 Como Executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/TotemAssist.git
cd TotemAssist
```

Execute o script principal:

```bash
python TasyClicker.pyw
```

> O script abrirá o navegador, realizará o login e navegará pela interface do Tasy.

---

## 📄 Estrutura do Código - Check_AutoAtendimento.pyw

- `iniciar_driver_e_logar()`: Inicia o navegador e realiza login automático no Tasy.
- **OCR + Selenium**: Captura uma screenshot da tela e usa EasyOCR para detectar textos.
- **Lógica condicional**: Verifica palavras-chave como `"autoatendimento"`, `"monitor"` e `"senha"` para realizar ações automatizadas.

---

## 🧪 Exemplo de Fluxo

1. A página é carregada  
2. Uma imagem da tela é capturada  
3. O OCR detecta uma palavra-chave  
4. O Selenium encontra o botão correspondente e **clica automaticamente**  

---

## 📌 Observações

- É necessário que o sistema Tasy esteja acessível em uma URL.
- Certifique-se de que o Chrome **não esteja bloqueando pop-ups ou janelas automáticas**.
- A automação depende da estrutura **HTML da página**, que pode mudar com atualizações do sistema.
