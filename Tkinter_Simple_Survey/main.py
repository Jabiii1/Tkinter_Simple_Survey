from tkinter import *
from tkinter import ttk



userinput = {}
def mainWindow():
    mainWindow = Tk()
    mainWindow.title("Personal Information")
    mainWindow.configure(bg="lightblue")
    def center_window(mainwindow, width, height):
        
        screen_width = mainwindow.winfo_screenwidth()
        screen_height = mainwindow.winfo_screenheight()

        
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        
        
        mainwindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 350
    window_height = 500

    center_window(mainWindow, window_width, window_height)
    mainWindow.resizable(FALSE,FALSE)

    Label(mainWindow, text="PERSONAL INFORMATION\n", font="Arial",justify="center", bg="lightblue").place(x=80, y=10, )

    # Icon 
    icon = PhotoImage(file= "Media_Files\\info.png")    
    mainWindow.iconphoto(False, icon) 
    
    # function
    def Inclick():
        if Button(Submit):
            
            # Personal Info
            userinput['First_Name'] = Fname.get()
            userinput['Middle_Name'] = Mname.get()
            userinput['Last_Name'] = Lname.get()
            userinput['Age'] = age.get()
            userinput['Gender'] = gender.get()
            userinput['Course'] = course.get()
            
            # Birthdate
            userinput['Month'] = month.get()
            userinput['Day'] = day.get()
            userinput['Year'] = year.get()
            
            # Address
            userinput['Island'] = IslandCbox.get()
            userinput['Region'] = RegionCbox.get()
            userinput['Province'] = ProvinceCbox.get()
            userinput['City'] = CityCbox.get()
            
            # Family Background
            userinput['Mother_Name'] = mother.get()
            userinput['Mother_Age'] = M_Age.get()
            userinput['Mother_Occupation'] = motherO.get()
            
            userinput['Father_Name'] = father.get()
            userinput['Father_Age'] = F_Age.get()
            userinput['Father_Occupation'] = fatherO.get()
            mainWindow.destroy()
            warningWindow()
        else:
            pass    
        


    # Personal Info
    Label(mainWindow, text='First Name:', bg="lightblue").place(x=8, y=43)
    Fname = Entry(mainWindow, width=20 ,justify="center")
    Fname.place(x=80, y=43)

    Label(mainWindow, text='Middle Name:', bg="lightblue").place(x=1, y=63)
    Mname = Entry(mainWindow, width=20  ,justify="center")
    Mname.place(x=80, y=63)

    Label(mainWindow, text='Last Name:', bg="lightblue").place(x=8, y=83)
    Lname = Entry(mainWindow, width=20  ,justify="center")
    Lname.place(x=80, y=83)


    Label(mainWindow, text="Age:", bg="lightblue").place(x=220, y=43)
    age = Entry(mainWindow, width=10, justify="center")
    age.place(x=270, y=43)


    # Combobox 
    Label(mainWindow, text="Gender:", bg="lightblue").place(x=220, y=63)
    gender = ttk.Combobox(mainWindow, values=["Male", "Female","Other"] , width=7, state="readonly" ,justify="center")
    gender.place(x=270, y=63)

    Label(mainWindow, text="Course:", bg="lightblue").place(x=220, y=83)
    course = ttk.Combobox(mainWindow, values=["BSIT", "ABELS","BSSW", "BSA", "BTVTEd" ,"BSE","DHRS", "BSAIS", "BSPA"] , width=7, state="readonly" ,justify="center")
    course.place(x=270, y=83)
    
    
    # Birthdate
    months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"]
    
    days = {
        "January" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31"],
        
        "February" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28"],
        
        "March" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30"],
        
        "April" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31"],
        
        "May" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30",
                "31"],
        
        "June" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30"],
        
        "July" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30",
                "31"],
        
        "August" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30",
                "31"],
        
        "September" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30"],
        
        "October" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31"],
        
        "November" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30"],
        
        "December" : ["1","2","3","4", "5", "6", "7", "8", "9", "10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30",
                    "31"]
    }

    Label(mainWindow, text="BIRTHDATE",font="Arial", bg="lightblue").place(x=136, y=114)
    
    Label(mainWindow, text="Birthmonth:", bg="lightblue").place(x=5, y=153)
    month =ttk.Combobox(mainWindow, width=13, values=months, justify="center", state="readonly")
    month.place(x=75, y=153)
    month.set("Select Month")
    
    Label(mainWindow, text="Birthday:", bg="lightblue").place(x=180, y=153)
    day =ttk.Combobox(mainWindow, width=13, values=months, justify="center", state="readonly")
    day.place(x=236, y=153)
    day.set("Select Day")
    
    Label(mainWindow, text="Birthyear:", bg="lightblue").place(x=110, y=183)
    year = ttk.Combobox(mainWindow, values=["1995", "1996","1997", "1998", "1999" ,"2001","2002", "2003", "2004", "2005","2006"] , width=11, state="readonly" ,justify="center")
    year.place(x=165, y=183)
    year.set("Select Year")
    
    def Month_Update(event):
        selectedMonth = month.get()
        if selectedMonth in days:
            day["values"] = days[selectedMonth]

    # Bind_Updates(Birthdate)
    month.bind("<<ComboboxSelected>>", Month_Update)

    
    
    # Address
    Label(mainWindow, text="ADDRESS",font="Arial", bg="lightblue").place(x=140, y=218)

    island = ["Luzon","Visayas","Mindanao"]

    region = {
        "Luzon": ["Region-I", "Region-II", "Region-III", "Region-IV-A", "Region-V", "NCR", "CAR", "MIMAROPA"],
        
        "Visayas": ["Western Visayas-VI", "Central Visayas-VII", "Eastern Visayas-VIII"],
        
        "Mindanao": ["Region-IX", "Region-X", "Region-XI", "Region-XII", "BARMM", "Region-XIII"]
        
    }

    provinces = {
            # Luzon
            "Region-I": ["Ilocos Norte", "Ilocos Sur", "La Union", "Pangasinan"],
            
            "Region-II":["Batanes", "Cagayan", "Isabela", "Nueva Vizcaya", "Quirino"],
            
            "Region-III":["Aurora", "Bataan", "Bulacan", "Nueva Ecija", "Pampanga", "Tarlac", "Zambales"],
            
            "Region-IV-A":["Batangas", "Cavite", "Laguna", "Quezon", "Rizal"],
                
            "Region-V":["Albay", "Camarines Norte", "Camarines Sur", "Catanduanes", "Masbate", "Sorsogon"],
            
            "NCR":["Metro Manila"],
            
            "CAR":["Abra", "Apayao", "Benguet", "Ifugao", "Kalinga", "Mountain Province"],
            
            "MIMAROPA":["Marinduque", "Occidental Mindoro", "Oriental Mindoro", "Palawan", "Romblon"],
            
            # Visayas
            "Western Visayas-VI":["Aklan", "Antique", "Capiz", "Guimaras", "Iloilo","Negros Oriental"],
            
            "Central Visayas-VII":["Bohol", "Cebu", "Negros Oriental", "Siquijor"],
                
            "Eastern Visayas-VIII":["Biliran", "Eastern Samar", "Leyte", "Northern Samar", "Samar", "Southern Leyte"],
            
            # "Mindanao"
            "Region-IX": ["Zamboanga del Norte", "Zamboanga del Sur", "Zamboanga Sibugay"],
            
            "Region-X":["Bukidnon", "Camiguin", "Lanao del Norte", "Misamis Occidental", "Misamis Oriental"],
            
            "Region-XI":["Davao de Oro", "Davao del Norte", "Davao del Sur", "Davao Occidental", "Davao Oriental"],
            
            "Region-XII":["Cotabato", "Sarangani", "South Cotabato", "Sultan Kudarat"],

            "BARMM":["Basilan", "Lanao del Sur", "Maguindanao del Norte", "Maguindanao del Sur", "Sulu", "Tawi-Tawi"],
            
            "Region-XIII":[ "Agusan del Norte", "Agusan del Sur", "Dinagat Islands", "Surigao del Norte", "Surigao del Sur",]
        }

    cities = {
            "Ilocos Norte": ["Laoag", "Batac"],
            
            "Ilocos Sur": ["Vigan", "Candon", "Tagudin"],
            
            "La Union": ["San Fernando", "Bauang", "Agoo", "Naguilian"],
            
            "Pangasinan": ["Dagupan", "San Carlos", "Urdaneta", "Alaminos", "Lingayen", "Calasiao"],
            
            "Batanes": ["Basco", "Itbayat"],
            
            "Cagayan": ["Tuguegarao", "Aparri", "Ballesteros", "Claveria"],
            
            "Isabela": ["Cauayan", "Ilagan", "Santiago", "Roxas", "San Mateo"],
            
            "Nueva Vizcaya": ["Bayombong", "Solano", "Bagabag"],
            
            "Quirino": ["Cabarroguis", "Diffun", "Maddela"],
            
            "Aurora": ["Baler", "Maria Aurora", "Dipaculao"],
            
            "Bataan": ["Balanga", "Dinalupihan", "Orion", "Mariveles"],
            
            "Bulacan": ["Malolos", "Meycauayan", "San Jose del Monte", "Bocaue", "Marilao", "Santa Maria"],
            
            "Nueva Ecija": ["Cabanatuan", "Gapan", "Palayan", "San Jose", "Talavera", "Science City of Muñoz"],
            
            "Pampanga": ["Angeles", "San Fernando", "Mabalacat", "Apalit"],
            
            "Tarlac": ["Tarlac City", "Concepcion", "Capas"],
            
            "Zambales": ["Olongapo", "Iba", "Subic", "Botolan"],
            
            "Batangas": ["Batangas City", "Lipa", "Tanauan", "San Juan", "Nasugbu"],
            
            "Cavite": ["Tagaytay", "Trece Martires", "Dasmariñas", "Imus", "Bacoor", "General Trias"],
            
            "Laguna": ["San Pablo", "Calamba", "Santa Rosa", "Biñan", "Cabuyao", "Los Baños"],
            
            "Quezon": ["Lucena", "Tayabas", "Sariaya", "Candelaria"],
            
            "Rizal": ["Antipolo", "Cainta", "Binangonan", "Taytay"],
            
            "Marinduque": ["Boac", "Santa Cruz", "Mogpog"],
            
            "Occidental Mindoro": ["Mamburao", "San Jose", "Sablayan"],
            
            "Oriental Mindoro": ["Calapan", "Pinamalayan", "Naujan"],
            
            "Palawan": ["Puerto Princesa", "Coron", "El Nido", "Roxas"],
            
            "Romblon": ["Romblon", "Odiongan", "San Fernando"],
            
            "Abra": ["Bangued", "Tineg"],
            
            "Apayao": ["Kabugao", "Conner", "Luna"],
            
            "Benguet": ["Baguio", "La Trinidad", "Itogon"],
            
            "Ifugao": ["Lagawe", "Kiangan", "Banaue"],
            
            "Kalinga": ["Tabuk", "Tinglayan"],
            
            "Mountain Province": ["Bontoc", "Sagada", "Bauko"],
            
            "Albay": ["Legazpi", "Tabaco", "Ligao", "Daraga"],
            
            "Camarines Norte": ["Daet", "Jose Panganiban", "Basud"],
            
            "Camarines Sur": ["Naga", "Iriga", "Pili", "Caramoan"],
            
            "Catanduanes": ["Virac", "San Andres"],
            
            "Masbate": ["Masbate City", "Aroroy", "Ticao"],
            
            "Sorsogon": ["Sorsogon City", "Bulusan", "Gubat"],
            
            "Aklan": ["Kalibo", "Malay", "Numancia"],
            
            "Antique": ["San Jose de Buenavista", "Sibalom", "Culasi"],
            
            "Capiz": ["Roxas City", "Pilar", "Panay"],
            
            "Guimaras": ["Jordan", "Buenavista", "Nueva Valencia"],
            
            "Iloilo": ["Iloilo City", "Passi", "Pototan", "Jaro"],
            
            "Bohol": ["Tagbilaran", "Ubay", "Talibon"],
            
            "Cebu": ["Cebu City", "Lapu-Lapu", "Mandaue", "Carcar", "Danao"],
            
            "Negros Oriental": ["Dumaguete", "Bais", "Tanjay", "Bayawan"],
            
            "Siquijor": ["Siquijor", "Larena", "Lazi"],
            
            "Biliran": ["Naval", "Kawayan", "Biliran"],
            
            "Eastern Samar": ["Borongan", "Guiuan", "Oras"],
            
            "Leyte": ["Tacloban", "Ormoc", "Baybay", "Palo"],
            
            "Northern Samar": ["Catarman", "Allen", "Bobon"],
            
            "Samar": ["Catbalogan", "Calbayog", "Gandara"],
            
            "Southern Leyte": ["Maasin", "Sogod", "Hinunangan"],
        
            "Zamboanga del Norte": ["Dipolog", "Dapitan", "Polanco"],
            
            "Zamboanga del Sur": ["Pagadian", "Molave", "Labangan"],
            
            "Zamboanga Sibugay": ["Ipil", "Kabasalan", "Diplahan"],
            
            "Bukidnon": ["Malaybalay", "Valencia", "Maramag", "Manolo Fortich"],
            
            "Camiguin": ["Mambajao", "Catarman"],
            
            "Lanao del Norte": ["Iligan", "Kauswagan", "Tubod"],
            
            "Misamis Occidental": ["Oroquieta", "Ozamis", "Tangub"],
            
            "Misamis Oriental": ["Cagayan de Oro", "Gingoog", "Tagoloan"],
            
            "Davao de Oro": ["Nabunturan", "Monkayo", "Compostela"],
            
            "Davao del Norte": ["Tagum", "Panabo", "Samal"],
            
            "Davao del Sur": ["Davao City", "Digos", "Santa Cruz"],
            
            "Davao Occidental": ["Malita", "Jose Abad Santos"],
            
            "Davao Oriental": ["Mati", "Baganga", "Cateel"],
            
            "Cotabato": ["Kidapawan", "M'lang", "Kabacan"],
            
            "Sarangani": ["Alabel", "Glan", "Malapatan"],
            
            "South Cotabato": ["Koronadal", "General Santos", "Tupi"],
            
            "Sultan Kudarat": ["Isulan", "Tacurong", "Lutayan"],
            
            "Agusan del Norte": ["Butuan", "Cabadbaran", "Nasipit"],
            
            "Agusan del Sur": ["Bayugan", "Prosperidad", "San Francisco"],
            
            "Dinagat Islands": ["San Jose", "Loreto"],
            
            "Surigao del Norte": ["Surigao City", "Siargao", "Claver"],
            
            "Surigao del Sur": ["Tandag", "Bislig", "Lianga"],
            
            "Basilan": ["Isabela City", "Lamitan"],
            
            "Lanao del Sur": ["Marawi", "Balindong", "Malabang"],
            
            "Maguindanao del Norte": ["Datu Odin Sinsuat", "Barira"],
            
            "Maguindanao del Sur": ["Buluan", "Pagalungan"],
            
            "Sulu": ["Jolo", "Patikul", "Parang"],
            
            "Tawi-Tawi": ["Bongao", "Sitangkai", "Panglima Sugala"]
        }

    # Island
    Label(mainWindow, text="Island:",bg="lightblue").place(x=8, y=253)
    IslandCbox = ttk.Combobox(mainWindow, width=15 ,values=island,justify="center", state="readonly")
    IslandCbox.place(x=63, y=253)          
    IslandCbox.set("Select Island")        

    # Region
    Label(mainWindow, text="Region:",bg="lightblue").place(x=180, y=253)
    RegionCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
    RegionCbox.place(x=225, y=253)  
    RegionCbox.set("Select Region") 

    # Province
    Label(mainWindow, text="Province:",bg="lightblue").place(x=8, y=280)
    ProvinceCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
    ProvinceCbox.place(x=63, y=280)        
    ProvinceCbox.set("Select Province")

    # City
    Label(mainWindow, text="City:",bg="lightblue").place(x=180, y=280)
    CityCbox = ttk.Combobox(mainWindow, width=15 ,justify="center", state="readonly")
    CityCbox.place(x=225, y=280) 
    CityCbox.set("Select City")

    # Bindings
    def Island_Update(event):
        selectedIsland = IslandCbox.get()
        if selectedIsland in region:
            RegionCbox["values"] = region[selectedIsland]
            

    def Region_Update(event):
        selectedRegion = RegionCbox.get()  
        if selectedRegion in provinces:
            ProvinceCbox["values"] = provinces[selectedRegion] 
            
    def Province_Update(event):
        selectedProvince = ProvinceCbox.get()  
        if selectedProvince in cities:
            CityCbox["values"] = cities[selectedProvince]  

    # Bind_Updates (ADDRESS)
    IslandCbox.bind("<<ComboboxSelected>>", Island_Update)
    RegionCbox.bind("<<ComboboxSelected>>", Region_Update)
    ProvinceCbox.bind("<<ComboboxSelected>>", Province_Update)

    # FAMILY BACKGROUND
    Label(mainWindow, text="FAMILY BACKGROUND\n", font="Arial",justify="center", bg="lightblue").place(x=90, y=315)

    # Mother's Name
    Label(mainWindow, text="Mother's Full Name:", bg="lightblue").place(x=5, y=350)
    mother = Entry(mainWindow, width=20 ,justify="center")
    mother.place(x=117, y=350)
    
    # Mother's Age
    Label(mainWindow, text="Age:", bg="lightblue").place(x=240, y=350)
    M_Age = ttk.Combobox(mainWindow, values=["30+", "40+","50+", "60+","70+", "80+", "90+"] , width=7, state="readonly" ,justify="center")
    M_Age.place(x=272, y=350)
    
    # Mother's Occupation
    Label(mainWindow, text="Mother's Occupation:", bg="lightblue").place(x=5, y=372)
    motherO = Entry(mainWindow, width=15 ,justify="center")
    motherO.place(x=130, y=373)


    # Father's Name
    Label(mainWindow, text="Father's Full Name:", bg="lightblue").place(x=5, y=405)
    father = Entry(mainWindow, width=20 ,justify="center")
    father.place(x=117, y=405   )
    
    # Father's Age
    Label(mainWindow, text="Age:", bg="lightblue").place(x=240, y=405)
    F_Age = ttk.Combobox(mainWindow, values=["30+", "40+","50+", "60+","70+", "80+", "90+"] , width=7, state="readonly" ,justify="center")
    F_Age.place(x=272, y=405)
    
    # Father's Occupation
    Label(mainWindow, text="Father's Occupation:", bg="lightblue").place(x=5, y=428)
    fatherO = Entry(mainWindow, width=15 ,justify="center")
    fatherO.place(x=130, y=428)
    
    # Done Button
    Submit = Button(mainWindow, width= 10, text="Submit", relief="groove",activebackground="deepskyblue", command=Inclick).place(x=143, y=465)
    
    mainWindow.mainloop()

def warningWindow():

        
        tryWindow = Tk()
        tryWindow.title("Warning!")
        tryWindow.configure(bg="lightblue")

        def center_window(tryWindow, width, height):
            
            screen_width = tryWindow.winfo_screenwidth()
            screen_height = tryWindow.winfo_screenheight()

            
            position_top = int(screen_height / 2 - height / 2)
            position_left = int(screen_width / 2 - width / 2)
            
            
            tryWindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

        window_width = 350
        window_height = 180

        center_window(tryWindow, window_width, window_height)

        tryWindow.lift()
        # icon 
        icon = PhotoImage(file= "Media_Files\\warning.png")    
        tryWindow.iconphoto(False, icon) 

        # Text
        Label(tryWindow, text="This loading might take for a while.",font=("Arial",13),bg="lightblue").place(x=30, y=40)
        Label(tryWindow, text="Are you sure do you want to continue?",font=("Arial",10),bg="lightblue").place(x=50, y=70)

        
        def ifYes():
            if Button(yes):
                tryWindow.destroy()
                loadingWindow()
            else:
                pass
        def ifNo():        
            if Button(no):
                tryWindow.destroy()
            else:
                pass
                    

        #Button (Yes/No)  
        yes = Button(tryWindow, text="Yes", width=5,height=1,relief="groove",activebackground="green", command=ifYes).place(x=200,y=120)
        no = Button(tryWindow, text="No", width=5,height=1,relief="groove",activebackground="red", command=ifNo).place(x=250,y=120)

        
        tryWindow.mainloop()

def loadingWindow():
    loadWindow = Tk()
    loadWindow.title("Loading")
    loadWindow.configure(bg="lightblue")
    def center_window(window, width, height):

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()


        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        

        window.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 350
    window_height = 180

    center_window(loadWindow, window_width, window_height)
    
    icon = PhotoImage(file= "Media_Files\\loading.png")    
    loadWindow.iconphoto(False, icon) 
    
    def clicked():
        loadWindow.destroy()
        infoClicked()
        
    
    def change_1():
        infos.config(text="Analyzing Complete!", font="Arial, 15", bg="lightblue")
        infos.place_configure(x=80, y=60)
        chkInfo = Button(loadWindow, text="Check Info",width=10,height=1,relief="groove",activebackground="green" ,command=clicked).place_configure(x=140, y=100)
        
        
    
    def change_2():
        infos.config(text="Checking Family Status...")
        
        loadWindow.after(1878, change_1)
    
    def change_3():
        infos.config(text="Scanning your Address...")
        
        loadWindow.after(1000, change_2)
    
    def change_4():
        infos.config(text="Checking Typos...")
        
        loadWindow.after(1000, change_3)
    
    def change_5():
        infos.config(text="Scanning Errors...")
        
        loadWindow.after(1000, change_4)
    # Texts
    wait = Label(loadWindow, text="\n\nPlease wait a while.", bg="lightblue")
    wait.pack(padx=0, pady=1)
    wait.after(5878, wait.destroy)
    
    infos = Label(loadWindow, text="Analyzing your Personal Details...", bg="lightblue")
    infos.pack(padx=0, pady=2)

    def stopLoad():
        loading.stop()   
        loading.pack_forget() 


    loading = ttk.Progressbar(loadWindow, orient=HORIZONTAL, length=200, mode="determinate")
    loading.pack(pady=3)
    loading.start()
    loadWindow.after(1000, change_5)
    
    loadWindow.after(5878,stopLoad) 

    loadWindow.lift()
    loadWindow.mainloop()

def infoClicked():
    lastwindow = Tk()
    lastwindow.title("Checking Information")
    lastwindow.configure(bg="lightblue")
    def center_window(lastwindow, width, height):
        
        screen_width = lastwindow.winfo_screenwidth()
        screen_height = lastwindow.winfo_screenheight()

        
        position_top = int(screen_height / 2 - height / 2)
        position_left = int(screen_width / 2 - width / 2)
        
        
        lastwindow.geometry(f'{width}x{height}+{position_left}+{position_top}')

    window_width = 360
    window_height = 500

    center_window(lastwindow, window_width, window_height)
    lastwindow.resizable(FALSE,FALSE)
    
    def Close():
        lastwindow.destroy()
    
    icon = PhotoImage(file= "Media_Files\\Last_icon.png")    
    lastwindow.iconphoto(False, icon) 
    
    
    
    text = Label(lastwindow, text="Checking User Input",font=("Arial", 12), bg="lightblue").place(x=100, y=40)
    
    line1 = Label(lastwindow, text="--------------------------------------------------------------------------------------------------------------------------------", bg="lightblue").place(x=1,y=17)
    
    # Personal Info
    Label(lastwindow, text="PERSONAL INFORMATION: ",bg="lightblue").place(x=8,y=65)
    Label(lastwindow, text=f"First Name: {userinput['First_Name']}", bg="lightblue").place(x=8, y=85)
    Label(lastwindow, text=f"Middle Name: {userinput['Middle_Name']}", bg="lightblue").place(x=8, y=105)
    Label(lastwindow, text=f"Last Name: {userinput['Last_Name']}", bg="lightblue").place(x=8, y=125)
    Label(lastwindow, text=f"Age: {userinput['Age']}", bg="lightblue").place(x=200, y=85)
    Label(lastwindow, text=f"Gender: {userinput['Gender']}", bg="lightblue").place(x=200, y=105)
    Label(lastwindow, text=f"Course: {userinput['Course']}", bg="lightblue").place(x=200, y=125)
    
    # Birth Month
    Label(lastwindow,text="BIRTHDATE & ADDRESS: ",bg="lightblue").place(x=8,y=185)
    Label(lastwindow, text=f"BirthMonth: {userinput['Month']}", bg="lightblue").place(x=8, y=205)
    Label(lastwindow, text=f"Birthday: {userinput['Day']}", bg="lightblue").place(x=8, y=225)
    Label(lastwindow, text=f"BirthYear: {userinput['Year']}", bg="lightblue").place(x=8, y=245)
    
    # Address
    Label(lastwindow, text=f"Island: {userinput['Island']}", bg="lightblue").place(x=200, y=205)
    Label(lastwindow, text=f"Region: {userinput['Region']}", bg="lightblue").place(x=200, y=225)
    Label(lastwindow, text=f"Province: {userinput['Province']}", bg="lightblue").place(x=200, y=245)
    Label(lastwindow, text=f"City: {userinput['City']}", bg="lightblue").place(x=200, y=265)
    
    # Family Background
    Label(lastwindow, text="FAMILY BACKGROUND: ", bg="lightblue").place(x=8, y=305)
    Label(lastwindow, text=f"Mother's Name: {userinput['Mother_Name']}", bg="lightblue").place(x=8, y=325)
    Label(lastwindow, text=f"Mother's Age: {userinput['Mother_Age']}", bg="lightblue").place(x=8, y=345)
    Label(lastwindow, text=f"Mother's Occupation: {userinput['Mother_Occupation']}", bg="lightblue").place(x=8, y=365)
    Label(lastwindow, text=f"Father's Name: {userinput['Father_Name']}", bg="lightblue").place(x=200, y=325)
    Label(lastwindow, text=f"Father's Age: {userinput['Father_Age']}", bg="lightblue").place(x=200, y=345)
    Label(lastwindow, text=f"Father's Occupation: {userinput['Father_Occupation']}", bg="lightblue").place(x=200, y=365)
    
    lineEnd = Label(lastwindow, text="--------------------------------------------------------------------------------------------------------------------------------", bg="lightblue").place(x=1,y=458)
    
    Button(lastwindow, text="Done",width=7,height=1, relief="groove",activebackground="deepskyblue", command=Close).place(x=150, y=430)
    lastwindow.lift()
mainWindow()