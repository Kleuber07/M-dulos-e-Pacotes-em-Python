# main.py

# Importa o módulo matematica
import matematica

# Importa funções específicas do pacote meu_pacote
from meu_pacote.mensagens import boas_vindas
from meu_pacote.operacoes import multiplica

# Exibe a mensagem de boas-vindas
print(boas_vindas("SeuNome"))

# Realiza e exibe os cálculos
print("Soma:", matematica.soma(5, 2))
print("Subtração:", matematica.subtrai(10, 4))
print("Módulo:", matematica.modulo(-5))
print("Multiplicação:", multiplica(3, 7))
