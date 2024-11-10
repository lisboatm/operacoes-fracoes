import math

# Função para simplificar a fração usando o Máximo Divisor Comum (MDC)
def simplificar(numerador, denominador):
    if denominador == 0:
        raise ValueError("Denominador não pode ser zero.")
    mdc = math.gcd(numerador, denominador)
    return numerador // mdc, denominador // mdc

# Função para realizar a operação entre duas frações
def processar_operacao(fracao1, operador, fracao2):
    # Extrai numerador e denominador de cada fração
    N1, D1 = map(int, fracao1.split('/'))
    N2, D2 = map(int, fracao2.split('/'))
    
    if operador == '+':
        # Soma
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == '-':
        # Subtração
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif operador == '*':
        # Multiplicação
        numerador = N1 * N2
        denominador = D1 * D2
    elif operador == '/':
        # Divisão
        numerador = N1 * D2
        denominador = N2 * D1
    else:
        raise ValueError(f"Operador inválido: {operador}")
    
    # Simplificar o resultado
    numerador, denominador = simplificar(numerador, denominador)
    
    return f"{numerador}/{denominador}"

# Função para processar cada caso de teste
def resolver_casos(casos):
    for caso in casos:
        fracao1, operador, fracao2 = caso
        try:
            resultado = processar_operacao(fracao1, operador, fracao2)
            print(f"{fracao1} {operador} {fracao2} = {resultado}")
        except ValueError as e:
            print(f"Erro: {e}")

# Função principal
def main():
    N = int(input())
    casos = [input().split() for _ in range(N)]
    resolver_casos(casos)

if __name__ == "__main__":
    main()
