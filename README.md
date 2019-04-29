# Django Study

[TOC]

# Install Ambient

No Linux/Ubuntu não precisamos instalar Python, porque já é nativo em sistemas operacionais baseados em Unix, mas para termos certeza basta executar o comando no terminal:

```
$ python –version
```

o resultado será:

```
Python 3.6.*
```

Vamos começar instalando os pacotes necessários no Sistema Operacional:

```
$ sudo apt-get update
$ sudo apt-get install python-dev python-setuptools
$ sudo apt install python3-venv
$ sudo apt install pip
```

Para testarmos se o virtualenv está instalado corretamente executaremos no terminal:

# Create the Project

Agora vamos entrar dentro do ambiente virtual que criamos e vamos ativá-lo:

```
$ mkdir python-project
$ cd python-project/
$ python3 -m venv nome_projeto
$ source nome_projeto/bin/activate
```

Neste momento temos o ambiente virtual criado e ativado, pronto para instalar o **django**:

```
$ pip install django
```

Quando executamos o comando **pip install django** sem especificarmos a versão desejada, o pip instala a ultima versão disponivel. Se quizermos instalar uma versão específica devemos executar assim:

```
$ pip install django==1.5.4
```

Então podemos finalmente criar o projeto django executando o seguinte comando:

```
$ django-admin startproject first_django_project
```