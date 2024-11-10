## README - Desafio D: Operações com Frações

### Descrição do Problema

O desafio consiste em ler expressões matemáticas que envolvem **frações** e realizar a operação indicada. Cada linha de entrada contém duas frações e um operador (`+`, `-`, `*`, ou `/`). Sua tarefa é realizar a operação entre as duas frações, simplificar o resultado e apresentar a fração simplificada.

O enunciado do problema especifica como realizar as operações básicas de adição, subtração, multiplicação e divisão com frações.

### Operações Suportadas
Dadas duas frações:
- **Fração 1**: N1 / D1
- **Fração 2**: N2 / D2

As operações são realizadas da seguinte maneira:

1. **Soma (`+`)**:
   \[
   \text{Resultado} = \frac{N1 \times D2 + N2 \times D1}{D1 \times D2}
   \]

2. **Subtração (`-`)**:
   \[
   \text{Resultado} = \frac{N1 \times D2 - N2 \times D1}{D1 \times D2}
   \]

3. **Multiplicação (`*`)**:
   \[
   \text{Resultado} = \frac{N1 \times N2}{D1 \times D2}
   \]

4. **Divisão (`/`)**:
   \[
   \text{Resultado} = \frac{N1 \times D2}{N2 \times D1}
   \]

Após realizar a operação, simplifique o resultado usando o **Máximo Divisor Comum (MDC)** para reduzir a fração ao menor termo possível.

### Entrada

- A primeira linha contém um inteiro **N** (1 ≤ N ≤ 10,000), indicando o número de casos de teste.
- As próximas **N** linhas contêm uma expressão no formato:
  ```
  numerador1/denominador1 operador numerador2/denominador2
  ```
- Os valores dos numeradores e denominadores estão no intervalo de **1 a 1000**.

### Saída

Para cada caso de teste, a saída deve apresentar:
```
fracao1 operador fracao2 = resultado_simplificado
```

- O resultado deve ser uma fração simplificada. Se a fração não puder ser simplificada, ela deve ser apresentada como está.

### Exemplo de Entrada
```
4
1/2 + 3/4
1/2 - 3/4
2/3 * 6/6
1/2 / 3/4
```

### Exemplo de Saída
```
1/2 + 3/4 = 5/4
1/2 - 3/4 = -1/4
2/3 * 6/6 = 2/3
1/2 / 3/4 = 2/3
```

---

## Implementação

### Código Utilizado em Python

```python
import math

# Função para simplificar a fração
def simplificar(numerador, denominador):
    if denominador == 0:
        raise ValueError("Denominador não pode ser zero.")
    mdc = math.gcd(numerador, denominador)
    return numerador // mdc, denominador // mdc

# Função para processar cada operação
def processar_operacao(fracao1, operador, fracao2):
    # Extrai numerador e denominador de cada fração
    N1, D1 = map(int, fracao1.split('/'))
    N2, D2 = map(int, fracao2.split('/'))
    
    # Verifica se os denominadores não são zero
    if D1 == 0 or D2 == 0:
        raise ValueError("Denominador não pode ser zero.")
    
    if operador == '+':
        # Soma: (N1*D2 + N2*D1) / (D1*D2)
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == '-':
        # Subtração: (N1*D2 - N2*D1) / (D1*D2)
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif operador == '*':
        # Multiplicação: (N1*N2) / (D1*D2)
        numerador = N1 * N2
        denominador = D1 * D2
    elif operador == '/':
        # Divisão: (N1/D1) / (N2/D2) -> (N1*D2) / (N2*D1)
        numerador = N1 * D2
        denominador = N2 * D1
    else:
        raise ValueError(f"Operador inválido: {operador}")
    
    # Simplifica o resultado
    numerador, denominador = simplificar(numerador, denominador)
    
    return f"{numerador}/{denominador}"

# Função principal para processar os casos de teste
def resolver_casos(casos):
    for caso in casos:
        fracao1, operador, fracao2 = caso
        try:
            resultado = processar_operacao(fracao1, operador, fracao2)
            print(f"{fracao1} {operador} {fracao2} = {resultado}")
        except ValueError as e:
            print(f"Erro: {e}")

# Leitura da entrada
def main():
    # Lê o número de casos
    N = int(input())
    
    casos = []
    
    # Lê cada caso
    for _ in range(N):
        caso = input().split()
        casos.append(caso)
    
    # Resolve e imprime os resultados
    resolver_casos(casos)

# Chama a função principal
if __name__ == "__main__":
    main()

```

---

## Explicação do Código

1. **Função `simplificar()`**:
   - Usa o **Máximo Divisor Comum (MDC)** para simplificar uma fração.

2. **Função `processar_operacao()`**:
   - Realiza a operação entre duas frações e retorna o resultado simplificado.

3. **Função `resolver_casos()`**:
   - Lê e processa cada caso de teste.

4. **Função `main()`**:
   - Lê a entrada e chama a função de resolução para processar cada linha.

---

## Como Executar o Código

Certifique-se de ter o **Python 3.11** instalado em sua máquina.

1. Salve o código em um arquivo, por exemplo, `operacoes_fracoes.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.
3. Execute o programa:
   ```bash
   python operacoes_fracoes.py
   ```
4. Insira os dados manualmente ou redirecione a entrada de um arquivo:
   ```bash
   python operacoes_fracoes.py < input.txt
   ```

---

## Conclusão

O **Desafio D** envolve operações com frações e simplificação. O uso do **Máximo Divisor Comum (MDC)** é crucial para garantir que a fração seja simplificada corretamente. A solução foi projetada para lidar com até **10,000 casos de teste** de forma eficiente.
