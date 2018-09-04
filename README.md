# desafioSC

###  Armazenamento:

Base A: É extremamente sensível e deve ser protegida com
os maiores níveis de segurança, mas o acesso a esses dados não precisa ser tão performática.
	
- Para essas necessidades podemos utilizar O Amazon Relational Database Service (Amazon RDS) que facilita configurar, operar e escalar bancos de dados relacionais na nuvem. O serviço oferece capacidade econômica e redimensionável e automatiza tarefas demoradas de administração, como provisionamento de hardware, configuração de bancos de dados, aplicação de patches e backups. Com isso, você pode se concentrar no desempenho rápido, na alta disponibilidade, na segurança e na conformidade que as aplicações precisam.

- O Amazon RDS pode ser configurado com diversos serviços de banco de dados, com otimização para memória, desempenho ou E/S, bem como oferece suporte para os de bancos de dados mais comuns, incluindo Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle e Microsoft SQL Server.

- Nesse caso usariamos o Postgres pelo grande suport, documentação e quantidade de APIs disponiveis para aplicações, python, ruby, go entre outros.

Base B:  Base B que também possui dados críticos, mas ao contrário da Base A, o acesso
precisa ser um pouco mais rápido. Uma outra característica da Base B é que além de consultas
ela é utilizada para extração de dados por meio de algoritmos de aprendizado de máquina.



Base C: A Base C, que não possui nenhum tipo de dado crítico, mas precisa de um acesso
extremamente rápido.
	- Para a necessidade de rápido acesso, e rastreio de eventos, O ElasticSearch se encaixa muito
	bem nesse caso. E com mesmo proposito de não ter que se preocupar com tarefas de administração da infraestrutura,
	Podemos ultilizar o ElasticSearch Service da AWS. 


### Tráfego

Em uma abordagem HTTP RESTful, começariamos com uma  interface que compusesse o protocolo HTTP da aplicação. Fariamos algo assim:

![APIs](https://github.com/jonnatascabral/desacioSC/blob/master/imagens/api.jpg)

A arquitetura escolhida 
Cada uma das bases existentes, são acessadas por sistemas em duas diferentes arquiteturas: micro-
serviços e nano-serviços. Vale salientar que essas bases de dados são externas, portanto não é
necessário dissertar sobre suas implementações, apenas suas consumações. Quantos aos payloads
retornados por esses recursos, o candidato pode usar sua criatividade e definí-los, imaginando quais
dados seriam importantes de serem retornados por sistemas como esses.
O primeiro sistema, acessa os seguintes dados da Base A:

• CPF
• Nome
• Endereço
• Lista de dívidas

O segundo, acessa a Base B que contém dados para cálculo do Score de Crédito. O Score
de Crédito é um rating utilizado por instituições de crédito (bancos, imobiliárias, etc) quando
precisam analisar o risco envolvido em uma operação de crédito a uma entidade.

• Idade
• Lista de bens (Imóveis, etc)
• Endereço
• Fonte de renda

O último serviço, acessa a Base C e tem como principal funcionalidade, rastrear eventos rela-
cionados a um determinado CPF.

• Última consulta do CPF em um Bureau de crédito (Serasa e outros).
• Movimentação financeira nesse CPF.
• Dados relacionados a última compra com cartao de crédito vinculado ao CPF.

Como você resolveria esse problema? Divague sobre os seguintes tópicos e outros que ache
adequado, sinta-se a vontade para desenhar, escrever, criar diagramas, vídeos, apresentação, ou
qualquer outro meio que facilite o entendimento por parte dos avaliadores:
• Tecnologias adotadas
• Arquitetura utilizada
• Dados armazenados (já listados ou que você acrescentaria)
