PROJETO STREAMLIT EM EC2 - ACESSO PÚBLICO VIA NAVEGADOR

OBJETIVO : 

Criar uma aplicação web simples usando Streamlit, hospedada em uma instância EC2 (Ubuntu 22.04 ou superior) da AWS, com acesso público por meio do navegador.

REQUISITOS : 
 - Conta na AWS ativa
 - Chave de acesso .pem
 - Git instalado na máquina local
  - Navegador web (Chrome, Firefox, etc.)

INSTRUÇÕES PARA RODAR LOCALMENTE NA EC2: 
 - Acesse o painel da AWS e crie uma instância Ubuntu 22.04.
 - Tipo sugerido: t2.micro (uso gratuito elegível).
Durante a criação:
 - Selecione ou crie um par de chaves (.pem).
 - No grupo de segurança, libere as portas:
22 – para acesso via SSH
8501 – para o Streamlit

CONECTAR VIA SSH:
Pelo terminal local,execute:
chmod 400 sua-chave.pem 
ssh -i "sua-chave.pem" ubuntu@<IP PÚBLICO-DA-INSTÂNCIA>

3.INSTALAR O PYTHON, PIP. E DEPENDÊNCIAS: 

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
pip install streamlit pandas matplotlib

4.ENVIAR O PROJETO PARA A INSTÂNCIA:
Usando git, na instância ec2:

sudo apt install git -y
git clone <URL-DO-REPOSITÓRIO>
cd <nome-do-repositório>

Opção 2-  usando scp:

scp -i sua-chave.pem app.py ubuntu@<IP-PÚBLICO>:/home/ubuntu/
scp -i sua-chave.pem dataset.csv ubuntu@<IP-PÚBLICO>:/home/ubuntu/

1. EXECUTAR A APLICAÇÃO:
Dentro da pasta do projeto (onde está app.py):

streamlit run app.py --server.port=8501 --server.address=0.0.0.0

6.ACESSAR NO NAVEGADOR:

http://<IP-PÚBLICO-DA-INSTÂNCIA>:8501

Rodando Localmente (Máquina Pessoal)
Pode executar na própria máquina 
Pré-requisitos
- Python 3.8+
- pip
- Streamlit

PASSOS: 
Clonar o projeto:

git clone <URL-DO-REPOSITÓRIO>
cd <nome-do-repositório>

INSTALAR AS DEPENDÊNCIAS:

pip install -r requirements.txt

EXECUTE O APP:

streamlit run app.py

PELO NAVEGADOR:

http://localhost:8501

ENTREGA:

- Captura de tela do terminal na EC2 com app rodando
 - Captura de tela da aplicação no navegador
- Código-fonte (app.py) no GitHub
- Link da aplicação via IP público da instância

DICAS: 

Use htop ou top para monitorar consumo na EC2.
Sempre valide se as bibliotecas foram instaladas com sucesso.
Para reiniciar a aplicação, use Ctrl+C no terminal da EC2 e execute o comando novamente.
Para evitar erros de permissão, sempre use chmod 400 na sua chave .pem.
