# pybr-talk-proposal-outbox
Draft for a 30 minute talk on SAGA/Outbox using Django

- [pybr-talk-proposal-outbox](#pybr-talk-proposal-outbox)
  - [Título Proposto](#título-proposto)
  - [Resumo](#resumo)
  - [Descrição](#descrição)
  - [Descreva mais prolixamente o que será abordado na sua atividade, a sua motivação para criá-la e informações que considere relevantes.](#descreva-mais-prolixamente-o-que-será-abordado-na-sua-atividade-a-sua-motivação-para-criá-la-e-informações-que-considere-relevantes)
  - [O que as pessoas que participarem podem esperar aprender na sua atividade?](#o-que-as-pessoas-que-participarem-podem-esperar-aprender-na-sua-atividade)
  - [Escolha até 3 palavras-chave para representar sua atividade](#escolha-até-3-palavras-chave-para-representar-sua-atividade)
  - [Quais conhecimentos prévios são necessários para que seja possível acompanhar bem a sua atividade?](#quais-conhecimentos-prévios-são-necessários-para-que-seja-possível-acompanhar-bem-a-sua-atividade)
  - [Tabela de conteúdo](#tabela-de-conteúdo)


## Título Proposto
Dançando e não pisando no próprio pé: SAGA e Outbox Pattern

## Resumo
Falaremos sobre desafios comuns numa Arquitetura Orientada a Eventos, SAGA, o problema do Dual-write (e por que enfrentá-lo é necessário) e o Pattern Outbox para mitigá-lo.


## Descrição
Nesta palestra, vamos explorar os desafios comuns que surgem ao trabalhar com micro serviços. Vamos discutir as escolhas arquiteturais e os problemas que aparecem à medida que a complexidade das aplicações aumenta. Também apresentaremos, de forma resumida, o Design Pattern **Saga**, destacando as diferenças entre os modelos de Orquestração e **Coreografia** para gerenciar transações distribuídas.

Além disso, vamos abordar o problema do **Dual-Write**, um dos desafios mais frequentes na busca por consistência de dados em sistemas distribuídos, e como o Pattern Outbox pode ajudar a mitigar esse problema.

- Os desafios que os micro serviços trazem consigo
- O que, afinal, é uma transação?
- Como um padrão arquitetural pode voltar para te assombrar se for levado em conta apenas no "caminho feliz"
- O que é o Design Pattern Saga: Orquestração VS. Coreografia
- O problema do Dual-Write
- O pattern Outbox
- Uma implementação simples usando Django.


## Descreva mais prolixamente o que será abordado na sua atividade, a sua motivação para criá-la e informações que considere relevantes.
No meio da minha carreira, quando estava deixando de ser júnior, "micro serviços" se tornou uma das palavras-chave mais quentes do mercado. Mudamos nosso paradigma de pensar, uma das transformações mais críticas do pensamento computacional moderno. No entanto, não entendíamos realmente o que tornava os micro serviços necessários. Falava-se de custos, de trabalhar com qualquer linguagem, de Docker, de Kubernetes, mas qual era a grande inovação?

Se olharmos o [Google Trends](https://trends.google.com/trends/explore?cat=1227&date=all&q=microservices,event%20driven,kafka&hl=pt) dos termos "microservices", "event driven" e "kafka", vemos que a ferramenta, o derivado, se tornou mais popular que o conceito. Minha proposta é usar a Arquitetura SAGA e Outbox como um Cavalo de Troia para explicar conceitos fundamentais como Aplicações Distribuídas, Eventos, Transações, Escopo Transacional, Commit e Rollback, ajudando, nem que apenas alguns devs, a entender melhor esses termos que lidamos todos os dias, muitas vezes sem saber sobre como eles chegaram ali.


## O que as pessoas que participarem podem esperar aprender na sua atividade?
Para os não tão inteirados no assunto:
- Aprender os conceitos básicos de Event Driven Architecture
- Aprender a definição de transação e escopo transacional
- Entender que quanto mais a complexidade da aplicação cresce, mais precisamos pensar que a infra que confiamos tende a falhar e precisamos estarmos prontos.
- Entender que precisamos criar garantias para o funcionamento da aplicação

Para pessoas com um conhecimento básico à intermediário do assunto:
- Aprender, de maneira simples, o que é SAGA e quais problemas ele se propõe a resolver.
- Instigar o pensamento crítico sobre suas aplicações e suas capacidades de falha.
- Aprender sobre o problema de Dual-Write
- Entender uma implementação de uma aplicação distribuída simples com outbox.

Para pessoas com conhecimento avançado:
- Um lembrete a conceitos que para nós já se tornaram simples
- Tenho certeza que vários ficarão felizes em me falar como várias soluções são melhores, hahaha.

## Escolha até 3 palavras-chave para representar sua atividade
Django, Arquitetura Orientada à Eventos, Micro Serviços

## Quais conhecimentos prévios são necessários para que seja possível acompanhar bem a sua atividade?
Monto minhas talks com a intenção que possam ser consumidas por pessoas com o menor nível de conhecimento possível, portanto acredito que sejam:

- Conhecimento básico de Django e da Django ORM
- Entender o básico de comunicação de comunicação HTTP
  - Saber comunicação HTTP é um conhecimento mais comum que é facilmente extrapolado para conceitos de mensageria e comunicação assíncrona.
- Não precisa saber implementar, mas conhecer o que é uma mensageria diminui a dissonância para entender.
- Interesse em padrões de design de arquitetura e aplicações.

## Tabela de conteúdo
Representando por tempo total

[0-3 minutos] Apresentando o tema e me apresentando

[3-7 minutos] Micro serviços e Aplicações distribuídas (Apresentando junto à um caso de uso simples)
[7-10 minutos] O que é uma transação?

[10-17 minutos] Explicação sobre SAGA e o modelo por Coreografia, descendo até o problema de Dual-Write e o Outbox.

[17-27 minutos] Demonstração do caso de uso apresentado e da implementação

[30 minutos] Perguntas (acredito que 1 minuto por pergunta)
