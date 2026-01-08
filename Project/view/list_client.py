
from Project.view.add_client import create_add_client_window

from Project.view.add_request import  create_add_request_window
from tkinter import ttk

from tkinter import ttk
import tkinter as tk
from Project.controller.ClientController import ClientController  # تأكد من المسار الصحيح

class ClientsTableView(ttk.Frame):

    


    def __init__(self, parent, controller=None):
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

        columns = ("Client_Id", "Full_name", "Phone_number", "Gender","Aage","ID_Card",
                   "Email", "Marital_status", "Job","Salary" , "Credit_rating", "Address", "Action")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        headings = ["ID", "الاسم الكامل", "الهاتف", "الجنس","العمر" ,"رقم البطاقة", 
                    "الايميل", "الحالة الاجتماعية", "الوظيفة", "الراتب الشهري","التصنيف الائتماني", "العنوان" ]
        headings.append("إجراء")  # آخر عمود للزر


        for col, heading in zip(columns, headings):
            self.table.heading(col, text=heading)


        # ---- Column widths ----
        col_widths = [70 , 200, 100, 100, 100, 100, 100, 100,100,100, 120, 120]
        for col, width in zip(columns, col_widths):
            self.table.column(col, width=width, anchor="center")

        # ----------- Alternating row colors ------------
        self.table.tag_configure("odd", background="#f2f3f4")
        self.table.tag_configure("even", background="#ffffff")

        # ----------- Load data from ClientControler ------------
        clients_list = ClientController()
        sample_data = clients_list.List()  # قائمة العملاء

        for index, row in enumerate(sample_data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row + ("طلب تمويل",), tags=(tags,))
        
      
        self.table.pack(fill="both", expand=True)
        self.table.bind("<Button-1>",self. on_click)

   
        # ----------- Button Row ------------
        btn_frame = tk.Frame(self, bg="#f4f6f7")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="إضافة", command=self.open_add_client_page).pack(side="left", padx=10)
  


    def refresh_tableeee(self):
        clients_list = ClientController()
        sample_data = clients_list.List()  # قائمة العملاء

        for index, row in enumerate(sample_data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row + ("طلب تمويل",), tags=(tags,))
        
      
        self.table.pack(fill="both", expand=True)
        self.table.bind("<Button-1>",self. on_click)

    def refresh_table(self):
    # Clear the table first
      for row in self.table.get_children():
        self.table.delete(row)

      clients_list = ClientController()  
      data = clients_list.List()  # example

    # Insert updated rows
      for index, row in enumerate(data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row + ("طلب تمويل",), tags=(tags,))


    def open_add_client_page(self):
        # فتح صفحة إضافة طلب
        create_add_client_window(parent=self)
       
   
    def open_add_request_finance_page(self, client_id):
      
               
       from Project.view.add_request import create_add_request_window
       create_add_request_window(self.controller, client_id)


    def on_click(self, event):
        item_id = self.table.identify_row(event.y)
        if not item_id:
            return

        col = self.table.identify_column(event.x)
        col_index = int(col.replace("#", "")) - 1

        if col_index == len(self.table["columns"]) - 1:  # العمود الأخير
            client_values = self.table.item(item_id, "values")
            client_id = client_values[0]  # أول عمود هو Client_Id
            self.open_add_request_finance_page(client_id)    