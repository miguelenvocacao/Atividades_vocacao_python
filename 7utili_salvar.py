# Sistema escolar, PT7: Salvar as informações

import json
from alunos.cadastro import alunos

def salvar_dados():

    with open("dados/aluno.json", "w") as arquivo:

        json.dump(alunos, arquivo, indent=4)
        
        print("Dados salvos!")















