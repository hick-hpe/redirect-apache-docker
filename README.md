
# REDIRECT-APACHE-DOCKER

## Sobre o projeto

O projeto **REDIRECT-APACHE-DOCKER** é uma aplicação com dois containers: um frontend e um backend. O objetivo é permitir acesso externo apenas ao frontend, protegendo a api. O backend é acessível apenas pelo frontend.

## Funcionalidades

-   Uma API backend em Flask 
    
-   Uma interface minimalista em HTML/Apache
       

## Tecnologias utilizadas

-   `Flask` (Python) para o backend
    
-   `Docker` para orquestração de containers
   
-   `HTML/JS` para o frontend
    
-   `Apache HTTPD` como serviço adicional simulado
    
-   `Docker Compose` para facilitar a organização dos serviços
    

## Estrutura de pastas

```
redirect-apache-docker/
├── api/       
│   └── app.py
│   └── Dockerfile
├── frontend/       
│   └── Dockerfile
│   └── index.html
│   └── my-proxy.conf
├── docker-compose.yml
├── requirements.txt
```

## Instalação

### Pré-requisitos

-   [Docker](https://www.docker.com/)
    
-   Docker Compose
    

### Passos

1.  Clone o repositório: 
   ```
   git clone https://github.com/hick-hpe/redirect-apache-docker.git
   cd redirect-apache-docker
 ```

2. Inicie os containers:
```
docker-compose up --build
``` 

## Executar o projeto

-   Frontend HTML/JS: acessível via `http://localhost:3000`
    

## Autor

Henrique Palermo Emerick
