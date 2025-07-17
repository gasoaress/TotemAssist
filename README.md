🏥 TotemAssist - Automação Inteligente com OCR para Sistema Tasy
TotemAssist é um sistema de automação que utiliza OCR (Reconhecimento Óptico de Caracteres) e Selenium WebDriver para interagir automaticamente com a interface do sistema hospitalar Tasy, da Unimed. O projeto foi desenvolvido para agilizar o uso de totens de autoatendimento, executando ações com base nas informações exibidas na tela.

⚙️ Funcionalidades
🧠 Reconhecimento de texto na interface gráfica via captura de tela (OCR com EasyOCR)

🤖 Automação da navegação no Tasy usando Selenium WebDriver

🔐 Preenchimento automático de credenciais de login

🖱️ Ações baseadas em contexto da tela (ex: clique em “Autoatendimento” ou “Monitor”)

🛡️ Identificação de falhas e recuperação automática (reload da interface)

📸 Captura de tela para análise e decisão automatizada

📌 Tecnologias Utilizadas
Python 3.x

Selenium

EasyOCR

Pillow (PIL)

🛠️ Pré-requisitos
Python instalado

Google Chrome instalado

Pacotes Python instalados:

bash
Copiar
Editar
pip install selenium easyocr pillow
Estrutura de pastas esperada:

Perfil do Chrome em: C:\selenium\ChromeProfile

Chrome em: C:\Program Files\Google\Chrome\Application\chrome.exe

🚀 Como executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/TotemAssist.git
cd TotemAssist
Execute o script principal:

bash
Copiar
Editar
python totem_automation.py
O script abrirá o navegador, realizará o login e navegará pela interface do Tasy conforme as palavras-chave detectadas na imagem capturada da tela.

📄 Estrutura do Código
iniciar_driver_e_logar(): Inicia o navegador e realiza login automático no Tasy.

OCR + Selenium: Captura uma screenshot da tela e usa EasyOCR para detectar textos.

Lógica condicional: Verifica palavras-chave como "autoatendimento", "monitor" e "senha" para realizar ações automatizadas.

🧪 Exemplo de Fluxo
A página é carregada

Uma imagem da tela é capturada

O OCR detecta a palavra "autoatendimento"

O Selenium encontra o botão correspondente e clica automaticamente

📌 Observações
É necessário que o sistema Tasy esteja acessível no endereço: https://tasy.unimedpc.coop.br/#/

Certifique-se de que o Chrome não esteja bloqueando pop-ups ou janelas automáticas.

A automação depende da estrutura HTML da página, que pode mudar com atualizações do sistema.
