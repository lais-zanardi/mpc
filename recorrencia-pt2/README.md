# Avaliação: Relação de Recorrência (Parte 2)

O script `avaliacao-recorrencia-pt2.py` é um programa em Python desenvolvido para calcular o somatório de `n` termos de uma fórmula de recorrência específica.

**Funcionamento do Script:**

1.  O programa solicita ao usuário dois valores inteiros:

      * `z`: O valor inicial (base para o numerador).
      * `n`: O número de termos a serem somados.

2.  A função `formula_recorrencia` calcula a soma. A lógica segue a seguinte recorrência:

      * O termo `a` (numerador) inicia com `z` e é multiplicado por `-2` a cada nova iteração.
      * O termo `b` (denominador) inicia com `2` e é multiplicado por `(i+2)` a cada nova iteração `i` (onde `i` vai de 1 até `n`).
      * A cada passo, o valor de `a/b` é adicionado à `soma` total.

3.  Ao final, o script imprime o resultado final da soma.

#### Como Executar

1.  Certifique-se de ter o Python 3 instalado em seu sistema.

2.  Clone o repositório (ou baixe o arquivo `.py`).

3.  Navegue até o diretório onde o arquivo está localizado.

4.  Execute o script através do terminal:

    ```bash
    python avaliacao-recorrencia-pt2.py
    ```

5.  Digite os valores de `z` e `n` quando solicitado.