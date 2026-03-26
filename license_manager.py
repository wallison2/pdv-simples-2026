import hmac, hashlib
from pathlib import Path
import datetime

class LicenseManager:
    def __init__(self, secret, preload_file="hmacs_preload.sd", usadas_file="CV.sd"):
        self.secret = secret
        self.preload_file = preload_file
        self.usadas_file = usadas_file
        self.data_file = "dta.sd"  # aqui vai guardar a data de expiração

    def _hmac_of(self, chave: str) -> str:
        return hmac.new(self.secret, chave.encode("utf-8"), hashlib.sha256).hexdigest()

    def carregar_hmacs(self):
        return {linha.strip() for linha in Path(self.preload_file).read_text().splitlines() if linha.strip()}

    def carregar_usadas(self):
        if not Path(self.usadas_file).exists():
            return set()
        return {linha.strip() for linha in Path(self.usadas_file).read_text().splitlines() if linha.strip()}

    def salvar_usada(self, hmac_str):
        with open(self.usadas_file, "a") as f:
            f.write(hmac_str + "\n")

    def activate_key(self, chave_digitada: str):
        hmacs_validos = self.carregar_hmacs()
        usadas = self.carregar_usadas()
        h = self._hmac_of(chave_digitada)

        if h not in hmacs_validos:
            return False, "Chave inválida!"

        if h in usadas:
            return False, "Chave já usada!"

        # Marca chave como usada
        self.salvar_usada(h)

        hoje = datetime.date.today()

        # Se já tem uma data de expiração salva, soma 30 dias
        if Path(self.data_file).exists():
            data_exp_str = Path(self.data_file).read_text().strip()
            try:
                data_exp = datetime.datetime.strptime(data_exp_str, "%Y-%m-%d").date()
            except ValueError:
                data_exp = hoje
            # Se ainda não venceu, soma 30 ao vencimento existente
            if data_exp >= hoje:
                nova_exp = data_exp + datetime.timedelta(days=30)
            else:
                nova_exp = hoje + datetime.timedelta(days=30)
        else:
            # Primeira ativação: 30 dias a partir de hoje
            nova_exp = hoje + datetime.timedelta(days=30)

        # Salva nova data de expiração
        Path(self.data_file).write_text(nova_exp.strftime("%Y-%m-%d"))

        dias = (nova_exp - hoje).days
        return True, f"Chave ativada! Agora você tem {dias} dias de uso."

    def dias_restantes(self):
        """Retorna quantos dias faltam até a expiração."""
        arq = Path(self.data_file)
        if not arq.exists():
            return 0

        hoje = datetime.date.today()
        data_exp = datetime.datetime.strptime(arq.read_text().strip(), "%Y-%m-%d").date()
        dias = (data_exp - hoje).days
        return max(dias, 0)

    def check_on_start(self):
        """Verifica se a licença está ativa ao iniciar o programa."""
        dias = self.dias_restantes()
        if dias <= 0:
            return False, "Licença expirada."
        elif dias <= 5:
            return True, f"Atenção: sua licença expira em {dias} dias."
        else:
            return True, f"Licença válida. Dias restantes: {dias}"
