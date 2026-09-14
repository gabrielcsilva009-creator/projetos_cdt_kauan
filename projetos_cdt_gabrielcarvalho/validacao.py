import re

def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf_limpo = re.sub(r'\D', '', cpf)
    # Verifica se tem exatamente 11 dígitos
    return len(cpf_limpo) == 11

def validar_email(email: str) -> bool:
    # Expressão regular simples para verificar o formato do e-mail
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email.strip()))

def validar_telefone(telefone: str) -> bool:
    # Remove caracteres não numéricos
    tel_limpo = re.sub(r'\D', '', telefone)
    # Verifica se tem 10 ou 11 dígitos (com DDD)
    return len(tel_limpo) in (10, 11)