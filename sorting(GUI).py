from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
class Sorting_App:
    def __init__(self,root):
        self.root=root
        blank_space=" "
        self.root.title(170*blank_space+"File Sorting Application")
        self.root.geometry("1366x760+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="folder.png")
        title=Label(self.root,text="File Sorting Application", image=self.logo_icon,compound=LEFT, font=("Bahnschrift",40,"bold"), bg="#032738", fg="#a8a032", anchor="w").place(x=0, y=0, relwidth=1)


        #---------Section1-------------------------
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder: ", font=("times new roman",16,"bold"), bg="white").place(x=5, y=80)
        
        txt_folder_name=Entry(self.root,textvariable=self.var_foldername, font=("times new roman",15,"bold"),state='readonly', bg="lightyellow").place(x=155,y=80, height=30, width=500)

        btn_browse_button=Button(self.root,command=self.browse_function,text="BROWSE",bd=2,relief=RAISED, font=("times new roman",15,"bold"), bg="#262626", fg="white",cursor="hand2", activebackground="#262626", activeforeground="white").place(x=665,y=80, height=30)

        hr=Label(self.root,bg="lightgray").place(x=35, y=130,height=1,width=1200)


        #-------------Section2----------------
        self.image_extensoins=["Image Extensions",".png",".jpg"]
        self.audio_extensoins=["Audio Extensions",".amr",".mp3"]
        self.video_extensoins=["Video Extensions",".mp4",".avi",".mkv",".3gp"]
        self.doc_extensoins=["Document Extensions",".docx",".xlxs",".pptx",".ppt",".pdf",".zip",".rar",".txt"]

        self.folders={
                "image" : self.image_extensoins,
                "audio" : self.audio_extensoins,
                "video" : self.video_extensoins,
                "document" : self.doc_extensoins
            }

        lbl_support_ext=Label(self.root,text="Supported Extensions: ", font=("times new roman",16,"bold"), bg="white").place(x=5, y=160)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensoins, font=("times new roman",16,"bold"),state="readonly",justify=CENTER)
        self.image_box.place(x=50,y=200,height=30,width=250)
        self.image_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensoins, font=("times new roman",16,"bold"),state="readonly",justify=CENTER)
        self.audio_box.place(x=350,y=200,height=30,width=250)
        self.audio_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensoins, font=("times new roman",16,"bold"),state="readonly",justify=CENTER)
        self.video_box.place(x=650,y=200,height=30,width=250)
        self.video_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensoins, font=("times new roman",16,"bold"),state="readonly",justify=CENTER)
        self.doc_box.place(x=950,y=200,height=30,width=250)
        self.doc_box.current(0)


        #-----------Section3------------------
        self.image_icon=PhotoImage(file="image.png")
        self.audio_icon=PhotoImage(file="audio.png")
        self.video_icon=PhotoImage(file="video.png")
        self.doc_icon=PhotoImage(file="document.png")
        self.other_icon=PhotoImage(file="other.png")

        frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        frame1.place(x=50,y=270,height=320,width=1150)
        self.lbl_total_files=Label(frame1,text="Total Files:  ", font=("times new roman",16,"bold"), bg="white")
        self.lbl_total_files.place(x=10,y=10)
        
        self.lbl_total_image=Label(frame1,text="Total Images\n0",image=self.image_icon,compound=TOP,font=("times new roman",15,"bold"),bg="#032738",fg="white")
        self.lbl_total_image.place(x=30,y=50,width=200,height=250)

        self.lbl_total_audio=Label(frame1,text="Total Audios\n0",image=self.audio_icon,compound=TOP,font=("times new roman",15,"bold"),bg="#032738",fg="white")
        self.lbl_total_audio.place(x=250,y=50,width=200,height=250)

        self.lbl_total_video=Label(frame1,text="Total Videos\n0",image=self.video_icon,compound=TOP,font=("times new roman",15,"bold"),bg="#032738",fg="white")
        self.lbl_total_video.place(x=470,y=50,width=200,height=250)

        self.lbl_total_doc=Label(frame1,text="Total Documents\n0",image=self.doc_icon,compound=TOP,font=("times new roman",15,"bold"),bg="#032738",fg="white")
        self.lbl_total_doc.place(x=690,y=50,width=200,height=250)

        self.lbl_total_other=Label(frame1,text="Other Files\n0",image=self.other_icon,compound=TOP,font=("times new roman",15,"bold"),bg="#032738",fg="white")
        self.lbl_total_other.place(x=910,y=50,width=200,height=250)

        #------------------Section4------------
        lbl_status=Label(self.root,text="Status: ", font=("times new roman",16,"bold"), bg="white")
        lbl_status.place(x=50,y=600)

        self.lbl_status_t=Label(self.root,text="", font=("times new roman",16,"bold"), bg="white", fg="blue")
        self.lbl_status_t.place(x=300,y=600)

        self.lbl_status_m=Label(self.root,text="", font=("times new roman",16,"bold"), bg="white", fg="green")
        self.lbl_status_m.place(x=440,y=600)

        self.lbl_status_l=Label(self.root,text="", font=("times new roman",16,"bold"), bg="white", fg="orange")
        self.lbl_status_l.place(x=590,y=600)


        #----------------Section4 (Buttons) ------------------

        self.btn_clear_button=Button(self.root,command=self.clear,text="CLEAR",bd=2,relief=RAISED, font=("times new roman",15,"bold"), bg="#607d8b", fg="white",cursor="hand2", activebackground="#607d8b", activeforeground="white")
        self.btn_clear_button.place(x=990,y=600,height=30)

        self.btn_start_button=Button(self.root,state=DISABLED,command=self.start_fuction,text="START",bd=2,relief=RAISED, font=("times new roman",15,"bold"), bg="#ff5722", fg="white",cursor="hand2", activebackground="#ff5722", activeforeground="white")
        self.btn_start_button.place(x=1100,y=600,height=30)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        combine_list=[]

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i)) == True:
                self.count+=1
                ext="." + i.split(".")[-1]
                for folder_name in self.folders.items():
                    # print(folder_name)
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext in folder_name[1] and folder_name[0]=="image":
                        images = images + 1
                    if ext in folder_name[1] and folder_name[0]=="audio":
                        audios+=1
                    if ext in folder_name[1] and folder_name[0]=="video":
                        videos+=1
                    if ext in folder_name[1] and folder_name[0]=="document":
                        documents+=1
        #  ----------- For Calculating Other Files ------------
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directory,i)) == True:
                ext="." + i.split(".")[-1]
                if ext not in combine_list:
                    others+=1

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_doc.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files: "+str(self.count))
        
    def browse_function(self):
        op=filedialog.askdirectory(title="Select The Folder You Want To Sort")
        if op!=None:
            # print(op)
            self.var_foldername.set(str(op))
        self.directory=self.var_foldername.get()
        self.other_name="others"
        self.rename_folder()
        self.all_files=os.listdir(self.directory)
        length=len(self.all_files)
        count=1
        self.Total_count()
        self.btn_start_button.config(state=NORMAL)

    def start_fuction(self):
            if self.var_foldername.get()!="":
                self.btn_clear_button.config(state=DISABLED)
                c=0
                for i in self.all_files:
                    if os.path.isfile(os.path.join(self.directory,i)) == True:
                        c+=1
                        self.create_move(i.split(".")[-1],i)
                        self.lbl_status_t.config(text="TOTAL: "+str(self.count))
                        self.lbl_status_m.config(text="MOVED: "+str(c))
                        self.lbl_status_l.config(text="LEFT: "+str(self.count-c))

                        self.lbl_status_t.update()
                        self.lbl_status_m.update()
                        self.lbl_status_l.update()

                    # print(f"Total Files: {length} | Moved: {count} | Left: {length-count}")
                        
                messagebox.showinfo("Success","All Files Has Moved Successfully")
                self.btn_start_button.config(state=DISABLED)
                self.btn_clear_button.config(state=NORMAL)
            else:
                messagebox.showerror("Error!","Please Select A Folder First")

    def clear(self):
        self.btn_start_button.config(state=DISABLED)
        self.var_foldername.set("")

        self.lbl_status_t.config(text="")
        self.lbl_status_m.config(text="")
        self.lbl_status_l.config(text="")

        self.lbl_total_image.config(text="Total Images ")
        self.lbl_total_audio.config(text="Total Audios ")
        self.lbl_total_video.config(text="Total Videos")
        self.lbl_total_doc.config(text="Total Documents ")
        self.lbl_total_other.config(text="Other Files ")
        self.lbl_total_files.config(text="Total Files ")


    def rename_folder(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory,folder))==True:
                os.rename(os.path.join(self.directory,folder),os.path.join(self.directory,self.folder.lower()))



    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if "." + ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory,folder_name))
                shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,folder_name))
                find=True
                break
        if find !=True:
            if self.other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory,self.other_name))
            shutil.move(os.path.join(self.directory,file_name),os.path.join(self.directory,self.other_name))


root=Tk()
obj=Sorting_App(root)
root.mainloop()