# Base de gestão de  arquivos para Scrapping

## Scrapping manager

Base de gerenciador de arquivos voltado para Scrapping! Sistema que permite que você só pense em quais informações você irar fazer o Scrapping, deixando que o lado de configuração de arquivos a aplicação se autogerencie.

## O que o projeto contém
- Scrapping em python
- A base de WinAppDriver (Driver de Scrapping da própria Microsoft para o Windows)
- Pré-adaptação para Scrapping via Browser em Selenium (driver de navegadores não incluso)

## Instalação
Para rodar o projeto faça essas configurações:
- Clone o projeto (utilizando comando git ou baixando em zip)
- Instale o Python (recomendado versão 3.8)
- Instale WinAppDriver (ou um driver para browser)
- Instale a biblioteca que se encontra em requirements
```
python -m pip install -U pip setuptools
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Configure o arquivo Config para rodar em ambiente local
```
LOCAL=True
```

## Resultados & O que é esperado
O que é esperado depende dos resultados gerado através do Scrapping, que será processado em gravado em arquivos pré-determinado.
