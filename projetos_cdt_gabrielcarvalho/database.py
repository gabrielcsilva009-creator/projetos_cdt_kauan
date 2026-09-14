import sqlite3

def salvar_aluno(dados: dict):
    conn = sqlite3.connect("academia.db")
    cursor = conn.cursor()
    
    # Cria a tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            email TEXT,
            plano TEXT
        )
    """)
    
    # Insere os dados
    cursor.execute("""
        INSERT INTO alunos (nome, cpf, email, plano)
        VALUES (?, ?, ?, ?)
    """, (dados['nome'], dados['cpf'], dados['email'], dados['plano']))
    
    conn.commit()
    conn.close()