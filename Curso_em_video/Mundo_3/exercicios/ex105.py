def notas(*n, sit=False):
    """-> Amostra a média e a situação da turma de acordo com as notas

    Args:
        sit (bool, optional):Se irá amostra(True) ou não(False) a situação da turma. Defaults to False.

    Returns:
        Dic: Dicionário que contem o número de notas adicionadas ['Total'], a maior nota ['Maior'], 
        menor nota ['Menor'], média ['Média'] e situação ['Situação']
    """

    aluno = {}
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    aluno['Média'] = sum(n) / len(n)

    if sit:
        if aluno['Média'] >= 7.0:
            aluno['Situação'] = 'Ótima'
        elif aluno['Média']>= 6.0:
            aluno['Situação'] = 'Boa'
        elif 6.0 > aluno['Média'] >= 5.0:
            aluno['Situação'] = 'Ruim'
        else:
            aluno['Situação'] = 'Pessíma'

    return aluno

resp = notas(5.5, 6.5, 7.5, 5.4, sit=True)
print(resp)

help(notas)