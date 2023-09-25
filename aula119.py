import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda) OK

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1,2)}
    for p in produtos
]

produtos_ordenados_nome = copy.deepcopy(novos_produtos)

produtos_ordenados_nome.sort(key=lambda p: p['nome'], reverse=True)

produtos_ordenados_preco = copy.deepcopy(novos_produtos) 

produtos_ordenados_preco.sort(key=lambda p: p['preco'])


print('Produtos:')
print(*produtos, sep='\n')
print()
print('Novos produtos:')
print(*novos_produtos, sep='\n')
print()
print('Produtos ordenados por nome:')
print(*produtos_ordenados_nome, sep='\n')
print()
print('Produtos ordenados por preço:')
print(*produtos_ordenados_preco, sep='\n')


