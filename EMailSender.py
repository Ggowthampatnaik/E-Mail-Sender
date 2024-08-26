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
        MessageBody = MessageTextInput.get("1.0", tk.END)
        Mail = f"Subject: {Subject}\n{MessageBody}"

        Smtp = smtplib.SMTP('smtp.gmail.com', 587)
        Smtp.starttls()

        try:
            Smtp.login(SenderEmailID, SenderPassword)
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error", "Invalid Credentials. Please check your email and password.")
            return

        try:
            Recipients = [ReceiverEmailID] + CCEmailID.split(",")
            Smtp.sendmail(SenderEmailID, Recipients, Mail)
        except smtplib.SMTPRecipientsRefused:
            messagebox.showerror("Error", "Invalid Receiver Email ID.")
            return

        Smtp.quit()
        messagebox.showinfo("Success", "Email sent successfully!")

        SubjectInput.delete(0, tk.END)
        MessageTextInput.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

def ExitApp():
    AppWindow.destroy()

def CreateWindow():
    global SenderMailIdInput, SenderPWInput, ReceiverMailIdInput, CCEmailInput, SubjectInput, MessageTextInput

    BackgroundColour = '#ace4f3'
    ForegroundColour = '#2e2d2b'
    InputBoxWidth = 40
    PaddingX = 10
    PaddingY = 5
    AppWindow.configure(bg = BackgroundColour)

    tk.Label(AppWindow, text = "Sender Email ID:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 0, column = 0, padx = PaddingX, pady = PaddingY)
    SenderMailIdInput = tk.Entry(AppWindow, width = InputBoxWidth)
    SenderMailIdInput.grid(row = 0, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Password:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 1, column = 0, padx = PaddingX, pady = PaddingY)
    SenderPWInput = tk.Entry(AppWindow, width = InputBoxWidth, show = "*")
    SenderPWInput.grid(row = 1, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Receiver Email ID:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 2, column = 0, padx = PaddingX, pady = PaddingY)
    ReceiverMailIdInput = tk.Entry(AppWindow, width = InputBoxWidth)
    ReceiverMailIdInput.grid(row = 2, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "CC:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 3, column = 0, padx = PaddingX, pady = PaddingY)
    CCEmailInput = tk.Entry(AppWindow, width = InputBoxWidth)
    CCEmailInput.grid(row = 3, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Subject:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 4, column = 0, padx = PaddingX, pady = PaddingY)
    SubjectInput = tk.Entry(AppWindow, width = InputBoxWidth)
    SubjectInput.grid(row = 4, column = 1, padx = PaddingX, pady = PaddingY)

    tk.Label(AppWindow, text = "Message:", bg = BackgroundColour, fg = ForegroundColour).grid(row = 5, column = 0, padx = PaddingX, pady = PaddingY)
    MessageTextInput = tk.Text(AppWindow, height = 10, width = InputBoxWidth, bg = '#fffacd')
    MessageTextInput.grid(row = 5, column = 1, padx = 50, pady = PaddingX)

    SendButton = tk.Button(AppWindow, text = "Send Email", command = SendEmail, bg = '#32cd32', fg = 'white')
    SendButton.grid(row = 6, column = 1, padx = PaddingX, pady = PaddingX)

    ExitButton = tk.Button(AppWindow, text = "Exit", command = ExitApp, bg = '#ff4500', fg = 'white')
    ExitButton.grid(row = 7, column = 1, padx = PaddingX, pady = PaddingX)

AppWindow = tk.Tk()
AppWindow.title("GGPMail")

CreateWindow()
AppWindow.mainloop()
