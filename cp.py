servicos = {
    "login": {
        "criticidade": 3,
        "descricao": "acesso ao sistema"
    },
    "pagamento": {
        "criticidade": 5,
        "descricao": "processamento de pagamentos"
    },
    "relatorio": {
        "criticidade": 2,
        "descricao": "geracao de relatorios"
    },
    "notificacoes":{
        "criticidade": 1,
        "descricao": "envio de avisos ao usuario"
    },
    "carrinho": {
        "criticidade": 4,
        "descricao": "carrinho de compras"
    },"busca": {
        "criticidade": 2,
        "descricao": "busca de produtos"
    },
    "estoque": {
        "criticidade": 3,
        "descricao": "controle de estoque"
    },
    "api_externa": {
        "criticidade": 4,
        "descricao": "integracao com parceiros externos"
    },
}

# Exercicio 2 --------------------------

def registrar_sintomas(*sintomas):
    lista_sintomas = list(sintomas)
    return lista_sintomas

sintomas_incidente = registrar_sintomas("erro 500", "tela branca", "login bloqueado")
print(sintomas_incidente)

# Exercicio 4 --------------------------

def calcular_pontuacao(criticidade, usuarios_afetados=0, indisponivel=False):
    pontuacao = criticidade
    if usuarios_afetados >= 100:
        pontuacao += 3
    if indisponivel:
        pontuacao += 2
    return pontuacao

pontuacao_incidente = calcular_pontuacao(criticidade=5, usuarios_afetados=250, indisponivel=True)
print(pontuacao_incidente)