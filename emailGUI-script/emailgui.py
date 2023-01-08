import smtplib
import tkinter as tk
import tkinter.messagebox as msgbox
import random
from os.path import exists

root = tk.Tk()
root.title("Email GUI")
root.geometry("450x225")
root.resizable(False, False)

# email_logo

file_exists = exists("logo.png")
if file_exists is True:
    image = tk.PhotoImage(file="logo.png")
    root.iconphoto(False, image)
else:
    pass

def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(user_mail.get(), user_pass.get())
    except:
        error = "please enter credentials carefully or read readme.md file"
        msgbox.showerror(title="login error", message=error)
    # Send the email
    for i in range(0, mail_count.get()):
        q = random.randint(1, 100)
        message = f"Subject: {sub.get() + str(q)}\n\n{Message.get()}"
        if mail_count.get() == 1:
            message = f"Subject: {sub.get()}\n\n{Message.get()}"
        server.sendmail(user_mail.get(), rec_mail.get(), message)
    server.close()
    msgbox.showinfo(title="status", message="mail have been sent")

# heading
tk.Label(text="Email GUI", font=("cosmic sans ms", 18, "bold")).grid()

# values
user_mail = tk.StringVar()
user_pass = tk.StringVar()
rec_mail = tk.StringVar()
sub = tk.StringVar()
Message = tk.StringVar()
mail_count = tk.IntVar()
mail_count.set(1)

# labels
tk.Label(text="You're Email ID").grid(row=4, column=0)
tk.Label(text="your password").grid(row=5, column=0)
tk.Label(text="receiver's Email ID").grid(row=6)
tk.Label(text="enter your subject").grid(row=7, column=0)
tk.Label(text="enter your message").grid(row=8, column=0)
tk.Button(text="send", relief='groove', bd=3, command=email).grid(row=10, column=1)
tk.Label(text="Number of mails").grid(row=9, column=0)

# entries
tk.Entry(width=45, bd=3, textvariable=user_mail).grid(row=4, column=1)
tk.Entry(width=45, bd=3, textvariable=user_pass, show="*").grid(row=5, column=1)
tk.Entry(width=45, bd=3, textvariable=rec_mail).grid(row=6, column=1)
tk.Entry(width=45, bd=3, textvariable=sub).grid(row=7, column=1)
tk.Entry(width=45, bd=3, textvariable=Message).grid(row=8, column=1)
tk.Entry(width=45, bd=3, textvariable=mail_count).grid(row=9, column=1)

root.mainloop()

