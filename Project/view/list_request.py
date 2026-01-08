import tkinter as tk
from tkinter import ttk
from Project.controller.RequestController import RequestController
from Project.controller.ClientController import ClientController
from Project.view.add_request import create_add_request_window 
from Project.view.add_finance import create_add_finance_window 
from Project.controller.OpenAiController import OpenAIControler
from Project.model.models import Request
from Project.model.models import Client
from tkinter import ttk, messagebox

import json
import re

class RequestsTableView(ttk.Frame):
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

        columns = ("Request_Id", "Client_Id", "Finance_Type", "Required_amount",
                   "Request_State", "Request_date", "Comments", "Action","ok")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=15
        )

        headings = ["رقم الطلب", "رقم العميل", "نوع التمويل", "المبلغ المطلوب",
                    "حالة الطلب", "تاريخ الطلب", "ملاحظات اللجنة"]

        headings.append("إجراء")  # آخر عمود للزر
        headings.append("موافقة")
        for col, heading in zip(columns, headings):
            self.table.heading(col, text=heading)

        col_widths = [100, 100, 150, 150, 120, 120, 200]
        for col, width in zip(columns, col_widths):
            self.table.column(col, width=width, anchor="center")

        # ---------- Alternating row colors ----------
        self.table.tag_configure("odd", background="#f2f3f4")
        self.table.tag_configure("even", background="#ffffff")

        # ---------- Load data from RequestControler ----------
        requests_list = RequestController()
        sample_data = requests_list.List()  # قائمة الطلبات

        for index, row in enumerate(sample_data):

            tags = ("even" if index % 2 == 0 else "odd")
           # self.table.insert("", "end", values=row, tags=(tags,))
            self.table.insert("", "end", values=row + ("تحليل طلب التمويل ", "موافقة") , tags=(tags,))


        self.table.pack(fill="both", expand=True)
        self.table.bind("<Button-1>",self. on_click)
        # ---------- Button Row ----------
        btn_frame = tk.Frame(self, bg="#f4f6f7")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="إضافة", command=self.open_add_request_page).pack(side="left", padx=10)
      

    def refresh_table(self):
    # Clear the table first
      for row in self.table.get_children():
        self.table.delete(row)

      request_list = RequestController()  
      data = request_list.List()  # example

    # Insert updated rows
      for index, row in enumerate(data):
            tags = ("even" if index % 2 == 0 else "odd")
            self.table.insert("", "end", values=row + ("تحليل طلب التمويل ", "موافقة") , tags=(tags,))




    def open_add_request_page(self):
        # فتح صفحة إضافة طلب
        create_add_request_window()

    def open_add_finance_page(self,client_id):
        # فتح صفحة إضافة طلب
  
    
      from Project.view.add_finance import create_add_finance_window
      create_add_finance_window(self.controller, client_id)

    
    def on_click(self, event):
     item_id = self.table.identify_row(event.y)
     if not item_id:
        return

     col = self.table.identify_column(event.x)
     col_index = int(col.replace("#", "")) - 1

     request_values = self.table.item(item_id, "values")
     client_id = request_values[1]  # Client_Id

    # العمود قبل الأخير = "تحليل طلب التمويل"
     if col_index == len(self.table["columns"]) - 2:
        print("تشغيل تحليل")
        self.get_client_and_request_with_analyze_client(client_id, request_values)

    # العمود الأخير = "موافقة"
     elif col_index == len(self.table["columns"]) - 1:
        print("تشغيل موافقة")
        self.open_add_finance_page( client_id )
       # messagebox.showinfo("موافقة", f"تمت الموافقة على الطلب: {request_values[0]}")



    def  get_client_and_request_with_analyze_client(self, client_id:int, request:Request):

        clientController = ClientController()
        client = clientController.GetClient(client_id)
      
        openAIControler = OpenAIControler( api_key="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        client_data = {
           "Full_name": client.Full_name,
           "Age": int(client.Aage),
           "Job": client.Job,
           "Monthly_income": float(client.Salary),
           "Credit_rating": int(client.Credit_rating),
           "Marital_status": client.Marital_status,
        # "Existing_loans": int(entry_loans.get()),
           "Requested_amount": float(request[3])
           }
    
        decision =openAIControler. evaluate_with_gemini(client_data)
        status = "موافق" if decision.get("approved") else "مرفوض"
        reason = decision.get("reason", "")
        match = re.search(r"\{.*\}", reason, re.DOTALL)
        if match:
         json_str = match.group()
         data = json.loads(json_str)
         print(data)
         print("Approved:", data["approved"])
         print("Reason:", data["reason"])
         messagebox.showinfo("نتيجة تحليل العميل", f"القرار: {status}\nالتفاصيل: { data["reason"]}")
        else:
         print("No JSON found in response.")

        



