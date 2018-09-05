

### O Problema

Elabore uma solução que ofereça armazenamento, processamento e disponi-
bilização desses dados, sempre considerando que tudo deve estar conforme as boas práticas de
segurança em TI. Afinal, nosso principal ativo são dados sensíveis dos consumidores brasileiros.

### Solução
	
Como primeiro passo na busca da solução, busquei por ferramentas que se encaixassem e suprissem as necessidades apontadas em cada etapa, passando por armazenamento, tráfego e a Disponibilização dos dados, sempre focando na agilidade e segurança. 
Segue abaixo em detalhes cada escolha e o porquê de cada uma delas com detalhes e referências.

### Arquitetura 
![arquitetura](https://github.com/JonnatasCabral/desafioSC/blob/master/imagens/arquitetura.jpg)

###  Armazenamento:

Base A: 
	
- Para as necessidades da base A necessidades podemos utilizar O Amazon Relational Database Service (Amazon RDS) que facilita configurar, operar e escalar bancos de dados relacionais na nuvem. O serviço oferece capacidade econômica e redimensionável e automatiza tarefas demoradas de administração, como provisionamento de hardware, configuração de bancos de dados, aplicação de patches e backups. Com isso, você pode se concentrar no desempenho rápido, na alta disponibilidade, na segurança e na conformidade que as aplicações precisam.

- O Amazon RDS pode ser configurado com diversos serviços de banco de dados, com otimização para memória, desempenho ou E/S, bem como oferece suporte para os de bancos de dados mais comuns, incluindo Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle e Microsoft SQL Server.

- Nesse caso usamos o Postgres pelo grande suporte, documentação e quantidade de APIs disponíveis para aplicações, python, ruby, go entre outros.

	[RDS](https://aws.amazon.com/rds/?nc1=h_ls)

Base B:  

- De  cara o Postgres também cumpre com as necessidades da base B, os ganhos são os citados no ponto acima. Porém para a utilização dos seus dados por meio algoritmos de ML, indicaria alguma implementação com serviços do S3, que são baratos, e perfomáticos na análise de dados estática e dinâmica.
	

Base C: 

- Para a necessidade de rápido acesso, e rastreio de eventos, o ElasticSearch se encaixa muito bem nesse caso. E com mesmo propósito de não ter que se preocupar com tarefas de administração da infraestrutura. Assim podemos utilizar o ElasticSearch Service da AWS. A ideia do Elasticsearch é que além de armazenar os dados de forma não relacional, ele provê uma infra interna muito boa para retornar buscas muito pesadas. Por ser um motor de pesquisa textual altamente escalável, permite armazenar e analisar grandes volumes de informações praticamente em tempo real.

	[ElasticSearch](https://www.elastic.co/products/elasticsearch)
	[ElasticSearch Service](https://aws.amazon.com/pt/elasticsearch-service/)



### Tráfego

O modelo  escolhido para criação da arquitetura de software distribuído é o REST. Neste modelo arquitetural, o protocolo [HTTP](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol) tem seus recursos explorados, sendo um modelo de comunicação seguro, amplamente testado e, acima de tudo, padrão.

Em uma abordagem HTTP RESTful, usamos uma  interface que compusesse o protocolo HTTP da aplicação. Faríamos algo assim:

![APIs](https://github.com/JonnatasCabral/desafioSC/blob/master/imagens/api.jpg)

#### API Gateway

Para a porta de entrada das nossas APIs, escolhi usar o API Gateway da AWS. Pensando na segurança, possuir um Gateway de APIs é uma das melhores soluções no mercado para conseguir ter o controle integral de sua API. 
Contemplando os pilares CIA (Confidentiality, Integrity, Availability) de forma quase impecável.


##### Payloads 


Microservice A:

 `pessoas/{cpf}`
```json
payload = {
  "cpf": Number,
  "nome": String,
  "endereco": {
    "rua": String,
    "numero": Number,
    "cep": Number
  },
  "dividas": [
    {
      "divida": String,
      "valor": Number,
      "Descricao": String
    },
    {
      "divida": String,
      "valor": Number,
      "Descricao": String
    }
  ]
}
```


Microservice B

`/{cpf}/score`
```json
payload =  {
  "cpf": Number,
  "nome": String, 
  "idade": Number,
  "bens": [
    {
      "titulo": String,
      "valor": Number,
      "Descricao": String
    },
    {
      "titulo": String,
      "valor": Number,
      "Descricao": String
    }
  ],
  "endereco": {
    "rua": String,
    "numero": Number,
    "cep": Number
  },
  "rendas": [
    {
      "fonte": String,
      "valor": Number,
      "descricao": String
    },
    {
      "fonte": String,
      "valor": Number,
      "descricao": String
    },
  ]
}
```

Microservice C

`/{cpf}/eventos`
```json
{
  "cpf": Number,
  "nome": String,
  "cosultas": [
    {
      "bureau": String,
    },
    {
      "bureau": String,
    },
  ],
  "ultima_compra": {
    "valor": Number,
    "descricao": String,
  },
  "movimentacoes": [
    {
      "tipo": String,
      "valor": Number,
      "descricao": String
    },
    {
      "tipo": String,
      "valor": Number,
      "descricao": String
    },
  ]
}
```

#### Segurança

Adicionei dois pontos de segurança na comunicação entre os serviços de disponibilização de dados, são os seguintes:


##### Authenticação

Escolhi usar [Token Based Authentication](https://www.w3.org/2001/sw/Europe/events/foaf-galway/papers/fp/token_based_authentication/), já que a autenticação baseada em token funciona garantindo que cada solicitação seja acompanhada por um token assinado, assim servidor verifica quanto à autenticidade e, em seguida, responde à solicitação.

Assim podemos utilizar o OAUTH, para comodidade e segurança dos usuários integrando a aplicação com sites de terceiros
como Google e Facebook. 


##### CSRF  (Cross-Site Request Forgery)

A primeira defesa contra ataques de [CSRF](https://pt.wikipedia.org/wiki/Cross-site_request_forgery) é garantir que as solicitações GET e outros métodos 'seguros', sejam livres de efeitos colaterais. Solicitações através de métodos "inseguros", como POST, PUT e DELETE, podem ser protegidos.
Ferramentas como Django, Rails, e outros frameworks se preocupam em disponibilizar uma fácil implementação da utiliação de um [CSRF Token](https://docs.djangoproject.com/en/2.1/ref/csrf/) que trabalha em cima dessa vulnerabilidade. 

#### Disponibilização dos dados

Para a disponibilização dos dados, escolhi usar do poder da gama de ferramentas disponíveis em JavaScript para a criação de uma interface para o cliente. O a ferramenta mais atual, bem documentada e utilizada pela comunidade Open Source é o React. Com ele podemos utilizar bons padrões de projetos React, tais com "Components" e "containers", já utilizados atualmente. Assim otimizando o desenvolvimento e a legibilidade do projeto.

#### Desenvolvimento e Deploy
Para melhorar a portabilidade das aplicações para os ambientes de desenvolvimento e produção usaremos o Docker, que possibilita o empacotamento dos nossos serviços  dentro de um container, assim podemos utilizar diversas ferramentas e linguagem, e só precisamos garantir que os ambientes de desenvolvimento e produção (AWS) possuam Docker.

#### Tecnologias adotadas
- AWS
- Python, Ruby, JavaScript
- Django, Rails, Node, React
- Postgres, ElasticSearch
- Docker

# Rodando aplicação

```bash

$ make build
$ make up 
$ make makemig
$ make mig

```

#### Referências
- [Microservices: Decomposição de Aplicações para Implantação e Escalabilidade](https://www.infoq.com/br/articles/microservices-intro)
- [Introdução ao REST InfoQ](https://www.infoq.com/br/articles/rest-introduction)
-  [HTTP](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [ElasticSearch](https://www.elastic.co/products/elasticsearch)
- [ElasticSearch Service](https://aws.amazon.com/pt/elasticsearch-service/)
- [RDS](https://aws.amazon.com/rds/?nc1=h_ls)
- [Token Based Authentication](https://www.w3.org/2001/sw/Europe/events/foaf-galway/papers/fp/token_based_authentication/)
- [CSRF (Cross-Site Request Forgery)](https://pt.wikipedia.org/wiki/Cross-site_request_forgery)
-  [Django CSRF Token](https://docs.djangoproject.com/en/2.1/ref/csrf/)


