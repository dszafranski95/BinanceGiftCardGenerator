from tkinter import *

root = Tk()

api_key_label = Label(root, text="API Key:")
api_key_label.grid(row=0, column=0)

api_key_entry = Entry(root)
api_key_entry.grid(row=0, column=1)

api_secret_label = Label(root, text="API Secret:")
api_secret_label.grid(row=1, column=0)

api_secret_entry = Entry(root)
api_secret_entry.grid(row=1, column=1)

success_label = Label(root, fg="green", text="")
success_label.grid(row=2, column=0, columnspan=2)

def save_keys():
    with open('keys.txt', 'w') as f:
        f.write(api_key_entry.get() + '\n')
        f.write(api_secret_entry.get() + '\n')
    success_label.config(text="SUCCESS! Your API keys have been created")

save_button = Button(root, text="Save", command=save_keys)
save_button.grid(row=3, column=0)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=3, column=1)

def save_keys():
    try:
        with open('keys.txt', 'w') as f:
            f.write(api_key_entry.get() + '\n')
            f.write(api_secret_entry.get() + '\n')
        success_label.config(text="SUCCESS! Your API keys have been created")
    except PermissionError:
        success_label.config(text="ERROR! Permission denied. Can't save the keys.", fg="red")
    except Exception as e:
        success_label.config(text=f"ERROR! {str(e)}", fg="red")


root.mainloop()
