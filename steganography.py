import _tkinter
import tkinter as tk
from PIL import ImageTk,Image, ImageOps
from tkinter import filedialog
import ntpath
import stepic
from cryptography.fernet import Fernet
from stegano import lsb
from tkinter import messagebox

# To display the root window
root = tk.Tk()
root.geometry("600x250")
root.resizable(width=False, height=False)
root.title('Cryptography & Steganography')
root.configure(bg='pink')


# The text encryption and text hiding GUI
def New_page():
    popup = tk.Toplevel() # A Toplevel widget is used to create a window on top of all other windows
    popup.grab_set()      # Routes all events for this application to this widget.
    popup.geometry("650x1000")
    popup.resizable(width=False,height=False)
    popup.configure(bg='pink')
    popup.title('Text Encryption and Image Steganography Application')

    def show_image():
        global img2
        global res2

        popup.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        path = ntpath.basename(popup.filename)

        width = 300
        height = 300

        res = Image.open(popup.filename)
        res2 = res.resize((width, height), Image.NEAREST)
        popup.image = res2

        img2 = ImageTk.PhotoImage(res2)

        canvas = tk.Canvas(popup, width=300, height=300)

        img3 = canvas.create_image(0, 0, anchor='nw', image=img2)
        canvas.image = img2  # keep a reference

        canvas.grid(row=1, rowspan=3, column=0, sticky='ns', padx=5, pady=5)

        v = tk.StringVar()
        v.set(popup.filename)
        tk.Entry(popup, textvariable=v).grid(row=4, column=0, sticky='we', padx=2, pady=2)

        encrypt_button.config(state=tk.NORMAL)

        res2.save('im1.jpg', 'PNG')

    # To encrypt the text    
    def encryption_code():
        global encrypted_value, key
        result = TextArea.get("1.0", 'end-1c')   #The text area

        if (not result):
            messagebox.showerror("Error", "Enter Text to Encrypt and Hide")
        else:
            # Put this somewhere safe!
            key = Fernet.generate_key()  # generated key
            f = Fernet(key)
            result_test = result.encode()  # Encoding the text in the text area box
            token = f.encrypt(result_test)

            normal = token.decode()

            v = tk.StringVar()
            v.set(normal)
            encrypted_value = v.get()

            decrpted = f.decrypt(token)

            TextArea.delete('1.0', 'end-1c')
            TextArea.insert('1.0', encrypted_value)

            key_number.insert(0, key)
            hide_button.config(state=tk.NORMAL)
            save_key.config(state=tk.NORMAL)

    def save_ekey():
        files = [('Text Document', '*.txt'),
                 ('Word Files', '*.doc')]
        converted = key.decode()
        file_p = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        file_p.write(converted)

    # exist window
    def quit():
        popup.destroy()

    def clear_text():
        TextArea.delete('1.0', 'end-1c')
        key_number.delete(0, 'end')

    def stegno_image():
        global stegno_img, secret
        secret = lsb.hide(res2, encrypted_value)
        secret.save('help4.jpg', 'PNG')
        time = secret
        root.image = res2

        stegno_img = ImageTk.PhotoImage(secret)

        img4 = hide_field.create_image(0, 0, anchor='nw', image=stegno_img)
        hide_field.image = stegno_img  # keep a reference
        hide_field.grid(row=7, column=0, rowspan=3, sticky='ns', columnspan=4, padx=5, pady=5)
        save.config(state=tk.NORMAL)

    def save_image():
        files = [('Joint Photographic Experts Group(JPEG)', '*.jpg')]
        file_p = filedialog.asksaveasfile(mode='w+b', defaultextension='.jpg')
        secret.save(file_p, 'PNG')

    # load Image
    load_image = tk.Label(popup, text="Select Image", font=("Arial Bold", 12)).grid(row=0,
                                                                                                  column=0, pady=4)  # Create a text label

    image_field = tk.Canvas(popup, width=300, height=300, bg="black")
    image_field.grid(row=1, column=0, rowspan=3, sticky='ns', padx=5)

    filepath = tk.Entry(popup, text="").grid(row=4, column=0, sticky='we', padx=2, pady=2)

    # load image button
    load_image_button = tk.Button(popup, text="Select Image", command=show_image, bg="black", fg="white").grid(row=5, column=0,
                                                                                    sticky='we')  # Create a text label

    # Encrpt Text
    encrpt_text = tk.Label(popup, text="Insert Message", font=("Arial Bold", 12)).grid(row=0,
                                                                                                 column=1, columnspan=2)  # Create a text label

    # To create the text area to load the text for encoding and decoding
    TextArea = tk.Text(popup, width=40, height=16, bg="black", fg="white")
    TextArea.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='ns', ipadx=1, padx=5)

    key_number = tk.Entry(popup, text="", bg="black", fg="white")
    key_number.grid(row=3, column=1, columnspan=2, sticky='we', padx=2, pady=2)

    # encrypt_field = tk.Entry(root, text="").grid(row=1, column=1,rowspan=3,sticky='ns', ipadx=80, padx=5, pady=5)

    # load image button
    encrypt_button = tk.Button(popup, text="Encode Message", command=encryption_code, state=tk.DISABLED)
    encrypt_button.grid(row=4, column=1, sticky='we', padx=5)  # Create a text label

    save_key = tk.Button(popup, text="Save Generated Key", command=save_ekey, state=tk.DISABLED)
    save_key.grid(row=4, column=2, sticky='we', padx=5)  # Create a text label
    # Clear loaded image button
    clear_text_button = tk.Button(popup, text="Clear Text", bg="black", font=("Arial Bold", 9), fg="white", command=clear_text).grid(row=5,
                                                                                                          column=1,
                                                                                                          columnspan=2,
                                                                                                          sticky='we',
                                                                                                          padx=5)  # Create a text label

    # Hide Text in image
    Hide_image = tk.Label(popup, text="Hide Text", font=("Arial Bold", 12)).grid(row=6, column=0,
                                                                               columnspan=4,pady=4)  # Create a text label

    hide_field = tk.Canvas(popup, width=300, height=300, bg="black")
    hide_field.grid(row=7, column=0, rowspan=3, sticky='ns', columnspan=4, padx=5)

    # Hide Text in image button
    hide_button = tk.Button(popup, text="Hide Message", command=stegno_image, state=tk.DISABLED)
    hide_button.grid(row=10, column=0, sticky='we', padx=5)  # Create a text label

    # load image button
    save = tk.Button(popup, text="Save Image", state=tk.DISABLED, command=save_image)
    save.grid(row=10, column=1, sticky='we', columnspan=2, padx=5)  # Create a text label

    # Clear loaded image button
    exit_button = tk.Button(popup, text="Exit", bg="black", fg="white", command=quit).grid(row=11, column=0, sticky='we',
                                                                                        columnspan=4,
                                                                                        padx=5)  # Create a text label

def retrieve_page():
    rpopup = tk.Toplevel()
    rpopup.grab_set()
    rpopup.geometry("650x450")
    rpopup.resizable(width=False, height=False)
    rpopup.configure(bg='pink')
    rpopup.title('Retrieve Hidden Message')

    def show_image():
        global img2
        global res2

        rpopup.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        path = ntpath.basename(rpopup.filename)

        width = 300
        height = 300

        res = Image.open(rpopup.filename)
        res2 = res.resize((width, height), Image.NEAREST)
        rpopup.image = res2

        img2 = ImageTk.PhotoImage(res2)

        canvas = tk.Canvas(rpopup, width=300, height=300)

        img3 = canvas.create_image(0, 0, anchor='nw', image=img2)
        canvas.image = img2  # keep a reference

        canvas.grid(row=2, column=0, columnspan=2, rowspan=3, sticky='ns', padx=5, pady=5)

        v = tk.StringVar()
        v.set(rpopup.filename)
        tk.Entry(rpopup, textvariable=v).grid(row=5, column=1, sticky='we', padx=(0, 5), pady=2)

        retrieve_button.config(state=tk.NORMAL)

    def decryption_code():
        global decrypted_value, decrpted_text
        result = TextArea.get("1.0", 'end-1c')

        f = key_number.get()

        encoded_text = result.encode()
        if len(key_number.get()) == 0:
            messagebox.showerror("Error", "Enter Encryption Key")
        else:
            try:
                token = Fernet(f)
            except ValueError:
                messagebox.showerror("Error", "Incorrect Decryption Key")
            else:
                decrpted = token.decrypt(encoded_text)
                decrpted_text = decrpted.decode()

                v = tk.StringVar()
                v.set(decrpted_text)

                TextArea.delete('1.0', 'end-1c')
                TextArea.insert('1.0', decrpted_text)

                save.config(state=tk.NORMAL)

    def save_button():
        files = [('Text Document', '*.txt'),
                 ('Word Files', '*.doc')]
        file_p = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        file_p.write(decrpted_text)

    # exist window
    def quit():
        rpopup.destroy()

    def stegno_image():
        global stegno_img

        clear_message = lsb.reveal(res2)
        value = str(clear_message)
        if (value == "None"):
            messagebox.showerror("Error", "No Hidden Text in Selected Image")
        else:
            TextArea.insert('1.0', value)
            decrypt_button.config(state=tk.NORMAL)

    #label_panel = tk.Label(rpopup, text="Retrieve Hidden Message", font=("Arial Bold", 13)).grid(row=0,
    #                                                                                                       column=0,
    #                                                                                                       columnspan=4)  # Create a text label
    # load Image
    load_image = tk.Label(rpopup, text="Load Stegno Image", font=("Arial Bold", 12)).grid(row=1, column=0,
                                                                                                   columnspan=2, pady=7)  # Create a text label

    image_field = tk.Canvas(rpopup, width=300, height=300, bg="black")
    image_field.grid(row=2, column=0, columnspan=2, rowspan=3, sticky='ns', padx=5, pady=5)

    filepathname = tk.Label(rpopup, text="Image Path: ", font=("Arial ", 10)).grid(row=5, column=0,
                                                                                 padx=(5, 0))  # Create a text label
    filepath = tk.Entry(rpopup, text="", fg="white", bg="black").grid(row=5, column=1, sticky='we', padx=(0, 5), pady=2)

    load_image_button = tk.Button(rpopup, text="Load Image", bg="white", fg="black", command=show_image).grid(row=6,
                                                                                                            column=0,
                                                                                                            sticky='we',
                                                                                                            padx=5,
                                                                                                            pady=2)  # load image button

    retrieve_button = tk.Button(rpopup, text="Retrieve Hidden Text", bg="white", fg="black", command=stegno_image,
                                state=tk.DISABLED)
    retrieve_button.grid(row=6, column=1, sticky='we', padx=5, pady=2)  # Retrieve Hidden Text in image

    Decrypt_textlabel = tk.Label(rpopup, text="Retrieved Message", font=("Arial Bold", 12),
                                 ).grid(row=1, column=2, columnspan=2)  # Encrpt Text

    TextArea = tk.Text(rpopup, width=40, height=16, fg="white", bg="black")
    TextArea.grid(row=2, column=2, rowspan=3, sticky='ns', ipadx=1, padx=5, pady=5,
                  columnspan=2)  # To Display cipher Text

    key_value = tk.Label(rpopup, text="Enter Key: ", font=("Arial ", 10)).grid(row=5, column=2)  # Create a text label

    key_number = tk.Entry(rpopup, text="", fg="white", bg="black")
    key_number.grid(row=5, column=3, sticky='we', padx=2, pady=2)  # enter encyption key

    decrypt_button = tk.Button(rpopup, text="Decrypt Text", bg="white", fg="black", command=decryption_code,
                               state=tk.DISABLED)
    decrypt_button.grid(row=6, column=2, sticky='we', padx=5, pady=2)  # decryption button

    save = tk.Button(rpopup, text="Save Decrypted Text", bg="white", fg="black", state=tk.DISABLED, command=save_button)
    save.grid(row=6, column=3, sticky='we', padx=5)  # Save Retrieved and decrypted Text

    exit_button = tk.Button(rpopup, text="Exit", bg="black", fg="white", command=quit).grid(row=7, column=0, sticky='we',
                                                                                        padx=5, pady=2,
                                                                                        columnspan=4)  # Exit GUI


#exist window
def quit():
    global root
    root.quit()

#Hide Text in image
main_label = tk.Label(root, text="High Security Steganography Platform",font=("Arial Bold", 24)).grid(row=0, column=0, columnspan=6, ipadx=5, ipady=5) # Create a text label
#head = tk.Label(root, text="Click any button to continue",font=("Arial Bold", 10),fg="black").grid(row=1, column=0, columnspan=3, ipadx=10, pady=10) # Create a text label

#Hide Text in image button
hide_image_button = tk.Button(root, text="Hide Message", height=8, bg="black", fg="white", font=("Arial Bold", 12), command=New_page)
hide_image_button.grid(row=2, column=0, columnspan=2, sticky='we', padx=5,  pady=9) # Create a text label

#load image button
Retrieve_image_button = tk.Button(root, text="Retrieve Message", font=("Arial Bold", 12), height=8, command=retrieve_page)
Retrieve_image_button.grid(row=2, column=2, columnspan=2, sticky='we', padx=5) # Create a text label

#Clear loaded image button
exit_button = tk.Button(root, text="Close", height=8, font=("Arial Bold", 12), bg="red",fg="white", command=quit).grid(row=2, column=4, sticky='we', columnspan=2, padx=5) # Create a text label

root.mainloop()
