
import tkinter as tk
from tkinter import ttk, messagebox
from Project.model.models import Request
from Project.controller.RequestController import RequestController
from tkcalendar import DateEntry

def create_add_request_window(controller,client_id):
    win = tk.Toplevel()

    name_entry = tk.Entry(win)
    name_entry.pack()


    def save_request():
        client_id_get=None
        if(client_id!=None):
            client_id_get=client_id
        else :
            client_id_get=entry_client_id.get()


        request = Request(
            Client_Id=client_id_get,
            Finance_Type= combo_finance_type.get(),
            Required_amount=entry_required_amount .get(),
            Request_State=combo_request_state.get(),
            Request_date= entry_request_date.get(),
            Comments= entry_comments.get(),
           
        )

        if not (request.Client_Id and request.Finance_Type and request.Required_amount ):
            messagebox.showerror("خطأ", "الرجاء  تعبئة الحقول")
            return
        
        requestControler = RequestController()
        result = requestControler.Add(request)

        if result is True:
            messagebox.showinfo("تم", "تم إضافة الطلب بنجاح")
                        
       
            from Project.view.list_request import RequestsTableView
            request_page = controller.get_page(RequestsTableView)
            request_page.refresh_table()

            win.destroy()
        else:
            messagebox.showerror("خطأ", result)

    # ---------------- تصميم الواجهة ----------------
    root = tk.Toplevel()
    root.title("إضافة طلب تمويل جديد")
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
        text="إضافة طلب تمويل جديد",
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
 
        
    #ttk.Label(frame, text="نوع التمويل:").grid(row=1, column=0, sticky="w", pady=6)
    #entry_finance_type= ttk.Entry(frame, width=32)
    #entry_finance_type.grid(row=1, column=1)

    ttk.Label(frame, text="نوع التمويل:").grid(row=1, column=0, sticky="w", pady=6)
    combo_finance_type= ttk.Combobox(frame, values=["تمويل عقاري", "تمويل مشروع", "قرض شخصي"], width=30, state="readonly")
    combo_finance_type.grid(row=1, column=1)
  

    ttk.Label(frame, text="المبلغ المطلوب:").grid(row=2, column=0, sticky="w", pady=6)
    entry_required_amount = ttk.Entry(frame, width=32)
    entry_required_amount .grid(row=2, column=1)

    ttk.Label(frame, text="حالة الطلب:").grid(row=3, column=0, sticky="w", pady=6)
    combo_request_state= ttk.Combobox(frame, values=["قيد الدراسة", "مقبول", "مرفوض"], width=30, state="readonly")
    combo_request_state.grid(row=3, column=1)
    combo_request_state.set("قيد الدراسة")



    ttk.Label(frame, text="تاريخ الطلب:").grid(row=5, column=0, sticky="w", pady=5)

    entry_request_date = DateEntry(frame, width=32, date_pattern='yyyy-mm-dd')
    entry_request_date.grid(row=5, column=1, sticky="w", pady=5)  # استخدم grid هنا
    
  

    ttk.Label(frame, text="ملاحظات اللجنة:").grid(row=6, column=0, sticky="w", pady=6)
    entry_comments= ttk.Entry(frame, width=32)
    entry_comments.grid(row=6, column=1)

    
    # زر الحفظ
    save_btn = ttk.Button(frame, text="حفظ الطلب", command=save_request)
    save_btn.grid(row=8, column=0, columnspan=2, pady=20)

    return root

