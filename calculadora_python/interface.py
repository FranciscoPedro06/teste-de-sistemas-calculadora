import tkinter as tk
from calculadora import somar, subtrair, multiplicar, dividir

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Clean")
        self.root.geometry("350x500")
        self.root.configure(bg="#2c2f33")

        self.primeiro_numero = None
        self.operador = None

        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 32, "bold"),
            bd=0, 
            justify="right", 
            bg="#23272a", 
            fg="white"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipadx=10, ipady=30)

        self.criar_botoes()

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(4):
            self.root.columnconfigure(i, weight=1)

    def criar_botoes(self):
        botoes = [
            ('C', 1, 0, 3), ('/', 1, 3, 1),
            ('7', 2, 0, 1), ('8', 2, 1, 1), ('9', 2, 2, 1), ('*', 2, 3, 1),
            ('4', 3, 0, 1), ('5', 3, 1, 1), ('6', 3, 2, 1), ('-', 3, 3, 1),
            ('1', 4, 0, 1), ('2', 4, 1, 1), ('3', 4, 2, 1), ('+', 4, 3, 1),
            ('0', 5, 0, 2), ('.', 5, 2, 1), ('=', 5, 3, 1)
        ]

        for texto, lin, col, colspan in botoes:
            comando = lambda x=texto: self.processar_clique(x)
            
            btn = tk.Button(
                self.root, 
                text=texto, 
                font=("Arial", 18),
                bg="#7289da" if texto not in ['=', 'C'] else "#43b581",
                fg="white", 
                activebackground="#5b6eae",
                relief="flat",
                command=comando
            )
            if texto == 'C':
                btn.configure(bg="#f04747")

            btn.grid(row=lin, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def processar_clique(self, tecla):
        if tecla in '0123456789.':
            atual = self.display_var.get()
            if tecla == '.' and '.' in atual:
                return
            self.display_var.set(atual + tecla)
            
        elif tecla == 'C':
            self.limpar()
            
        elif tecla in ['+', '-', '*', '/']:
            if self.display_var.get():
                self.primeiro_numero = self.display_var.get()
                self.operador = tecla
                self.display_var.set("") 
                
        elif tecla == '=':
            self.calcular()

    def limpar(self):
        self.display_var.set("")
        self.primeiro_numero = None
        self.operador = None

    def calcular(self):
        if not self.primeiro_numero or not self.operador or not self.display_var.get():
            return

        segundo_numero = self.display_var.get()

        try:
            num1 = float(self.primeiro_numero)
            num2 = float(segundo_numero)

            if self.operador == '+':
                resultado = somar(num1, num2)
            elif self.operador == '-':
                resultado = subtrair(num1, num2)
            elif self.operador == '*':
                resultado = multiplicar(num1, num2)
            elif self.operador == '/':
                resultado = dividir(num1, num2)

            if resultado.is_integer():
                resultado = int(resultado)

            self.display_var.set(str(resultado))
            
            self.primeiro_numero = None
            self.operador = None

        except ValueError as e:
            self.display_var.set("Erro: Div/0")
            self.primeiro_numero = None
        except Exception:
            self.display_var.set("Erro Geral")
            self.primeiro_numero = None

if __name__ == "__main__":
    janela = tk.Tk()
    app = CalculadoraApp(janela)
    janela.mainloop()