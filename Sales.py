#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class SalesDataApp:
    def __init__(self, master):
        self.master = master  #assigning 
        self.master.title("Sales Data Calculator")  #title of the application 
        
        # Set fixed size for the window
        self.master.geometry("400x300")  # Width x Height
        self.master.resizable(False, False)  # Disable resizing

        self.welcome_label = tk.Label(master, text="Welcome to Sales Calculator\nClick 'Start' to begin") #producing welcoming message 
        self.welcome_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_calculator)  #allows you start the app and move onto the next step
        self.start_button.pack(pady=10)

    def start_calculator(self):
        
        # Remove welcome message and start the sales data input
        self.welcome_label.destroy()
        self.start_button.destroy()

        #this is where the label for days input will be created 
        self.days_label = tk.Label(self.master, text="Enter number of days of sales data to input:")
        self.days_label.pack()

        #this allows you to create a text entry widget where number of days of sales data can be inputted 
        self.days_entry = tk.Entry(self.master)
        self.days_entry.pack()

        self.sales_entries = []  #initializes an empty list which later will be used to store number of days

        #command parameter will call self.submit_days when the submit button is clicked. It will read the number of days and proceed to sales entry
        self.submit_button = tk.Button(self.master, text="Submit Days", command=self.submit_days)
        self.submit_button.pack(pady=10)

        #this function will be executed when the reset button is clicked. It will clear the whole application and bring you back to the start page. 
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_app)
        self.reset_button.pack(pady=5)

    def reset_app(self):
        for widget in self.master.winfo_children(): #retriiving a list of all child widgets and the loop iterates over each widget in the list
            widget.destroy()  #this method call removes the widget from the GUI ad frees up the resources associated with it

        #after destorying the widgets, this label is displayed welcoming the user back to the main page.
        self.welcome_label = tk.Label(self.master, text="Welcome to Sales Calculator\nClick 'Start' to begin")
        self.welcome_label.pack(pady=20)

        #this parameter assigns the method to be called when the start button is clicked. The button handles the logic for starting sales calculator
        self.start_button = tk.Button(self.master, text="Start", command=self.start_calculator)
        self.start_button.pack(pady=10)  #adding a padding of 10 pixel

    def submit_days(self):  #defines a method called submit_days which is part of a class and the self refers to the current instance of the class
        try:
            self.days = int(self.days_entry.get()) #retrieving the text input from the days_entry widget
            if self.days <= 0:  #checking if the numbers of days is less than or equal to 0 and
                raise ValueError("Number of days should be positive.")  #if so raise the valueError.
            self.create_sales_entries()  #method is handling the logic of generating the necessary input fields for the user to enter sales data for specified number of days
        except ValueError as e: #executed if a ValueError is raised in the try block
            messagebox.showerror("Input Error", f"Invalid input: {e}") #displays an error message dialog. its formatted to include the error description where e contains the error messgae

    def create_sales_entries(self):  #defining the create_sales_entries method which is part of a class
        for widget in self.master.winfo_children(): #loop iterates over all child widgets currently in the main window and destroys them
            widget.destroy()
        
        # Recreate the days entry section
        self.days_label = tk.Label(self.master, text="Enter number of days of sales data to input:")
        self.days_label.pack()

        self.days_entry = tk.Entry(self.master)
        self.days_entry.pack()

        self.sales_entries = [] #initializes an empty list to hold the entry fields for each day's sales data 
        for day in range(1, self.days + 1):  #loop iterates from 1 to number of days specified by the user. 
            label = tk.Label(self.master, text=f"Enter sales for Day #{day}:")  #for each day specified the label and entry widget are created
            label.pack()

            entry = tk.Entry(self.master)
            entry.pack()
            self.sales_entries.append(entry) #entry field is appended to the self.sales_entries list, allowing for an easy access later. 

        submit_sales_button = tk.Button(self.master, text="Calculate Summary", command=self.calculate_summary) #this button will trigger the calculate_summary. This method will handle the logic for summarizing the sales data
        submit_sales_button.pack(pady=10)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_app) #allowing users to clear the sales data entries and return to the welcome page of the app. reset_app method will destory all widgets
        self.reset_button.pack(pady=5)

    def calculate_summary(self):
        try:
            sales = [float(entry.get()) for entry in self.sales_entries] #uses list comprehension to iterate over each entry in self.sales_entries
            total_sales = sum(sales)  #computes the total of all sale entries 
            average_sales = total_sales / len(sales) if sales else 0  #calculates the average of all the sale entries and if the sales is empty the automatic output is 0.
            
            # Displays the results in a message box
            result_text = f"Total Sales: {total_sales:.2f}\nAverage Sales: {average_sales:.2f}"
            messagebox.showinfo("Sales Summary", result_text)
        except ValueError:  #occurs during the conversion of entries to floats. 
            messagebox.showerror("Input Error", "Please ensure all sales entries are numeric.")

if __name__ == "__main__":  #checks wheter the script is being run as the main program and if it is, the following code block will be executed.
    root = tk.Tk() #creates an instance of the main application window
    app = SalesDataApp(root) #creates an instance of SalesDataApp class passing the root window as the master widget
    root.mainloop()



# In[ ]:




