# Trabalho Prático - Teoria dos Grafos

**Alunos:**  
- Wilken Henrique Moreira  
- Arthur Feitas Jardin  

**Curso:** Engenharia de Software, 4° Período, PUC Minas  
**Disciplina:** Teoria dos Grafos  

**Data de Entrega:** 24 de novembro, até as 23:59  
**Pontos:** 20  
**Formato de Entrega:** Upload de Arquivo no Canvas (ZIP ou RAR contendo o código fonte, o arquivo `.tex` do relatório e o PDF do relatório)

---

## Descrição do Trabalho

O trabalho é composto por três partes e deve ser realizado em grupos de até 5 alunos. A implementação pode ser feita nas linguagens C/C++, C#, Java ou Python. O relatório deve ser escrito em LaTeX, no formato fornecido pela SBC ([Modelo SBC LaTeX](https://www.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr)).

**Importante:** Cada membro do grupo deve entregar uma cópia do trabalho individualmente. A falta de entrega por qualquer membro do grupo resultará em nota zero para esse aluno. 

---

## Partes do Trabalho

### Parte 1 - Biblioteca para Manipulação de Grafos

Desenvolver uma biblioteca para manipulação de grafos, incluindo as seguintes funcionalidades:

#### Representações de Grafos:
- Matriz de Adjacência
- Matriz de Incidência
- Lista de Adjacência

#### Funções Básicas de Manipulação:
- Criação de grafos com X vértices (inseridos pelo usuário)
- Criação e remoção de arestas
- Ponderação e rotulação de vértices e arestas
- Checagem de adjacência entre vértices e arestas
- Checagem da existência de arestas
- Checagem da quantidade de vértices e arestas
- Checagem se o grafo é vazio ou completo
- Checagem de conectividade (simplismente conexo, semi-fortemente conexo e fortemente conexo)
- Checagem da quantidade de componentes fortemente conexos (Kosaraju)
- Checagem de pontes e articulações

### Parte 2 - Identificação de Pontes

1. **Método Naive**: Testar a conectividade do grafo removendo uma aresta de cada vez (utilizando busca em largura ou profundidade).
2. **Método de Tarjan**: Implementação do algoritmo de Tarjan para identificação de pontes.

Após implementar ambos os métodos, você deverá encontrar um **caminho euleriano** em um grafo euleriano usando o **Algoritmo de Fleury** com as duas abordagens de detecção de pontes. Teste as duas abordagens utilizando grafos aleatórios com 100, 1000, 10000 e 100000 vértices.

### Parte 3 - Leitura e Salvamento de Grafos em Formatos Gephi

Implemente a funcionalidade para ler e salvar grafos em arquivos nos formatos suportados pelo Gephi (GEXF, GDF, GML, GraphML, Pajek NET, GraphViz DOT, CSV, UCINET DL, Tulip TPL, Netdraw VNA, Spreadsheet). Utilize o Gephi para gerar ilustrações de exemplo baseadas na documentação disponível.

---

## Relatório

O relatório deverá ser redigido entre 12 a 15 páginas e deve conter:
- Descrição das implementações
- Resultados obtidos, com telas e gráficos produzidos
- Formato de artigo SBC (LaTeX)

O relatório deve ser submetido junto ao código-fonte no formato `.zip` ou `.rar`. A documentação do formato SBC LaTeX pode ser acessada [aqui](https://www.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr).

---

## Apresentação

A apresentação será realizada tanto de forma presencial quanto em vídeo (demonstração dos resultados). Todos os membros do grupo devem participar da apresentação, que terá duração entre 5 e 10 minutos.

---

## Observações Importantes:
- A entrega será considerada inválida se algum dos itens não for enviado.
- O trabalho deve ser enviado até a data e horário limite (24 de novembro, 23:59).
