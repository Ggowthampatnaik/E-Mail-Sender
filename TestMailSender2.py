# E-Mail Sender using SMTPLib and Tkinter

import smtplib
import tkinter as tk
from tkinter import messagebox

def SendEmail():
    try:
        SenderEmailID = SenderMailIdInput.get()
        SenderPassword = SenderPWInput.get()
        ReceiverEmailID = ReceiverMailIdInput.get()
        CCEmailID = CCEmailInput.get()
        Subject = SubjectInput.get()
        MessegeBody = MessegeTextInput.get("1.0", tk.END)
        Mail = f"Subject: {Subject}\n{MessegeBody}"

        Smtp = smtplib.SMTP('smtp.gmail.com', 587)
        Smtp.starttls()

        try:
            Smtp.login(SenderEmailID, SenderPassword)
        except smtplib.SMTPAuthenticationError as Error:
            messagebox.showerror("Error", "Given Credentials are wrong. Please try again.")
            return
        
        try:
            Recipients = [ReceiverEmailID] + CCEmailID.split(",")
            Smtp.sendmail(SenderEmailID, Recipients, Mail)
        except smtplib.SMTPRecipientsRefused as Error:
            messagebox.showerror("Error", "Receiver Mail ID is invalid.")

        Smtp.quit()
        messagebox.showinfo("Success", "Email sent successfully!")

        SubjectInput.delete(0, tk.END)
        MessegeTextInput.delete("1.0", tk.END)

    except Exception as Error:
        messagebox.showerror("Error", "Failed to send email.")

def ExitApp():
    AppWindow.destroy()

def CreateWindow():
    global SenderMailIdInput, SenderPWInput, ReceiverMailIdInput, SubjectInput, MessegeTextInput

    BackgroundColour = '#ace4f3'
    ForegroundColour = '#2e2d2b'
    InputBoxWidth = 40
    PaddingX = 10
    PaddingY = 5
    AppWindow.configure(bg = BackgroundColour)

    tk.Label(AppWindow, text = "Sender Email ID:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 0, column = 0, padx = PaddingX, pady = PaddingY)
    SenderMailIdInput = tk.Entry(AppWindow, width = InputBoxWidth).grid(row = 0, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Password:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 1, column = 0, padx = PaddingX, pady = PaddingY)
    SenderPWInput = tk.Entry(AppWindow, width = InputBoxWidth, show = "*").grid(row = 1, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Receiver Email ID:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 2, column = 0, padx = PaddingX, pady = PaddingY)
    ReceiverMailIdInput = tk.Entry(AppWindow, width = InputBoxWidth).grid(row = 2, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text="CC:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 3, column = 0, padx = PaddingX, pady = PaddingY)
    CCEmailInput = tk.Entry(AppWindow, width = InputBoxWidth).grid(row = 3, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Subject:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 4, column = 0, padx = PaddingX, pady = PaddingY)
    SubjectInput = tk.Entry(AppWindow, width = InputBoxWidth).grid(row = 4, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Message:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 5, column = 0, padx = PaddingX, pady = PaddingY)
    MessegeTextInput = tk.Text(AppWindow, height = PaddingX, width = InputBoxWidth, bg='#fffacd').grid(row = 5, column = 1, padx = 50, pady = PaddingX)

    SendButton = tk.Button(AppWindow, text = "Send Email", command = SendEmail, bg = '#32cd32', fg = 'white')
    SendButton.grid(row = 6, column = 1, padx = PaddingX, pady = PaddingX)

    ExitButton = tk.Button(AppWindow, text = "Exit", command = ExitApp, bg = '#ff4500', fg = 'white')
    ExitButton.grid(row = 7, column = 1, padx = PaddingX, pady = PaddingX)

AppWindow = tk.Tk()
AppWindow.title("GGPMail")

CreateWindow()
AppWindow.mainloop()
