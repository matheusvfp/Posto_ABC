# Gerenciamento de Abastecimentos e Tanques de Combustível - Posto ABC ⛽


O sistema de gerenciamento de abastecimentos e tanques de combustíveis do posto ABC visa proporcionar uma experiência intuitiva para os colaboradores. O objetivo é organizar os registros de abastecimentos e a estrutura dos tanques de forma lógica e acessível, facilitando tanto o cadastro quanto a gestão eficiente dos recursos do posto.

## Arquitetura
O projeto foi desenvolvido utilizando Python e Django. A aplicação segue boas práticas de desenvolvimento e padrões de código limpo.

## Funcionalidades Implementadas
- Registro de abastecimentos com identificação da bomba utilizada, quantidade de litros, valor abastecido e imposto de 13%.
- Estruturação dos tanques e bombas de combustível.

## Executando o Projeto

### Pré-requisitos 📋
- Python 3.x
- pip
- Virtualenv

### Passos para Configuração

1. **Clone o repositório**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual**
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o banco de dados**
    ```bash
    python manage.py migrate
    ```

5. **Crie um superusuário para acessar o admin do Django**
    ```bash
    python manage.py createsuperuser
    ```

6. **Inicie o servidor**
    ```bash
    python manage.py runserver
    ```

7. **Acesse a aplicação**
    Abra o navegador e acesse `http://127.0.0.1:8000/admin` para acessar o admin do Django e começar a gerenciar os tanques e abastecimentos.


### Testes
- Foram implementados testes unitários para validar a lógica dos modelos e das funcionalidades.
- Foram implementados testes unitários para as views principais.

## Estrutura do Projeto

- `app_abastecimentos/` - App Django que contém a lógica principal para o gerenciamento de abastecimentos.
- `templates/` - Templates HTML para renderização das páginas.
- `test/` - Arquivos de testes unitários.
- `requirements.txt` - Lista de dependências do projeto.
- `README.md` - Este arquivo com instruções para configuração e execução.

## Apoie o Projeto 🙌
Se você quiser apoiar o projeto, deixe uma ⭐.
______

Made with ❤️ by Matheus
