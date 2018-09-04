
# desafioSC

## Solução
	
Como primeiro passo na busca da solução, busquei por ferramentas que se encaixassem em suprissem as necessidades apontadas em cada etapa, passando por armazenamento, trafego e a Disponibilização dos dados, sempre focando na agilidade e segurança.

###  Armazenamento:

Base A: É extremamente sensível e deve ser protegida com
os maiores níveis de segurança, mas o acesso a esses dados não precisa ser tão performática.
	
- Para essas necessidades podemos utilizar O Amazon Relational Database Service (Amazon RDS) que facilita configurar, operar e escalar bancos de dados relacionais na nuvem. O serviço oferece capacidade econômica e redimensionável e automatiza tarefas demoradas de administração, como provisionamento de hardware, configuração de bancos de dados, aplicação de patches e backups. Com isso, você pode se concentrar no desempenho rápido, na alta disponibilidade, na segurança e na conformidade que as aplicações precisam.

- O Amazon RDS pode ser configurado com diversos serviços de banco de dados, com otimização para memória, desempenho ou E/S, bem como oferece suporte para os de bancos de dados mais comuns, incluindo Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle e Microsoft SQL Server.

- Nesse caso usariamos o Postgres pelo grande suport, documentação e quantidade de APIs disponiveis para aplicações, python, ruby, go entre outros.

	[RDS](https://aws.amazon.com/rds/?nc1=h_ls)

Base B:  Base B que também possui dados críticos, mas ao contrário da Base A, o acesso
precisa ser um pouco mais rápido. Uma outra característica da Base B é que além de consultas
ela é utilizada para extração de dados por meio de algoritmos de aprendizado de máquina.
	


Base C: A Base C, que não possui nenhum tipo de dado crítico, mas precisa de um acesso
extremamente rápido.

	- Para a necessidade de rápido acesso, e rastreio de eventos, o ElasticSearch se encaixa muito
	bem nesse caso. E com mesmo propósito de não ter que se preocupar com tarefas de administração da infraestrutura,
	Podemos ultilizar o ElasticSearch Service da AWS. A ideia do Elasticsearch é que além de armazenar os dados de forma não relacional, ele prove uma infra interna muito boa para retornar buscas muito pesadas. Por ser um motor de pesquisa textual altamente escalável, permite armazenar e analisar grandes volumes de informações praticamente em tempo real.

	[ElasticSearch](https://www.elastic.co/products/elasticsearch)
	[ElasticSearch Service](https://aws.amazon.com/pt/elasticsearch-service/)



### Tráfego

O modelo  escolhido para criação da arquitetura de software distribuido é o REST. Neste modelo arquitetural, o protocolo [HTTP](https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol) tem seus recursos explorados, sendo um modelo de comunicação seguro, amplamente testado e, acima de tudo, padrão.

Em uma abordagem HTTP RESTful, usariamos uma  interface que compusesse o protocolo HTTP da aplicação. Fariamos algo assim:

![APIs](https://github.com/JonnatasCabral/desafioSC/blob/master/imagens/api.jpg)

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

Adicionei dois pontos de segurança na comunicação entre os serviços de disponibilização de dados, utilizando de 


##### Authenticação

Escolhi usar [Token Based Authentication](https://www.w3.org/2001/sw/Europe/events/foaf-galway/papers/fp/token_based_authentication/), já que a autenticação baseada em token funciona garantindo que cada solicitação seja acompanhada por um token assinado, assim servidor verifica quanto à autenticidade e, em seguida, responde à solicitação.

Assim podemos ultilizar o OAUTH, para comodidade e segurança dos usuarios integrando a aplicação com sites de terceiros
como Google e Facebook. 


##### [CSRF  (Cross-Site Request Forgery)](https://pt.wikipedia.org/wiki/Cross-site_request_forgery)

A primeira defesa contra ataques de CSRF é garantir que as solicitações GET e outros métodos 'seguros', sejam livres de efeitos colaterais. Solicitações através de métodos "inseguros", como POST, PUT e DELETE, podem ser protegidos.
Ferramentas como Django, rails, e outros frameworks se preocupam em disponibilizar uma fácil implementação para essa vulnerabilidade.

#### Tecnologias adotadas
- AWS
- Python, Ruby, JavaScript
- Django, Rails, Node, React
- Postgres, ElasticSearch
