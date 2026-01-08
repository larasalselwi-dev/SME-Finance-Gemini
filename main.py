import tkinter as tk
from tkinter import ttk
from Project.view.list_client import ClientsTableView
from Project.view.list_request import RequestsTableView
from Project.view.list_finance import FinanceTableView
from Project.view.list_guarante import GuarantesTableView

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Finance System")
        self.geometry("1500x800")
        nav = ttk.Frame(self)
        nav.pack(fill="x", pady=4)
        ttk.Button(nav, text="عملاء البنك  ", width=50, command=lambda: self.show_frame(ClientsTableView)).pack(side="right")
        ttk.Button(nav, text="طلبات التمويل ", width=50, command=lambda: self.show_frame(RequestsTableView)).pack(side="right")
        ttk.Button(nav, text="التمويلات", width=50, command=lambda: self.show_frame(FinanceTableView)).pack(side="right")
        ttk.Button(nav, text="الضمانات", width=50, command=lambda: self.show_frame(GuarantesTableView)).pack(side="right")
        
        # Container for all views
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        # Register all views
        for F in ( ClientsTableView, RequestsTableView,FinanceTableView,GuarantesTableView):
            frame = F(self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")




      

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def get_page(self, page_class):
      return self.frames[page_class]

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
