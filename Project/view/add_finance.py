import tkinter as tk
from tkinter import ttk, messagebox
from Project.model.models import Finance
from Project.controller.FinanceController import FinanceController
from tkcalendar import DateEntry


def create_add_finance_window(controller,client_id):
    win = tk.Toplevel()

    name_entry = tk.Entry(win)
    name_entry.pack()

    def save_finance():

        client_id_get=None
        if(client_id!=None):
            client_id_get=client_id
        else :
            client_id_get=entry_client_id.get()
   
        finance = Finance(
            Client_Id=client_id_get,
            Amount_granted=entry_amount_granted.get(),
            Payment_term=entry_payment_term .get(),
            Interest_rate=entry_interest_rate.get(),
            Exchange_date= entry_exchange_date .get(),
       
           
        )

        if not (finance.Client_Id and finance.Amount_granted and finance.Payment_term ):
            messagebox.showerror("خطأ", "الرجاء  تعبئة الحقول")
            return
        
        financeControler = FinanceController()
        result = financeControler.Add(finance)

        if result is True:
            messagebox.showinfo("تم", "تم إضافة التمويل بنجاح")
            
       
            from Project.view.list_finance import FinanceTableView
            finance_page = controller.get_page(FinanceTableView)
            finance_page.refresh_table()

            win.destroy()

        else:
            messagebox.showerror("خطأ", result)

    # ---------------- تصميم الواجهة ----------------
    root = tk.Toplevel()
    root.title("إضافة  تمويل جديد")
    root.geometry("480x520")
    root.configure(bg="#F5F6FA")
    root.resizable(False, False)

    # تنسيق عام
    style = ttk.Style()
    style.configure("TLabel", font=("Cairo", 13))
    style.configure("TEntry", font=("Cairo", 12))
    style.configure("TButton", font=("Cairo", 12), padding=8)
    style.configure("TCombobox", font=("Cairo", 12))

    # فريم أساسي مع تصميم جميل
    container = tk.Frame(root, bg="white", bd=2, relief="flat")
    container.place(relx=0.5, rely=0.54, anchor="center", width=430, height=450)

    # عنوان جميل
    title = tk.Label(
        root,
        text="إضافة تمويل جديد",
        font=("Cairo", 18, "bold"),
        bg="#F5F6FA",
        fg="#2C3E50"
    )
    title.pack(pady=20)

    # الفريم الداخلي
    frame = ttk.Frame(container, padding=15)
    frame.pack(fill="both", expand=True)

    # --- الحقول ---
    if(client_id==None):
      ttk.Label(frame, text="رقم العميل:").grid(row=0, column=0, sticky="w", pady=6)
      entry_client_id = ttk.Entry(frame, width=32)
      entry_client_id.grid(row=0, column=1)


    ttk.Label(frame, text="المبلغ الممنوح:").grid(row=1, column=0, sticky="w", pady=6)
    entry_amount_granted = ttk.Entry(frame, width=32)
    entry_amount_granted  .grid(row=1, column=1)




    ttk.Label(frame, text="تاريخ الصرف:").grid(row=2, column=0, sticky="w", pady=5)
    entry_exchange_date = DateEntry(frame, width=30, date_pattern='yyyy-mm-dd')
    entry_exchange_date.grid(row=2, column=1, sticky="w", pady=5)  # استخدم grid هنا
    


    ttk.Label(frame, text=" مدة السداد:").grid(row=3, column=0, sticky="w", pady=6)
    entry_payment_term= ttk.Entry(frame, width=32)
    entry_payment_term.grid(row=3, column=1)


    ttk.Label(frame, text="نسبة الفائدة:").grid(row=4, column=0, sticky="w", pady=6)
    entry_interest_rate= ttk.Entry(frame, width=32)
    entry_interest_rate.grid(row=4, column=1)
    
    # زر الحفظ
    save_btn = ttk.Button(frame, text="حفظ الطلب", command=save_finance)
    save_btn.grid(row=5, column=0, columnspan=2, pady=20)

    return root

