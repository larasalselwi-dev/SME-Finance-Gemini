
from tkinter import ttk

from tkinter import ttk
import tkinter as tk
from Project.controller.GuaranteeController import GuaranteeControler  # تأكد من المسار الصحيح

class GuarantesTableView(ttk.Frame):



    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # 
        # ----------- Style ------------
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

        # ----------- Table Frame ------------
        table_frame = tk.Frame(self)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("Guarante_Id", "Client_Id", "Guarante_Type", "Guarante_state", "Guarante_amount"
                   )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        headings = ["رقم الضمانة", "رقم العميل", "نوع الضمانة", "حالة الضمانة", "مبلغ الضمانة"
                 ]

        for col, heading in zip(columns, headings):
            self.table.heading(col, text=heading)

        # ---- Column widths ----
        col_widths = [70, 200, 150, 120, 120, 120, 120, 120, 120, 120]
        for col, width in zip(columns, col_widths):
            self.table.column(col, width=width, anchor="center")

        # ----------- Alternating row colors ------------
        self.table.tag_configure("odd", background="#f2f3f4")
        self.table.tag_configure("even", background="#ffffff")

        # ----------- Load data from ClientControler ------------
        guarant_list = GuaranteeControler()
        sample_data = guarant_list.List()  # قائمة العملاء

        for index, row in enumerate(sample_data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row, tags=(tags,))

        self.table.pack(fill="both", expand=True)

        # ----------- Button Row ------------
        btn_frame = tk.Frame(self, bg="#f4f6f7")
        btn_frame.pack(pady=10)



    def refresh_table(self):
    # Clear the table first
      for row in self.table.get_children():
        self.table.delete(row)

      guarantee_list = GuaranteeControler()  
      data = guarantee_list.List()  # example

    # Insert updated rows
      for index, row in enumerate(data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row, tags=(tags,))








