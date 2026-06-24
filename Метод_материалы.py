import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

COLOR_BG = "#F8F9FA"         
COLOR_CARD = "#FFFFFF"      
COLOR_ACCENT = "#1E7E34"     
COLOR_TEXT_MAIN = "#212529"   
COLOR_TEXT_SEC = "#6C757D"   
COLOR_BORDER = "#DEE2E6"     
COLOR_DANGER = "#C82333"    

class MethodicalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Система учета методических материалов")
        self.geometry("850x650")
        self.configure(bg=COLOR_BG)

        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.style.configure("TLabel", background=COLOR_BG, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 11))
        self.style.configure("Card.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 11))
        self.style.configure("Subtitle.TLabel", background=COLOR_CARD, foreground=COLOR_TEXT_SEC, font=("Segoe UI", 10))
        self.style.configure("TRadiobutton", background=COLOR_CARD, foreground=COLOR_TEXT_MAIN, font=("Segoe UI", 10), focuscolor=COLOR_CARD)
        
        self.current_user = ""
        self.current_role = ""
        self.materials = [
            {"id": 1, "author": "Петров И.И.", "title": "Методические указания по Python", "subject": "Программирование", "type": "Пособие", "status": "Одобрено"},
            {"id": 2, "author": "Сидоров К.М.", "title": "Лабораторный практикум по БД", "subject": "Базы данных", "type": "Практикум", "status": "На проверке"}
        ]
        
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_screen()
        
        main_title = tk.Label(self, text="Электронный учет методматериалов", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 24, "bold"))
        main_title.pack(pady=(60, 20))
        
        login_card = tk.Frame(self, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=0)
        login_card.config(highlightbackground=COLOR_BORDER)
        login_card.pack(pady=20, padx=40, ipady=30, ipadx=30)
        
        ttk.Label(login_card, text="Авторизация в системе", style="Card.TLabel", font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 5))
        ttk.Label(login_card, text="Пожалуйста, введите данные для входа", style="Subtitle.TLabel").pack(anchor="w", pady=(0, 25))
        
        input_frame = tk.Frame(login_card, bg=COLOR_CARD)
        input_frame.pack(fill="x", pady=5)
        ttk.Label(input_frame, text="ФИО Сотрудника / Преподавателя", style="Card.TLabel").pack(anchor="w")
        
        self.username_entry = tk.Entry(input_frame, bg="#FFFFFF", fg=COLOR_TEXT_MAIN, insertbackground=COLOR_ACCENT, 
                                       width=40, font=("Segoe UI", 12), bd=1, relief="solid")
        self.username_entry.insert(0, "Иванов Иван Иванович")
        self.username_entry.pack(fill="x", ipady=8, pady=(5, 15))
        
        ttk.Label(login_card, text="Ваша роль в системе", style="Card.TLabel").pack(anchor="w", pady=(10, 5))
        
        self.role_var = tk.StringVar(value="Преподаватель")
        role_frame = tk.Frame(login_card, bg=COLOR_CARD)
        role_frame.pack(fill="x", pady=5)
        
        ttk.Radiobutton(role_frame, text="Преподаватель", variable=self.role_var, value="Преподаватель").pack(side="left", padx=(0, 15))
        ttk.Radiobutton(role_frame, text="Методист", variable=self.role_var, value="Методист").pack(side="left", padx=15)
        ttk.Radiobutton(role_frame, text="Администратор", variable=self.role_var, value="Администратор").pack(side="left", padx=15)
        

        btn_frame = tk.Frame(login_card, bg=COLOR_CARD)
        btn_frame.pack(fill="x", pady=(35, 0))
        
        login_btn = tk.Button(btn_frame, text="Войти в панель", bg=COLOR_ACCENT, fg="#FFFFFF", 
                              font=("Segoe UI", 12, "bold"), activebackground="#145A24", 
                              activeforeground="#FFFFFF", width=20, bd=0, relief="flat",
                              command=self.handle_login)
        login_btn.pack(side="right")

    def handle_login(self):
        self.current_user = self.username_entry.get().strip()
        self.current_role = self.role_var.get()
        
        if not self.current_user:
            messagebox.showwarning("Внимание", "Пожалуйста, введите Ваше имя для авторизации.")
            return
            
        if self.current_role == "Преподаватель":
            self.show_teacher_screen()
        else:
            self.show_manager_screen()  

    def show_teacher_screen(self):
        self.clear_screen()
        
        header = tk.Frame(self, bg=COLOR_CARD, bd=1, relief="solid")
        header.pack(fill="x")
        tk.Label(header, text=f"Личный кабинет: {self.current_user} ({self.current_role})", bg=COLOR_CARD, fg=COLOR_TEXT_MAIN, font=("Segoe UI", 11)).pack(side="left", padx=20, pady=10)
        tk.Button(header, text="Выйти", bg=COLOR_DANGER, fg="#FFFFFF", font=("Segoe UI", 10), bd=0, padx=15, command=self.show_login_screen).pack(side="right", padx=20, pady=10)
        
        tk.Label(self, text="Подача материала на регистрацию", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=40, pady=25)
        
        content_frame = tk.Frame(self, bg=COLOR_BG)
        content_frame.pack(fill="both", expand=True, padx=40)
        
        form_card = tk.Frame(content_frame, bg=COLOR_CARD, padx=25, pady=25, bd=1, relief="solid", width=380)
        form_card.pack(side="left", fill="y", pady=(0, 20))
        form_card.pack_propagate(False)
        
        def create_input(parent, label_text, default_val):
            frame = tk.Frame(parent, bg=COLOR_CARD)
            frame.pack(fill="x", pady=8)
            ttk.Label(frame, text=label_text, style="Card.TLabel").pack(anchor="w")
            entry = tk.Entry(frame, bg="#FFFFFF", fg=COLOR_TEXT_MAIN, bd=1, relief="solid", font=("Segoe UI", 11))
            entry.insert(0, default_val)
            entry.pack(fill="x", ipady=5, pady=(4, 0))
            return entry

        title_entry = create_input(form_card, "Название материала", "Методическое пособие по ООП")
        subject_entry = create_input(form_card, "Учебная дисциплина", "Информатика")
        type_entry = create_input(form_card, "Тип публикации", "Учебное пособие")
        
        def submit_material():
            new_id = len(self.materials) + 1
            new_mat = {
                "id": new_id,
                "author": self.current_user,
                "title": title_entry.get(),
                "subject": subject_entry.get(),
                "type": type_entry.get(),
                "status": "На проверке"
            }
            self.materials.append(new_mat)
            messagebox.showinfo("Успех", f"Материал зарегистрирован под ID #{new_id} и отправлен методисту.")
            self.show_teacher_screen()
            
        tk.Button(form_card, text="Зарегистрировать материал", bg=COLOR_ACCENT, fg="#FFFFFF", 
                  font=("Segoe UI", 11, "bold"), bd=0, pady=10, command=submit_material).pack(fill="x", pady=(25, 0))

        list_frame = tk.Frame(content_frame, bg=COLOR_BG, padx=20)
        list_frame.pack(side="left", fill="both", expand=True)
        tk.Label(list_frame, text="Мои поданные материалы:", bg=COLOR_BG, fg=COLOR_TEXT_SEC, font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 10))
        
        for m in self.materials:
            if m["author"] == self.current_user:
                txt = f"• {m['title']}\n  Дисциплина: {m['subject']} | Статус: {m['status']}"
                tk.Label(list_frame, text=txt, bg=COLOR_BG, fg=COLOR_TEXT_MAIN, font=("Segoe UI", 10), justify="left").pack(anchor="w", pady=6)


    def show_manager_screen(self):
        self.clear_screen()
        
        header = tk.Frame(self, bg=COLOR_CARD, bd=1, relief="solid")
        header.pack(fill="x")
        tk.Label(header, text=f"Панель учета: {self.current_user} ({self.current_role})", bg=COLOR_CARD, fg=COLOR_TEXT_MAIN, font=("Segoe UI", 11)).pack(side="left", padx=20, pady=10)
        tk.Button(header, text="Выйти", bg=COLOR_DANGER, fg="#FFFFFF", font=("Segoe UI", 10), bd=0, padx=15, command=self.show_login_screen).pack(side="right", padx=20, pady=10)
        
        tk.Label(self, text="Реестр методических разработок кафедры", bg=COLOR_BG, fg=COLOR_ACCENT, font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=40, pady=25)
        
        table_card = tk.Frame(self, bg=COLOR_CARD, padx=20, pady=20, bd=1, relief="solid")
        table_card.pack(fill="both", expand=True, padx=40, pady=(0, 20))
        
        self.style.configure("Treeview", background="#FFFFFF", foreground=COLOR_TEXT_MAIN, rowheight=30, fieldbackground="#FFFFFF", font=("Segoe UI", 10))
        self.style.map("Treeview", background=[('selected', COLOR_ACCENT)], foreground=[('selected', '#FFFFFF')])
        self.style.configure("Treeview.Heading", background=COLOR_BG, foreground=COLOR_TEXT_SEC, font=("Segoe UI", 10, "bold"))
        
        columns = ("id", "author", "title", "subject", "type", "status")
        tree = ttk.Treeview(table_card, columns=columns, show="headings", height=12)
        
        tree.heading("id", text="ID")
        tree.heading("author", text="Автор (Преподаватель)")
        tree.heading("title", text="Название материала")
        tree.heading("subject", text="Дисциплина")
        tree.heading("type", text="Тип")
        tree.heading("status", text="Статус")
        
        tree.column("id", width=40, anchor="center")
        tree.column("author", width=150)
        tree.column("title", width=250)
        tree.column("subject", width=130)
        tree.column("type", width=100, anchor="center")
        tree.column("status", width=100, anchor="center")
        
        for m in self.materials:
            tree.insert("", "end", values=(m["id"], m["author"], m["title"], m["subject"], m["type"], m["status"]))
            
        tree.pack(fill="both", expand=True)
        
        def approve_material():
            selected = tree.selection()
            if selected:
                item_values = tree.item(selected, "values")
                mat_id = int(item_values[0])
                for m in self.materials:
                    if m["id"] == mat_id:
                        m["status"] = "Одобрено"
                
                tree.set(selected, "status", "Одобрено")
                messagebox.showinfo("Система учета", "Статус материала успешно изменен на 'Одобрено'.")
            else:
                messagebox.showwarning("Внимание", "Пожалуйста, выберите строчку с материалом из таблицы.")

        action_frame = tk.Frame(table_card, bg=COLOR_CARD)
        action_frame.pack(fill="x", pady=(20, 0))
        
        tk.Button(action_frame, text="Утвердить и принять на учет", bg=COLOR_ACCENT, fg="#FFFFFF", 
                  font=("Segoe UI", 11, "bold"), bd=0, padx=20, pady=8, command=approve_material).pack(side="right")


if __name__ == "__main__":
    app = MethodicalApp()
    app.mainloop()
