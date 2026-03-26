import tkinter as tk
from tkinter import messagebox
import requests

# URL do seu servidor webhook
WEBHOOK_URL = "http://seu-servidor.com/webhook"

# Valor fixo da mensalidade
MENSALIDADE = 119.99

def pagar_mensalidade():
    # Simula pagamento no PDV
    messagebox.showinfo("Pagamento", f"Mensalidade de R$ {MENSALIDADE:.2f} paga com sucesso!")

    # Envia para o servidor via webhook
    payload = {
        "evento": "mensalidade_paga",
        "valor": MENSALIDADE,
        "status": "confirmado",
        "cliente": "PDV-001"  # você pode colocar ID do cliente aqui
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        if response.status_code == 200:
            messagebox.showinfo("Servidor", "Pagamento registrado no servidor!")
        else:
            messagebox.showwarning("Servidor", f"Falha no servidor: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível enviar para o servidor.\n{e}")

# ---------------------- Tkinter ----------------------
root = tk.Tk()
root.title("PDV - Mensalidade")
root.geometry("300x150")

label = tk.Label(root, text=f"Mensalidade: R$ {MENSALIDADE:.2f}", font=("Arial", 14))
label.pack(pady=20)

btn_pagar = tk.Button(root, text="Pagar Mensalidade", command=pagar_mensalidade, bg="green", fg="white", font=("Arial", 12))
btn_pagar.pack(pady=10)

root.mainloop()
