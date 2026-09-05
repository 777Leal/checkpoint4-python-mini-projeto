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

# Função 1: Consulta em dicionário + parametro padrão

# Criar uma função que receba o catálogo e o nome de um serviço. Se o serviço existir, devolver seus dados. Se não existir, devolver uma mensagem de erro. A mensagem de erro deve possuir um valor padrão que possa ser substituído na chamada.

def consultar_servico(catalogo, servico, mensagem_erro="Serviço não encontrado"):
    if servico in catalogo:
        return catalogo[servico]
    return mensagem_erro

# resultado = consultar_servico(servicos, "login")
# print(resultado)

# resultado_erro = consultar_servico(servicos, "chat", "Esse serviço não existe no catálogo")
# print(resultado_erro)


# Exercicio 2 --------------------------

def registrar_sintomas(*sintomas):
    lista_sintomas = list(sintomas)
    return lista_sintomas

sintomas_incidente = registrar_sintomas("erro 500", "tela branca", "login bloqueado")
print(sintomas_incidente)

# Função 3: Configuração flexível com kwargs

# Criar uma função que monte o registro do incidente a partir de argumentos nomeados. Use get() para definir valores padrão quando alguma informação opcional não for enviada.

def registrar_incidente(**kwargs):
    return {
        "servico": kwargs.get("servico", "não especificado"),
        "usuarios_afetados": kwargs.get("usuarios_afetados", 0),
        "indisponivel": kwargs.get("indisponivel", False),
    }

# registro = registrar_incidente(servico="login", criticidade=3, descricao="Falha de autenticação", data="2024-06-01", usuario="usuario123")
# print(registro)

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
