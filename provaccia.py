import tkinter as tk


#prepare some data
ButtonPlace  = dict(relx=0.35, rely=0.79, relwidth=0.3, relheight=0.1)
ButtonConfig = dict(bg='#3ab54a', fg='blue', activebackground='#3ab54a', activeforeground='blue')
CanvasConfig = dict(width=600, height=400, highlightthickness=0)


#class names should start with a capital letter
class BackBone(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #you don't need an inner frame so I got rid of it
        
        #init some vars for storing and managing pages
        self.page       = 0
        self.pages      = {}
        self.page_names = []

        #make a refererence of pages and page names
        for C in [StartPage, PageOne]:
            self.pages[C.NAME]=C(self)
            self.page_names.append(C.NAME)
             
        #you can just use one button for every page
        self.btn = tk.Button(self, text="Start Page", command=self.next_page, **ButtonConfig)
        self.btn.place(**ButtonPlace)
        
        #init start page  
        self.btn.invoke()

    def next_page(self):
        #whatever page is packed ~ forget it
        for n, f in self.pages.items():
            f.pack_forget()
        
        #get page name
        name = self.page_names[self.page]
        #pack page associated with name
        self.pages[name].pack()
        #change button text to the name of this page (same as you had it)
        self.btn['text'] = name
        #raise the button up in z-order
        self.btn.tkraise()
        #prime next page number
        self.page = (self.page + 1) % len(self.page_names)
    

class StartPage(tk.Canvas):
    #static page name reference
    NAME = 'Start Page'
    #the proper term is master ~ not parent. controller is no more
    def __init__(self, master): 
        tk.Canvas.__init__(self, master, bg='#aaaaff', **CanvasConfig)
        #you don't need a frame. make the whole thing a canvas
    
    
#apply StartPage comments to this page, as well
class PageOne(tk.Canvas):
    NAME = 'Page One'
    def __init__(self, master):
        tk.Canvas.__init__(self, master, bg='#ffaaaa', **CanvasConfig)
            

#this is the proper way to initialize your app            
if __name__ == '__main__':
    app = BackBone()
    app.configure(bg='beige', highlightthickness=0, bd=0)
    app.resizable(False, False)
    app.mainloop()   