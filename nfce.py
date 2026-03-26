import xml.etree.ElementTree as ET

# Carregar o XML do arquivo (ou string)
xml_file = "exemplo_nfce.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

# Namespace usado no XML (precisa para buscar elementos)
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}

# Acessar o número da nota fiscal (nNF)
nNF = root.find('.//nfe:ide/nfe:nNF', ns).text
print("Número da NF:", nNF)

# Acessar a data de emissão (dhEmi)
dhEmi = root.find('.//nfe:ide/nfe:dhEmi', ns).text
print("Data de emissão:", dhEmi)

# Acessar o nome do emitente (xNome)
nome_emitente = root.find('.//nfe:emit/nfe:xNome', ns).text
print("Emitente:", nome_emitente)

# Acessar CNPJ do emitente
cnpj_emitente = root.find('.//nfe:emit/nfe:CNPJ', ns).text
print("CNPJ do Emitente:", cnpj_emitente)

# Acessar os produtos (pode ter vários)
produtos = root.findall('.//nfe:det/nfe:prod', ns)
for i, prod in enumerate(produtos, 1):
    descricao = prod.find('nfe:xProd', ns).text
    quantidade = prod.find('nfe:qCom', ns).text
    valor_unit = prod.find('nfe:vUnCom', ns).text
    valor_total = prod.find('nfe:vProd', ns).text
    print(f"Produto {i}: {descricao} - Qtde: {quantidade}, Valor Unit: {valor_unit}, Total: {valor_total}")

# Acessar valor total da NF
vNF = root.find('.//nfe:total/nfe:ICMSTot/nfe:vNF', ns).text
print("Valor total da NF:", vNF)



import xml.etree.ElementTree as ET

def ler_nfce_xml(caminho_arquivo):
    ns = {'ns': 'http://www.portalfiscal.inf.br/nfe'}
    tree = ET.parse(caminho_arquivo)
    root = tree.getroot()

    infNFe = root.find('.//ns:infNFe', ns)
    ide = infNFe.find('ns:ide', ns)
    emit = infNFe.find('ns:emit', ns)
    dets = infNFe.findall('ns:det', ns)
    total = infNFe.find('ns:total/ns:ICMSTot', ns)

    dados = {
        'numero_nf': ide.find('ns:nNF', ns).text,
        'data_emissao': ide.find('ns:dhEmi', ns).text,
        'emitente_nome': emit.find('ns:xNome', ns).text,
        'emitente_cnpj': emit.find('ns:CNPJ', ns).text,
        'produtos': [],
        'valor_total': total.find('ns:vNF', ns).text,
    }

    for det in dets:
        prod = det.find('ns:prod', ns)
        dados['produtos'].append({
            'descricao': prod.find('ns:xProd', ns).text,
            'quantidade': prod.find('ns:qCom', ns).text,
            'valor_unitario': prod.find('ns:vUnCom', ns).text,
            'valor_total': prod.find('ns:vProd', ns).text,
        })

    return dados


def importar_xml_nfce(self):
    caminho, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo XML", "", "Arquivos XML (*.xml)")
    if caminho:
        dados_nfce = ler_nfce_xml(caminho)
        # Agora, preencha os campos do seu PDV com esses dados:
        self.txt_numero_nf.setText(dados_nfce['numero_nf'])
        self.txt_data_emissao.setText(dados_nfce['data_emissao'])
        self.txt_emitente.setText(dados_nfce['emitente_nome'])
        self.txt_cnpj_emitente.setText(dados_nfce['emitente_cnpj'])
        # Para os produtos, pode popular uma tabela
        self.preencher_tabela_produtos(dados_nfce['produtos'])
        self.txt_valor_total.setText(dados_nfce['valor_total'])


def preencher_tabela_produtos(self, produtos):
    self.table_produtos.setRowCount(0)
    for prod in produtos:
        linha = self.table_produtos.rowCount()
        self.table_produtos.insertRow(linha)
        self.table_produtos.setItem(linha, 0, QTableWidgetItem(prod['descricao']))
        self.table_produtos.setItem(linha, 1, QTableWidgetItem(prod['quantidade']))
        self.table_produtos.setItem(linha, 2, QTableWidgetItem(prod['valor_unitario']))
        self.table_produtos.setItem(linha, 3, QTableWidgetItem(prod['valor_total']))



