
import tkinter as tk
from tkinter import ttk, messagebox
from Project.model.models import Guarantee
from Project.controller.GuaranteeController import GuaranteeControler
from tkcalendar import DateEntry

def create_add_guarantee_window(controller , client_id):
    win = tk.Toplevel()

    name_entry = tk.Entry(win)
    name_entry.pack()
    def save_guarantee():

        client_id_get=None
        if(client_id!=None):
            client_id_get=client_id
        else :
            client_id_get=entry_client_id.get()


        guarantee = Guarantee(
            Client_Id=client_id_get,
            Guarante_Type=combo_guarante_type.get(),
            Guarante_state=combo_guarante_state .get(),
            Guarante_amount=entry_guarante_amount.get(),
            
       
           
        )

        if not (guarantee.Client_Id and guarantee.Guarante_Type and guarantee.Guarante_amount ):
            messagebox.showerror("خطأ", "الرجاء  تعبئة الحقول")
            return
        
        guaranteeController = GuaranteeControler()
        result = guaranteeController.Add(guarantee)

        if result is True:
            messagebox.showinfo("تم", "تم إضافة الضمانة بنجاح")               
            from Project.view.list_guarante import GuarantesTableView
            guarntee_page = controller.get_page(GuarantesTableView)
            guarntee_page.refresh_table()
            win.destroy()            

        else:
            messagebox.showerror("خطأ", result)

    # ---------------- تصميم الواجهة ----------------
    root = tk.Toplevel()
    root.title("إضافة  ضمانة ")
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
        text="إضافة ضمانة",
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

    ttk.Label(frame, text="نوع الضمانة:").grid(row=1, column=0, sticky="w", pady=6)
    combo_guarante_type = ttk.Combobox(frame, values=["كفيل", "عقاري","وديعة","ذهب"], width=30, state="readonly")
    combo_guarante_type.grid(row=1, column=1)
   

    ttk.Label(frame, text="قيمة الضمان:").grid(row=2, column=0, sticky="w", pady=6)
    entry_guarante_amount = ttk.Entry(frame, width=32)
    entry_guarante_amount  .grid(row=2, column=1)

    ttk.Label(frame, text="حالة الضمانة:").grid(row=3, column=0, sticky="w", pady=6)
    combo_guarante_state = ttk.Combobox(frame, values=["مستخدم", "جديد"], width=30, state="readonly")
    combo_guarante_state.grid(row=3, column=1)
   



    
    # زر الحفظ
    save_btn = ttk.Button(frame, text="حفظ الطلب", command=save_guarantee)
    save_btn.grid(row=4, column=0, columnspan=2, pady=20)

    return root

