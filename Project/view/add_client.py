import tkinter as tk
from tkinter import ttk, messagebox
from Project.model.models import Client
from Project.controller.ClientController import ClientController


def create_add_client_window(parent):
    win = tk.Toplevel()

    name_entry = tk.Entry(win)
    name_entry.pack()
    def save_client():
        client = Client(
            Full_name=entry_name.get(),
            Email=entry_email.get(),
            Address=entry_address.get(),
            Gender=combo_gender.get(),
            Phone_number=entry_phone.get(),
            ID_Card=entry_nid.get(),
            Job=entry_job.get(),
            Marital_status=combo_marital_status.get(),
            Credit_rating=0,
            Salary=entry_Salary.get(),
            Aage=entry_Aage .get(),
        )

        if not (client.Full_name and client.Address and client.Marital_status and client.Job and client.Gender and client.ID_Card):
            messagebox.showerror("خطأ", "الرجاء تعبئة الحقول")
            return
        
        clientControler = ClientController()
        result = clientControler.Add(client)

        if result is True:
            messagebox.showinfo("تم", "تم إضافة العميل بنجاح")

            parent.refresh_table()

            win.destroy()

            
        else:
            messagebox.showerror("خطأ", result)

    # ---------------- تصميم الواجهة ----------------
    root = tk.Toplevel()
    root.title("إضافة عميل جديد")
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
        text="إضافة عميل جديد",
        font=("Cairo", 18, "bold"),
        bg="#F5F6FA",
        fg="#2C3E50"
    )
    title.pack(pady=20)

    # الفريم الداخلي
    frame = ttk.Frame(container, padding=15)
    frame.pack(fill="both", expand=True)

    # --- الحقول ---
    ttk.Label(frame, text="اسم العميل الرباعي:").grid(row=0, column=0, sticky="w", pady=6)
    entry_name = ttk.Entry(frame, width=32)
    entry_name.grid(row=0, column=1)

    ttk.Label(frame, text="رقم الهوية:").grid(row=1, column=0, sticky="w", pady=6)
    entry_nid = ttk.Entry(frame, width=32)
    entry_nid.grid(row=1, column=1)

    ttk.Label(frame, text="رقم الهاتف:").grid(row=2, column=0, sticky="w", pady=6)
    entry_phone = ttk.Entry(frame, width=32)
    entry_phone.grid(row=2, column=1)

    ttk.Label(frame, text="الجنس:").grid(row=3, column=0, sticky="w", pady=6)
    combo_gender = ttk.Combobox(frame, values=["ذكر", "أنثى"], width=30, state="readonly")
    combo_gender.grid(row=3, column=1)
    combo_gender.set("ذكر")

     
    ttk.Label(frame, text="العمر:").grid(row=4, column=0, sticky="w", pady=6)
    entry_Aage = ttk.Entry(frame, width=32)
    entry_Aage.grid(row=4, column=1)

    ttk.Label(frame, text="الحالة الاجتماعية:").grid(row=5, column=0, sticky="w", pady=6)
    combo_marital_status = ttk.Combobox(
        frame,
        values=["عازب", "متزوج", "أرمل", "مطلق"],
        width=30,
        state="readonly"
    )
    combo_marital_status.grid(row=5, column=1)

    ttk.Label(frame, text="الإيميل:").grid(row=6, column=0, sticky="w", pady=6)
    entry_email = ttk.Entry(frame, width=32)
    entry_email.grid(row=6, column=1)

    ttk.Label(frame, text="الوظيفة:").grid(row=7, column=0, sticky="w", pady=6)
    entry_job = ttk.Entry(frame, width=32)
    entry_job.grid(row=7, column=1)


    
    ttk.Label(frame, text="الراتب الشهري:").grid(row=8, column=0, sticky="w", pady=6)
    entry_Salary = ttk.Entry(frame, width=32)
    entry_Salary.grid(row=8, column=1)

    ttk.Label(frame, text="العنوان:").grid(row=9, column=0, sticky="w", pady=6)
    entry_address = ttk.Entry(frame, width=32)
    entry_address.grid(row=9, column=1)

   
    # زر الحفظ
    save_btn = ttk.Button(frame, text="حفظ العميل", command=save_client)
    save_btn.grid(row=10, column=0, columnspan=2, pady=20)

    return root

