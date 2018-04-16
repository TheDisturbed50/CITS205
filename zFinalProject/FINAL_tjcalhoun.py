# Thomas Calhoun
# EXTRA CREDIT
# tjcalhoun@alaska.edu 24 Mar 2016
# Python 3.5.1

# DUE 28 APR 2016

import matplotlib
import matplotlib.pyplot as plot
from mpl_toolkits.basemap import Basemap

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from tkinter import ttk
from PIL import Image
from matplotlib.image import pil_to_array
from math import radians, cos, sin, asin, sqrt
import tkinter as tk
import numpy as np
import tkinter.messagebox as tkmb

# \/ \/ \/ Global Variables \/ \/ \/
# Target Specs
targets = dict(AF2401=[64.599793, -148.208310], AF2402=[64.794088, -148.015832], AF2403=[64.732308, -147.835617],
               AF2405=[64.571844, -147.824648], AF2407=[64.667670, -148.195247], AF2417=[64.684219, -147.928126])

# Round Specs
M795 = dict(Name="M795 HE", Type="High Explosive", Weight=97, Fuze=["PD", "VT"], Range=22500)
M549A1 = dict(Name="M549A1 HE-RAP", Type="High Explosive - Rocket Accelerated Projectile", Weight=96,
              Fuze=["PD", "VT"], Range=30100)
M982 = dict(Name="M982 EXCALIBUR", Type="High Explosive - GPS Guided Projectile", Weight=106, Fuze=None, Range=23000)
M485A2 = dict(Name="M485A2", Type="Illumination", Weight=85, Fuze="VT", Range=17600)
XM1066 = dict(Name="XM1066", Type="(Experimental) Infrared - Illumination", Weight=85, Fuze="VT", Range=17600)
# Propellant Specs, modern MACS charges used
M231 = dict(Name="Lima", Min=1, Max=2, Description="Low-level Charge, for short range Targets")
M232A1 = dict(Name="Hotel", Min=3, Max=5, Description="High-level Charge, for long range Targets")
# Howitzer and inventory values
ready = False
gun1 = "M777 Howitzer"
roundsOnHand = {"M795": M795, "M549A1": M549A1, "M982": M982, "M485A2": M485A2, "XM1066": XM1066,}
propellantOnHand = {"M231": M231, "M232A1": M232A1,}
currRound = "M795"
currProp = "M231"
progress = "zero"


#  Some important functions need to be defined from the start, see docstrings for details on each object.
### Save Current Config ###############################################################################################


def save_settings(stg1, stg2, stg3):
    """
    Writes current variable set to file.
    """
    fileO = open("assets/settings.cfg", "w")
    settingCompile = [stg1, stg2, stg3]
    for setting in settingCompile:
        fileO.write(setting)  # writing each list item out
        fileO.write("\n")  # dropping to a new line for next item in list
    fileO.close()

    print("\n\nSave Settings:\n{}\n{}\n{}\nSave Complete!".format(stg1, stg2, stg3))

    tkmb.showinfo("Saved Data", "Current data set has been Saved!")


### Load Last Config ##################################################################################################


def load_settings():
    """
    Load settings, and write over generic variables with saved data.
    """
    global currRound, currProp, progress, setting1, setting2, setting3

    def load_init():
        global setting1, setting2, setting3
        print("\n\nImporting Settings...\n\n")

        fileI = open("assets/settings.cfg",
                     "r")  # import from a different file, so overwrite our defined variables above.

        varList = []  # empty list to append to

        for line in fileI:
            varList.append(line[:-1])  # [:-1] kills the "\n" from reprinting since it interprets lines with it.

        print("List Append Complete\n")

        print("Completed List:\n", varList)

        setting1, setting2, setting3 = varList  # Overwriting variables from the 'save' operation, based on the list.

        print("\n\nSetting1:", setting1,
              "\nSetting2:", setting2,
              "\nSetting3:", setting3)
        fileI.close()

    try:  # Error handler just in case.
        load_init()
    except Exception as err:  # and starts out fresh.
        global setting1, setting2, setting3
        print("File Load Error!")
        tkmb.showerror("Settings Load Failure", "Exception Raised:\n{}\nProgram Defaults will be used.".format(err))
        setting1 = "M795"
        setting2 = "M231"
        setting3 = "zero"

    currRound = setting1
    currProp = setting2
    progress = setting3

    print("Settings Loaded Successfully!")


load_settings()  # To load last saved settings by default.


### Program Exit Command ##############################################################################################


def quitter(event=None):
    """
    A simple function to signal the end of the program.
    Used for GUI widget commands.
    """
    save_settings(currRound, currProp, progress)  # Force saves the current dataset.
    sys.exit()


### INVENTORY SELECT WINDOW ###########################################################################################


def inv_select(event=None):
    """
    Inventory Selection Menu
    """
    self = tk.Tk()
    self.wm_title("pyFATDS Inventory Select")
    self.lift()

    unclasslabel1 = tk.Label(self, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
    unclasslabel1.pack(side=tk.TOP)

    ttk.Button(self, text="Save Changes & Close", command=lambda: verify()).place(x=0, y=0)

    # TK frame to enclose set of pack & place labels
    choices = tk.Frame(self)  # Spare Frame 1 will contain the drop down selections.
    choices.pack(fill=tk.X, pady=5)  # Using the pack system to stack it beneath our other widgets.

    # NOTE: Above, the widget frame did not need a height specified, as the .pack() method on any widget will force-
    #      resize the frame to whatever dimensions it needs. However, the .pack() arguments for the frame itself
    #      will not be over-ridden ('fill', 'padx', 'pady', etc...)
    def verify():
        rnd_menu()
        prop_menu()
        tkmb.showinfo("Verify Selection", "Current Selections:\nShell: {}\nProp: {}".format(currRound, currProp))
        self.destroy()

    rnds = list(roundsOnHand.keys())
    rnd_var = tk.StringVar()
    rnd_var.set(rnds[0])

    def rnd_menu():
        global currRound
        currRound = rnd_var.get()

    rnd_drp_down = tk.OptionMenu(choices, rnd_var, rnds[0], rnds[1], rnds[2], rnds[3], rnds[4])
    rnd_drp_down.pack(side=tk.LEFT, padx=100, anchor=tk.NW)

    props = list(propellantOnHand.keys())
    prp_var = tk.StringVar()
    prp_var.set(props[0])

    def prop_menu():
        global currProp
        currProp = prp_var.get()

    prp_drp_down = tk.OptionMenu(choices, prp_var, props[0], props[1])
    prp_drp_down.pack(side=tk.RIGHT, padx=100, anchor=tk.NE)

    # another TK frame to enclose set of pack & place labels.
    inv = tk.Frame(self)  # Spare Frame 2 will handle the label system associated with drops.
    inv.pack(fill=tk.X, pady=5)
    tk.Frame(self, height=200).pack()  # spacer to expand window

    sh_lab = tk.Label(inv, text="Available Shells", font=("Verdana", 10, "underline", "bold"))
    sh_lab.pack(side=tk.LEFT, padx=80, anchor=tk.NW)
    M795l = tk.Label(self, text="M795 \"High Explosive\"")
    M795l.place(in_=sh_lab, x=0, y=20, anchor=tk.NW, bordermode="outside")
    M549A1l = tk.Label(self, text="M549A1 \"High Explosive - RAP (Rocket Assist Proj.)\"")
    M549A1l.place(in_=sh_lab, x=0, y=40, anchor=tk.NW, bordermode="outside")
    M982l = tk.Label(self, text="M982 \"High Explosive - Excalibur\"")
    M982l.place(in_=sh_lab, x=0, y=60, anchor=tk.NW, bordermode="outside")
    M485A2l = tk.Label(self, text="M485A2 \"Illumination\"")
    M485A2l.place(in_=sh_lab, x=0, y=80, anchor=tk.NW, bordermode="outside")
    XM1066l = tk.Label(self, text="XM1066 \"Illumination - Infrared\"")
    XM1066l.place(in_=sh_lab, x=0, y=100, anchor=tk.NW, bordermode="outside")

    prop_lab = tk.Label(inv, text="Available Propellants", font=("Verdana", 10, "underline", "bold"))
    prop_lab.pack(side=tk.RIGHT, padx=80, anchor=tk.NE)
    M231 = tk.Label(self, text="M231 \"Lima Charge\"")
    M231.place(in_=prop_lab, x=0, y=20, anchor=tk.NW, bordermode="outside")
    M232A1l = tk.Label(self, text="M232A1 \"Hotel Charge\"")
    M232A1l.place(in_=prop_lab, x=0, y=40, anchor=tk.NW, bordermode="outside")


### Reference Window ##################################################################################################


def ref_window(event=None):
    """
    The pyFATDS Reference Window.
    Designed to provide the user with a quick reference to aide in operations as a separate window.
    :return:
    """
    refWindow = tk.Tk()
    refWindow.wm_title("pyFATDS Reference")
    refWindow.lift()

    unclasslabel1 = tk.Label(refWindow, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
    unclasslabel1.pack(side=tk.TOP)

    ref_txt1 = open("assets/txt/arty_ref.pyfatds", "r")  # a true line-saver, pulling my text from file.

    # This next part had me stuck for hours... I needed a scrollbar for the text above (obviously), and scrolling a
    #     frame or even a canvas within a frame was a daunting, buggy task.      ...At first.
    scroll = tk.Scrollbar(refWindow)  # Invoke tkinter's scrollbar, parent to window.
    scroll.pack(side=tk.RIGHT, fill=tk.Y)  # Positional arguments to the right, filling the y-axis.

    ref_txt_lab1 = tk.Text(refWindow, wrap=tk.NONE, yscrollcommand=scroll.set, font=("arial", 8), width=100,
                           bg="gray95")  # the Text widget was my fix. Not only does it support a wicked amount of text,
    #     but it also pairs with scrollbar naturally.
    for line in ref_txt1:
        ref_txt_lab1.insert(tk.END, line)  # to actually associate my file text to the widget.

    ref_txt_lab1.pack(fill=tk.BOTH, pady=25)  # adding a 'pady' constraint, so the close button doesnt overlap.

    scroll.config(command=ref_txt_lab1.yview)  # setting the scrollbar to iterate our Text widget scroll Y position.

    exit_button = ttk.Button(refWindow, text="Close", command=lambda: refWindow.destroy())
    exit_button.place(x=0, y=0)

    label = tk.Label(refWindow, text="Learn About Artillery", font=("courier", 12))
    label.place(in_=unclasslabel1, x=15, y=30, anchor=tk.NW, bordermode="outside")

    refWindow.mainloop()


### Help Window #######################################################################################################


def help_window(event=None):
    """
    A help window for the application.
    This is designed as a separate GUI window from main program container.
    :return:
    """
    helpWindow = tk.Tk()  # Establishment of window.
    helpWindow.wm_title("pyFATDS Help & Info")  # Windowbar Title
    helpWindow.lift()

    extStrings = open("assets/txt/ext_str.pyfatds", "r")  # Help Txt will be embedded from file.
    extTxt = extStrings.read()
    extStrings.close()

    # Some local string variables, to keep the widget arguments short and sweet.
    help_desc = """
    Features & Tips:
    /\\         Press < F1 > to open the Help menu         /\\
    \\/ Press Left or Right keys to navigate between menus \\/

    /\\ Press < F11 > to enable Fullscreen /\\
    \\/ Press < ESC > to leave Fullscreen  \\/
    """

    cpyrght = """
    © 2016 Thomas Calhoun -- All Rights Reserved
    Designed & Implemented by Thomas Calhoun
    """

    # The following is an array of widgets - Labels and Buttons. Using "ttk" on buttons adds some visual improvements.
    exit_button = ttk.Button(helpWindow, text="Close", command=lambda: helpWindow.destroy())
    exit_button.place(x=0, y=0)  # keeping in the corner, using "pack" here would throw off the entire widget grid.

    unclasslabel1 = tk.Label(helpWindow, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
    unclasslabel1.pack(padx=50)

    label = tk.Label(helpWindow, text="pyFATDS Help & Reference", font=("courier", 12))
    label.pack()

    help_desc_label = tk.Label(helpWindow, text=help_desc, font=("arial", 10))
    help_desc_label.pack()

    fa_101_button = ttk.Button(helpWindow, text="Field Artillery for Dummies", command=ref_window)
    fa_101_button.pack()

    disclaimer = tk.Label(helpWindow, text=extTxt, font=("helvetica", 8), fg="blue", justify="left")
    disclaimer.pack(pady=10)

    cr_label = tk.Label(helpWindow, text=cpyrght, font=("helvetica", 8), fg="red")
    cr_label.pack(pady=10)

    helpWindow.mainloop()  # Mainloop to make the magic happen.


### APP CONTAINER #####################################################################################################


class pyFATDS(tk.Tk):
    """
    Container class - Manages the main window instance.
    Any following classes are meant to serve as content pages, being raised to the front of the container.
    """

    def __init__(self, *args, **kwargs):  # Init Object
        tk.Tk.__init__(self, *args, **kwargs)  # Init the window
        tk.Tk.iconbitmap(self, default="assets/img/pyfatds_icon.ico")
        tk.Tk.wm_title(self, "PyFATDS 0.1 Alpha")  # Window Titlebar
        self.attributes("-fullscreen", True)  # Starting application in fullscreen.
        self.lift()  # Brings the program to top level within Windows. This way, you dont have to 'click in' or interact
        #     to start using keyboard commands.
        container = tk.Frame(self)  # Initialize the GUI frame as the container space.
        container.pack(side="top", fill="both", expand=True)  # Positional Arguments.
        container.grid_rowconfigure(0, weight=1)  # These keep the content flexible on the canvas.
        container.grid_columnconfigure(0, weight=1)  # Otherwise, it all remains static in size despite the pack method.

        # The following is a gun-status label to show on ALL windows.
        self.yReadyLabel = tk.Label(self, text="READY", bg="green", fg="white", width=12, font=("arial", 20, "bold"))
        self.yReadyLabel.place(relx=1, x=-10, y=9, anchor=tk.NE)
        self.nReadyLabel = tk.Label(self, text="NOT READY", bg="red", width=12, font=("arial", 20, "bold"))
        self.nReadyLabel.place(relx=1, x=-10, y=9, anchor=tk.NE)

        # -- Boolean label operator
        rdy = tk.StringVar()
        self.rddy = rdy  # Redeclared variable, adding "self" to beginning assigns it to 'controller', an can be used
        # by other pages for more timely update.
        rdy.set(str(ready))  # initial setting of above defined stringvar
        # -- Difficulty label operator
        dif = tk.StringVar()
        self.diff = dif
        dif.set(progress)

        def rdy_refresh(*args):
            rdy.set(str(ready))  # tied to the global boolean, we convert it to a tkinter-friendly StringVar.

        tk.Label(self, textvariable=rdy).place(relx=1, x=-25, y=49, anchor=tk.NE)
        tk.Label(self, text="Difficulty Level:").place(relx=1, x=-50, y=69, anchor=tk.NE)
        tk.Label(self, textvariable=dif).place(relx=1, x=-25, y=69, anchor=tk.NE)
        self.bind("<Button-1>", rdy_refresh)  # Bind the refresh function to left mouse click...
        # I suppose, it may be more timely if tied to the button commands that originally change the bool value (hmm...)
        # -- End/ boolean label operator

        # Universal page items (here to become static across pages)
        ttk.Button(self, text="Help", command=help_window, width=6).place(x=0, y=0)
        ttk.Button(self, text="Exit", command=quitter, width=6).place(x=45, y=0)

        self.frames = {}  # Empty dict, to maintain page data when the program is run.

        # Loop ties in the pages to be loaded into the container.
        for F in (StartPage, One_Setup, Two_MissionArea):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # declare our starting point in the program.

        self.protocol("WM_DELETE_WINDOW", quitter)  # Properly closes program when main window is closed.
        self.bind("<Control-q>", quitter)  # Threw in a key binding to exit as well.
        self.bind("<F1>", help_window)

        self.state = True  # The following code and 2 fullscreen functions, are the toggle feature to/from fullscreen.
        self.bind("<F11>", self.start_fullscreen)
        self.bind("<Escape>", self.end_fullscreen)

    def start_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.attributes("-fullscreen", False)
        return "break"

    def show_frame(self, cont):
        """
        This is the page switch, callable from button command for navigation.
        :param cont:
        :return:
        """
        frame = self.frames[cont]
        frame.tkraise()


### START PAGE ########################################################################################################


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # ----------/Arrow Key Binding for Nav/---------------------------------------------------------------------- #
        def key_right0(event=None):
            controller.show_frame(One_Setup)

        controller.bind("<Right>", key_right0)
        # ----------------------------------------------------------------------------------------------------------- #
        unclasslabel1 = tk.Label(self, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
        unclasslabel1.pack()

        label = tk.Label(self, text="pyFATDS Start", font=("courier", 12))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="-> Proceed", command=lambda: controller.show_frame(One_Setup))
        button1.pack()

        intro_file = open("assets/txt/intro.pyfatds", "r")
        intro_txt = intro_file.read()
        intro_file.close()

        tk.Label(self, text=intro_txt, font=("arial", 16, "bold")).pack()
        tk.Label(self, text="""
/\\         Press < F1 > to open the Help menu         /\\
\\/ Press Left or Right keys to navigate between menus \\/
        """, font=("courier", 10, "bold")).pack(side=tk.BOTTOM, pady=15)
        tk.Label(self, text="Note: This program is only tested for compatibility with Windows 7 & above."
                            "", fg="red").pack(side=tk.BOTTOM, pady=15)


### PAGE ONE ##########################################################################################################


class One_Setup(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def key_left1(event=None):
            controller.show_frame(StartPage)

        def key_right1(event=None):
            controller.show_frame(Two_MissionArea)

        controller.bind("<Left>", key_left1)
        controller.bind("<Right>", key_right1)

        def not_ready_toggle():
            global ready
            if ready:
                ready = False
                controller.rddy.set(str(ready))  # Live update for boolean label.
                controller.yReadyLabel.place_forget()  # Removes the opposing label from view.
                controller.nReadyLabel.place(relx=1, x=-10, y=9, anchor=tk.NE)  # Positions the correct label into view.

        def ready_toggle():
            global ready
            if not ready:
                ready = True
                controller.rddy.set(str(ready))
                controller.nReadyLabel.place_forget()
                controller.yReadyLabel.place(relx=1, x=-10, y=9, anchor=tk.NE)
                tkmb.showwarning("Gun Status", "Gun Battery is now HOT!")

        unclasslabel1 = tk.Label(self, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
        unclasslabel1.pack()

        label = tk.Label(self, text="pyFATDS Operations -- Data Setup", font=("courier", 12))
        label.pack(pady=10, padx=10)

        button0 = ttk.Button(self, text="-> Proceed to Mission Page",
                             command=lambda: controller.show_frame(Two_MissionArea))
        button0.pack()

        button1 = ttk.Button(self, text="<- Return to Start Page", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # User acknowledgement of ready status...
        readyButton = ttk.Button(self, text="Ready!", command=lambda: ready_toggle())
        readyButton.pack()
        # ...or not ready.
        notReadyButton = ttk.Button(self, text="Not Ready!", command=lambda: not_ready_toggle())
        notReadyButton.pack()

        # Blank Frame to space out widgets.
        spacer = tk.Frame(self, height=100)
        spacer.pack(fill=tk.X, pady=5)

        ttk.Button(self, text="Select Munitions", command=lambda: inv_select()).pack()  # Takes user to Inventory

        tk.Frame(self, height=75).pack()  # spacer
        tk.Label(self, text="Current Munition Selections", font=("arial", 12, "bold", "underline")).pack()

        # Placement of labels vertically, binding a .pack() method to a side works, but stacking is miserable without
        #    placing additional frames. Not taking advantage of this shows them offset and and typically in the
        #    wrong place.
        a_frame = tk.Frame(self)
        a_frame.pack(fill=tk.X)
        b_frame = tk.Frame(self)
        b_frame.pack(fill=tk.X)
        c_frame = tk.Frame(self)
        c_frame.pack(fill=tk.X)

        global shell_desc_var, prop_desc_var
        shell_var = tk.StringVar()
        prop_var = tk.StringVar()
        shell_desc_var = tk.StringVar()
        prop_desc_var = tk.StringVar()

        def get_desc(event=None):
            global shell_desc_var, prop_desc_var
            if currRound == "M795":
                desc = M795.get("Type")
                shell_desc_var.set(desc)
            elif currRound == "M549A1":
                desc = M549A1.get("Type")
                shell_desc_var.set(desc)
            elif currRound == "M982":
                desc = M982.get("Type")
                shell_desc_var.set(desc)
            elif currRound == "M485A2":
                desc = M485A2.get("Type")
                shell_desc_var.set(desc)
            elif currRound == "XM1066":
                desc = XM1066.get("Type")
                shell_desc_var.set(desc)
            else:
                tkmb.showerror("Internal Error", "Unable to read Shell information from database...")
            shell_var.set(currRound)  # worked these in for a mass variable update on this page.
            prop_var.set(currProp)
            if currProp == "M231":
                desc = M231.get("Description")
                prop_desc_var.set(desc)
            elif currProp == "M232A1":
                desc = M232A1.get("Description")
                prop_desc_var.set(desc)
            else:
                tkmb.showerror("Internal Error", "Unable to read Prop information from database...")

        self.bind("<Enter>", get_desc)  # Triggers the update by moving the cursor into window view.

        sel_title = tk.Label(a_frame, text="Type", font=("arial", 10, "bold", "underline"))
        sel_title.pack(side=tk.LEFT, padx=160, anchor=tk.W)
        sel_desc = tk.Label(a_frame, text="Description", font=("arial", 10, "bold", "underline"))
        sel_desc.pack(side=tk.RIGHT, padx=160, anchor=tk.E)

        shell = tk.Label(b_frame, textvariable=shell_var, font=("arial"), fg="red")
        shell.pack(side=tk.LEFT, padx=150, anchor=tk.W)
        sh_desc = tk.Label(b_frame, textvariable=shell_desc_var, font=("arial"), fg="red")
        sh_desc.pack(side=tk.RIGHT, padx=150, anchor=tk.E)

        prop = tk.Label(c_frame, textvariable=prop_var, font=("arial"), fg="red")
        prop.pack(side=tk.LEFT, padx=150, anchor=tk.W)
        prop_desc = tk.Label(c_frame, textvariable=prop_desc_var, font=("arial"), fg="red")
        prop_desc.pack(side=tk.RIGHT, padx=150, anchor=tk.E)


### PAGE TWO ##########################################################################################################


class Two_MissionArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def key_left2(event=None):
            controller.show_frame(One_Setup)

        controller.bind("<Left>", key_left2)

        unclasslabel1 = tk.Label(self, text="// UNCLASSIFIED //", font=("courier", 18, "bold"), fg="green")
        unclasslabel1.pack()

        label = tk.Label(self, text="pyFATDS Operations -- Mission Area", font=("courier", 12))
        label.pack(pady=10, padx=10)

        button0 = ttk.Button(self, text="<- Return to Start Page", command=lambda: controller.show_frame(StartPage))
        button0.pack()

        button1 = ttk.Button(self, text="<- Return to Setup Page", command=lambda: controller.show_frame(One_Setup))
        button1.pack()
        # -------------/Start MatPlotLib Params/--------------------------------------------------------------------- #
        mf2 = plot.figure(figsize=(4, 3), dpi=200)

        gun_grid = [64.83, -147.71]
        gunp2 = None
        line_array = None

        def gun_loc2(event=None):  # Plot friendly unit location.
            global gunp2, gun_plot_txt
            gun_lat, gun_lon = gun_grid
            xpt, ypt = m2(gun_lon, gun_lat)  # To map, have to flip lat/lon values.
            gunp2 = m2.plot(xpt, ypt, "^", markersize=6, color="b")  # Plots the marker
            gun_plot_txt = plot.text(xpt, ypt, "Gun 1", fontsize=8, fontweight='bold',
                                     ha='left', va='bottom', color='b')  # Labels the marker.
            mf2.canvas.draw()  # Makes changes effective on the visible map.

        tgt_plot = None

        def active_target(targ_grid, tgt_id, event=None):  # Plot target data.
            global tgt_plot, tgt_plot_txt, line_array
            tgt_lat, tgt_lon = targ_grid
            xpt, ypt = m2(tgt_lon, tgt_lat)
            tgt_plot = m2.plot(xpt, ypt, "+", markersize=10, color="r")
            tgt_plot_txt = plot.text(xpt, ypt, tgt_id, fontsize=8, fontweight='bold',
                                     ha="left", va="bottom", color="m")
            line_array_lat = [gun_grid[0], tgt_lat]
            line_array_lon = [gun_grid[1], tgt_lon]
            x, y = m2(line_array_lon, line_array_lat)
            line_array = m2.plot(x, y, marker=None, color='r')
            mf2.canvas.draw()

        def remove_plots2(event=None):  # "Reference to the Biblical book of Job 1:21"
            global gunp2, tgt_plot, tgt_plot_txt, gun_plot_txt, line_array  # For we giveth the map plots...
            gunp2.pop(0).remove()  # And then,
            gun_plot_txt.remove()
            tgt_plot.pop(0).remove()  # We taketh away.
            tgt_plot_txt.remove()
            mf2.canvas.draw()  # *Drops Mic*

        def remove_tgt_only(event=None):  # a singular removal option.
            global tgt_plot, tgt_plot_txt, tgt_bool, line_array
            tgt_plot.pop(0).remove()
            line_array.pop(0).remove()
            tgt_plot_txt.remove()
            mf2.canvas.draw()
            tgt_bool = False

        def gun_trajectory(shell, prop):  # TODO WORK IN PROGRESS
            # Thinking of a max shell distance divided by prop charge computation.
            # then account for mission type and determine the 'effectiveness', scoring the user on time taken
            # and choices of munitions.
            pass

        dist = 0.0

        def range_calc(target_grid, gun_grid):
            """
            Borrowed this code from the World Wide Web, one of my very few direct copy & pastes
            to get a job done. Credit to the Haversine Formula.
            """
            global dist
            # ----/Thomas Edits/------------------------------------------------------------------------------------- #
            lat1, lon1 = target_grid
            lat2, lon2 = gun_grid
            # ------------------------------------------------------------------------------------------------------- #
            # convert decimal degrees to radians
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

            # haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * asin(sqrt(a))
            r = 6371  # Radius of earth in kilometers. Use 3956 for miles
            dist = c * r
            return dist

        max_time = 0
        target = ""
        tgt_grid = []

        def lvl_up(lvl):
            global progress
            if lvl == "zero":
                progress = "one"
                return
            elif lvl == "one":
                progress = "two"
                return
            elif lvl == "two":
                progress = "three"
                return
            elif lvl == "three":
                progress = "four"
                return
            elif lvl == "four":
                progress = "five"
                return
            elif lvl == "five":
                progress = "custom"
                return
            else:
                progress = "zero"

        range_var = tk.StringVar()
        range_var.set(dist)
        rng_label_label = tk.Label(self, text="Range (Km):", font=("arial", 12, "bold"))
        rng_label_label.place(relx=1, x=-200, y=100, anchor=tk.NE)
        rng_label = tk.Label(self, textvariable=range_var, font=("arial", 12, "bold"))
        rng_label.place(relx=1, x=-10, y=100, anchor=tk.NE)

        global tgt_bool  # THIS made it work............ *throws up imaginary papers*
        tgt_bool = False

        def mission_action(tgt_name):  # taking our target info (predefined), to plot on map.
            """
            A line-saving effort, to streamline by use of functions to minimize redundancy.
            """
            global range, rng_label, dist, tgt_bool
            tgt_grid = targets.get(tgt_name)
            active_target(tgt_grid, tgt_name)
            lvl_up(progress)
            dist = range_calc(tgt_grid, gun_grid)
            range_var.set(dist)
            tgt_bool = True

        def custom_mission():  # A BIG work in progress, Mainly just need to make sure the IntVar is working right,
            popup = tk.Tk()             # and where the breakdown of info is occurring.
            popup.wm_title("pyFATDS Custom Mission")
            popup.lift()
            popup.attributes('-topmost', True)

            def quitter_2_point_0(event=None):
                global progress
                progress = "zero"
                popup.destroy()

            popup.protocol("WM_DELETE_WINDOW", quitter_2_point_0)

            tk.Label(popup, text="""Welcome to the Custom Module!
You can move this window freely, but it will always remain on top!
Below are options to plot your own target!
We do not yet support picking from the map, so use your best judgement!
            """, font=("arial", 10)).pack(padx=25, pady=40)

            tk.Label(popup, text="UNDER CONSTRUCTION!\nThis feature is bugged and not working properly!",
                     font=("arial", 12, "bold")).pack()

            uname = tk.StringVar()
            pv_lat = tk.IntVar()
            pv_lon = tk.IntVar()

            tk.Label(popup, text="Your Name:", font=("courier")).pack()
            tk.Entry(popup, textvariable=uname).pack(pady=10)
            widget_frame1 = tk.Frame(popup)
            widget_frame1.pack(fill=tk.X)
            widget_frame2 = tk.Frame(popup)
            widget_frame2.pack(fill=tk.X)
            tk.Label(widget_frame1, text="Latitude Entry:   ", font=("courier")).pack(side=tk.LEFT)
            tk.Entry(widget_frame1, textvariable=pv_lat).pack(side=tk.LEFT, pady=10)

            tk.Label(widget_frame2, text="Longitude Entry:  ", font=("courier")).pack(side=tk.LEFT)
            tk.Entry(widget_frame2, textvariable=pv_lon).pack(side=tk.LEFT, pady=10)

            def plot_custom(event=None):
                if tgt_bool:
                    remove_tgt_only()  # Clears the board for the user.
                cust_lat = pv_lat.get()
                cust_lon = pv_lon.get()
                cust_tgt_name = str(uname.get())+"'s Target"
                cust_grid = [cust_lat, cust_lon]

                def cust_plot_init(event=None):
                    global tgt_bool
                    active_target(cust_grid, cust_tgt_name)
                    dist = range_calc(cust_grid, gun_grid)
                    range_var.set(dist)
                    tgt_bool = True

                controller.bind("<Return>", cust_plot_init)

            ttk.Button(popup, text="Submit", command=plot_custom).pack(side=tk.BOTTOM)
            ttk.Button(popup, text="Close & Restart", command=quitter_2_point_0).place(x=0, y=0)

            popup.mainloop()

        def mission(lvl):
            global max_time, target, tgt_grid
            if not ready:
                tkmb.showerror("NO GO", "Operations is a NO-GO, gun is in a NOT READY status!\n"
                                        "Please move to READY in the setup page to proceed...")
                return
            if lvl == "zero":
                max_time = 90
                target = "AF2401"
            elif lvl == "one":
                max_time = 55
                target = "AF2402"
            elif lvl == "two":
                max_time = 50
                target = "AF2403"
            elif lvl == "three":
                max_time = 40
                target = "AF2405"
            elif lvl == "four":
                max_time = 30
                target = "AF2407"
            elif lvl == "five":
                max_time = 15
                target = "AF2417"
            elif lvl == "custom":  # last effort to make this fun... lol
                custom_mission()
                return
            if tgt_bool is not True:
                mission_action(target)
                return
            remove_tgt_only()
            mission_action(target)

        show_battery = ttk.Button(self, text="Show Gun Battery", command=gun_loc2)
        show_battery.pack(side=tk.LEFT, padx=20)
        mission_tgt_show = ttk.Button(self, text="Mission Proceed", command=lambda: mission(progress))
        mission_tgt_show.place(in_=show_battery, relx=0.5, y=-2, anchor=tk.S, bordermode="outside")
        hide_plots = ttk.Button(self, text="Hide Target Locations", command=remove_plots2)
        hide_plots.place(in_=mission_tgt_show, relx=0.5, y=-2, anchor=tk.S, bordermode="outside")

        def prog_bind(event=None):
            controller.diff.set(progress)

        controller.bind("<Enter>", prog_bind)
        # -------------/Start Basemap Params/------------------------------------------------------------------------ #
        canvas = FigureCanvasTkAgg(mf2, self)
        m2 = Basemap(projection="mill",
                     llcrnrlat=64.4711,
                     llcrnrlon=-148.7329,
                     urcrnrlat=64.8764,
                     urcrnrlon=-146.6249,
                     resolution="l", )

        pilImage = Image.open("assets/img/iak_topo.png")
        arrayImg = pil_to_array(pilImage)
        im = m2.imshow(arrayImg, origin="upper")  # Projects custom imagery as Background.

        m2.drawmeridians(np.arange(0, 360, .5), linewidth=0.2, dashes=[2, 4], labels=[0, 1, 1, 0], color='r',
                         labelstyle="+/-", fontsize=6)
        m2.drawparallels(np.arange(-90, 100, .2), linewidth=0.2, dashes=[2, 4], labels=[1, 0, 0, 1], color='r',
                         labelstyle="+/-", fontsize=6)

        canvas.show()
        # -------------/End Basemap Params/-------------------------------------------------------------------------- #

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


### INITIALIZATION ####################################################################################################

app = pyFATDS()
app.mainloop()