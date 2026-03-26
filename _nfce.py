from lxml import etree
from datetime import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import requests

class NFCeHandler:
    def __init__(self, certificado_pfx, senha_certificado):
        self.certificado_pfx = certificado_pfx
        self.senha_certificado = senha_certificado
        self.certificado = self._carregar_certificado()

    def _carregar_certificado(self):
        with open(self.certificado_pfx, "rb") as cert_file:
            return serialization.load_pkcs12(cert_file.read(), self.senha_certificado.encode())

    def gerar_xml_nfce(self, dados_nfce):
        # Criação do XML com estrutura básica da NFC-e
        raiz = etree.Element("nfeProc", xmlns="http://www.portalfiscal.inf.br/nfe", versao="4.00")
        nota_fiscal = etree.SubElement(raiz, "NFe")

        # Informações gerais da NFC-e
        inf_nfe = etree.SubElement(nota_fiscal, "infNFe", Id="NFe123456789", versao="4.00")
        ide = etree.SubElement(inf_nfe, "ide")
        etree.SubElement(ide, "cUF").text = dados_nfce["codigo_uf"]
        etree.SubElement(ide, "natOp").text = dados_nfce["natureza_operacao"]
        etree.SubElement(ide, "dhEmi").text = dados_nfce["data_hora_emissao"]
        etree.SubElement(ide, "tpNF").text = dados_nfce["tipo_nf"]
        etree.SubElement(ide, "idDest").text = dados_nfce["id_destino"]

        # Emitente
        emitente = etree.SubElement(inf_nfe, "emit")
        etree.SubElement(emitente, "CNPJ").text = dados_nfce["cnpj_emitente"]
        etree.SubElement(emitente, "xNome").text = dados_nfce["nome_emitente"]

        # Destinatário
        destinatario = etree.SubElement(inf_nfe, "dest")
        etree.SubElement(destinatario, "CPF").text = dados_nfce["cpf_destinatario"]
        etree.SubElement(destinatario, "xNome").text = dados_nfce["nome_destinatario"]

        # Produtos/Serviços
        det = etree.SubElement(inf_nfe, "det", nItem="1")
        produto = etree.SubElement(det, "prod")
        etree.SubElement(produto, "cProd").text = dados_nfce["codigo_produto"]
        etree.SubElement(produto, "xProd").text = dados_nfce["descricao_produto"]
        etree.SubElement(produto, "vProd").text = dados_nfce["valor_produto"]

        # Totais
        total = etree.SubElement(inf_nfe, "total")
        icms_tot = etree.SubElement(total, "ICMSTot")
        etree.SubElement(icms_tot, "vNF").text = dados_nfce["valor_total_nf"]

        # Salvando o XML
        xml_string = etree.tostring(raiz, pretty_print=True, xml_declaration=True, encoding="utf-8")
        with open("nfce.xml", "wb") as file:
            file.write(xml_string)

        return "nfce.xml"

    def assinar_xml(self, arquivo_xml):
        chave_privada = self.certificado.key

        # Ler o XML gerado
        with open(arquivo_xml, "rb") as file:
            xml_dados = file.read()

        # Assinar o XML
        assinatura = chave_privada.sign(
            xml_dados,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        # Anexar a assinatura ao XML (exemplo simplificado)
        arquivo_assinado = "nfce_assinado.xml"
        with open(arquivo_assinado, "wb") as file:
            file.write(xml_dados + b"\n<!-- Assinatura: -->\n" + assinatura)

        return arquivo_assinado

    def enviar_xml_sefaz(self, arquivo_assinado, url_webservice):
        with open(arquivo_assinado, "rb") as file:
            xml_dados = file.read()

        # Enviar ao webservice
        headers = {"Content-Type": "application/xml"}
        response = requests.post(url_webservice, data=xml_dados, headers=headers)

        if response.status_code == 200:
            print("XML enviado com sucesso!")
            print(response.text)
        else:
            print("Erro ao enviar o XML:")
            print(response.text)

# Exemplo de uso da classe
if __name__ == "__main__":
    dados_nfce = {
        "codigo_uf": "15",  # Código do estado (Pará)
        "natureza_operacao": "Venda",
        "data_hora_emissao": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "tipo_nf": "1",  # 1 = Saída
        "id_destino": "1",  # 1 = Operação interna
        "cnpj_emitente": "12345678000100",
        "nome_emitente": "Loja Teste Ltda",
        "cpf_destinatario": "12345678900",
        "nome_destinatario": "Cliente Teste",
        "codigo_produto": "001",
        "descricao_produto": "Produto de Teste",
        "valor_produto": "100.00",
        "valor_total_nf": "100.00"
    }

    certificado_pfx = "certificado.pfx"
    senha_certificado = "senha_do_certificado"
    url_homologacao = "https://homologacao.sefaz.xx.gov.br/NFeRecepcao"

    # Criando a instância da classe
    nfce_handler = NFCeHandler(certificado_pfx, senha_certificado)

    # Gerar o XML
    arquivo_xml = nfce_handler.gerar_xml_nfce(dados_nfce)
    print(f"Arquivo XML gerado: {arquivo_xml}")

    # Assinar o XML
    arquivo_assinado = nfce_handler.assinar_xml(arquivo_xml)
    print(f"Arquivo XML assinado: {arquivo_assinado}")

    # Enviar para SEFAZ
    nfce_handler.enviar_xml_sefaz(arquivo_assinado, url_homologacao)
