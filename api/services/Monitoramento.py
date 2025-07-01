import os
from datetime import datetime
from openpyxl import Workbook, load_workbook
import psutil

class Monitoramento:
    def __init__(self):
        self.data_atual = datetime.now().strftime('%Y-%m-%d')
        self.arquivo = f"./desempenho/{self.data_atual}.xlsx"

        # Tenta carregar ou criar a planilha com segurança
        if not os.path.exists(self.arquivo):
            self.criar_planilha()
        else:
            try:
                self.planilha = load_workbook(self.arquivo)
                self.sheet = self.planilha.active
            except Exception as e:
                print(f"[Monitoramento] Erro ao carregar planilha existente: {e}")
                self.criar_planilha()

    def criar_planilha(self):
        self.planilha = Workbook()
        self.sheet = self.planilha.active
        self.sheet.append(['Data', 'Hora', 'PID', 'IP', 'Memória (MB)', 'Ação'])
        self.planilha.save(self.arquivo)

    def registrar_acao(self, acao, ip=''):
        self.data_atual = datetime.now().strftime('%Y-%m-%d')
        self.arquivo = f"./desempenho/{self.data_atual}.xlsx"

        # Garante que a planilha seja válida a cada escrita
        if not os.path.exists(self.arquivo):
            self.criar_planilha()
        else:
            try:
                self.planilha = load_workbook(self.arquivo)
                self.sheet = self.planilha.active
            except Exception as e:
                print(f"[Monitoramento] Erro ao reabrir planilha: {e}")
                self.criar_planilha()

        agora = datetime.now()
        data = agora.strftime('%Y-%m-%d')
        hora = agora.strftime('%H:%M:%S')
        pid = os.getpid()
        memoria = psutil.Process(pid).memory_info().rss / (1024 * 1024)

        self.sheet.append([data, hora, pid, ip, round(memoria, 2), acao])
        self.planilha.save(self.arquivo)