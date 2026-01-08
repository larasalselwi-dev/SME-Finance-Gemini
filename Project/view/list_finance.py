import tkinter as tk
from tkinter import ttk
from Project.controller.FinanceController import FinanceController
from Project.view.add_finance import  create_add_finance_window

from Project.view.add_guarante import  create_add_guarantee_window

  # تأكد من المسار الصحيح

class FinanceTableView(ttk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller  # 

        # ---------- Style ----------
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#ffffff",
            foreground="#000000",
            rowheight=28,
            fieldbackground="#ffffff",
            font=("Segoe UI", 10)
        )

        style.map(
            "Treeview",
            background=[("selected", "#5dade2")],
            foreground=[("selected", "white")]
        )

        style.configure(
            "Treeview.Heading",
            background="#2e86c1",
            foreground="white",
            font=("Segoe UI", 11, "bold")
        )

        # ---------- Table Frame ----------
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)



        columns = ("Finance_Id", "Client_Id", "Amount_granted", "Exchange_date",
                   "Payment_term", "Interest_rate","Action")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        headings = ["رقم التمويل", "رقم العميل", "المبلغ الممنوح", "تاريخ الصرف",
                    "مدة السداد", " نسبة الفائدة"]
        headings.append("إجراء")  # آخر عمود للزر
        for col, heading in zip(columns, headings):
            self.table.heading(col, text=heading)

        col_widths = [100, 100, 150, 150, 120, 120, 200]
        for col, width in zip(columns, col_widths):
            self.table.column(col, width=width, anchor="center")

        # ---------- Alternating row colors ----------
        self.table.tag_configure("odd", background="#f2f3f4")
        self.table.tag_configure("even", background="#ffffff")

        # ---------- Load data from RequestControler ----------
        finances_list = FinanceController()
        sample_data = finances_list.List()  # قائمة الطلبات

        for index, row in enumerate(sample_data):
            tags = ("even" if index % 2 == 0 else "odd")
            
            self.table.insert("", "end", values=row + ("اضافة ضمانة",), tags=(tags,))
        
      
        self.table.pack(fill="both", expand=True)
        self.table.bind("<Button-1>",self. on_click)
        

        # ---------- Button Row ----------
        btn_frame = tk.Frame(self, bg="#f4f6f7")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="إضافة", command=self.open_add_finances_page).pack(side="left", padx=10)

       
    def refresh_table(self):
    # Clear the table first
      for row in self.table.get_children():
        self.table.delete(row)

      finances_list = FinanceController()  
      data = finances_list.List()  # example

    # Insert updated rows
      for index, row in enumerate(data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row + ("اضافة ضمانة",), tags=(tags,))


    def open_add_finances_page(self):
        # فتح صفحة إضافة طلب
        create_add_finance_window()

    def open_add_guarante_page(self,client_id):
       
       from Project.view.add_guarante import create_add_guarantee_window
       create_add_guarantee_window(self.controller, client_id)


    def on_click(self, event):
        item_id = self.table.identify_row(event.y)
        if not item_id:
            return

        col = self.table.identify_column(event.x)
        col_index = int(col.replace("#", "")) - 1

        if col_index == len(self.table["columns"]) - 1:  # العمود الأخير
            client_values = self.table.item(item_id, "values")
            client_id = client_values[1]  # أول عمود هو Client_Id
            self.open_add_guarante_page(client_id)   