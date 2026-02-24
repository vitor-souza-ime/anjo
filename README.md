
# 👼 Problema do Anjo — Simulação Computacional em Python

Este repositório apresenta uma implementação computacional do **Problema do Anjo (Angel Problem)**, um jogo combinatório proposto por John H. Conway, modelado aqui como um processo dinâmico em grade bidimensional finita.

O projeto tem como objetivo:

* Simular a dinâmica entre o **Anjo** e o **Diabo**
* Visualizar o crescimento das regiões bloqueadas
* Analisar experimentalmente a mobilidade do Anjo para diferentes valores de ( k )
* Produzir gráficos ilustrativos da trajetória

---

## 📌 Descrição do Problema

O jogo ocorre em um tabuleiro (aproximação finita de ℤ²), envolvendo dois jogadores:

* 👼 **Anjo**: pode mover-se até ( k ) casas por turno.
* 😈 **Diabo**: bloqueia uma casa livre por turno.

O jogo termina quando:

* O Anjo fica sem movimentos possíveis → vitória do Diabo.
* O Anjo sobrevive até um número máximo de turnos → sobrevivência experimental.

### Parâmetro crítico

* ( k = 1 ) → o Diabo pode vencer.
* ( k \geq 2 ) → o Anjo possui estratégia vencedora no plano infinito.

---

## 🧮 Modelagem Matemática

A dinâmica é modelada sobre um grafo:

[
G = (\mathbb{Z}^2, E)
]

Com métrica Manhattan:

[
d((x,y),(a,b)) = |x-a| + |y-b|
]

O conjunto de movimentos possíveis do Anjo é dado por:

[
{ (dx,dy) \mid |dx| + |dy| \le k }
]

---

## ⚙️ Implementação

### Características principais

* Tabuleiro ( N \times N )
* Representação matricial com NumPy
* Visualização com Matplotlib
* Impressão de métricas na CLI:

  * Turno atual
  * Número de bloqueios
  * Posição do Anjo

---

## 📊 Visualização

O gráfico gerado apresenta:

* ⬛ Casas bloqueadas pelo Diabo (quadrados pretos)
* 🔴 Trajetória do Anjo (linha vermelha)
* 🔴 Posição final destacada

A visualização permite analisar:

* Formação de barreiras
* Conectividade restante
* Expansão espacial do Anjo

---

## 🚀 Como Executar

### Requisitos

```bash
pip install numpy matplotlib
```

### Execução

```bash
python anjo.py
```

O terminal exibirá informações por turno e, ao final, será mostrado o gráfico da simulação.

---

## 📈 Parâmetros Ajustáveis

No código, podem ser alterados:

```python
N = 40           # tamanho do tabuleiro
power = 2        # valor de k
max_turns = 200  # limite de turnos
```

---

## 🔬 Possibilidades de Extensão

Este projeto pode ser expandido para:

* Implementação de estratégias não aleatórias
* Diabo com heurística baseada em BFS
* Estudo estatístico de tempo médio até captura
* Modelagem como processo estocástico adversarial
* Análise de conectividade dinâmica
* Simulação com fronteiras periódicas (toro)
* Implementação com NetworkX

---

## 📚 Fundamentação Teórica

O Problema do Anjo foi resolvido independentemente por:

* Kloster (2007)
* Máthé (2007)

Mostrando que o Anjo de poder 2 possui estratégia vencedora no plano infinito.

---

## 🎯 Objetivo Acadêmico

Este repositório pode ser utilizado como:

* Ferramenta didática em disciplinas de:

  * Teoria dos Grafos
  * Sistemas Dinâmicos
  * Processos Estocásticos
  * Computação Científica
* Base para experimentos computacionais
* Exemplo de modelagem matemática aplicada

---

## 👨‍🏫 Autor

Vitor Amadeu Souza
Engenharia de Computação
Ênfase em modelagem computacional, grafos e sistemas dinâmicos

