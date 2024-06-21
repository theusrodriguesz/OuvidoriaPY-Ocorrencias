class Ocorrencia:
    def __init__(self, nome, tipo, descricao):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo.capitalize()}\nDescrição: {self.descricao}\n"

class SistemaOcorrencias:
    def __init__(self):
        self.ocorrencias = []

    def adicionar_ocorrencia(self, nome, tipo, descricao):
        tipo = tipo.lower()
        if tipo in ['crítica', 'elogio', 'sugestão']:
            nova_ocorrencia = Ocorrencia(nome, tipo, descricao)
            self.ocorrencias.append(nova_ocorrencia)
            print("Ocorrência adicionada com sucesso.")
        else:
            print("Tipo de ocorrência inválido. Use 'crítica', 'elogio' ou 'sugestão'.")

    def exibir_ocorrencias(self):
        if not self.ocorrencias:
            print("Nenhuma ocorrência registrada.")
        else:
            for ocorrencia in self.ocorrencias:
                print(ocorrencia)

    def exibir_ocorrencias_por_tipo(self, tipo):
        tipo = tipo.lower()
        ocorrencias_filtradas = [ocorrencia for ocorrencia in self.ocorrencias if ocorrencia.tipo == tipo]
        
        if not ocorrencias_filtradas:
            print(f"Nenhuma ocorrência do tipo '{tipo}' registrada.")
        else:
            for ocorrencia in ocorrencias_filtradas:
                print(ocorrencia)