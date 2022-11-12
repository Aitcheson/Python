#timezone converter v3

#for date and time
import datetime
import zoneinfo

#gui elements
import tkinter as tk

#Opens gui window
window = tk.Tk()

#Renames gui window
window.title("Timezone Tool v3")


#Users current time, date and time of day
time_now = datetime.datetime.now()

time_now_tod = "error"
if time_now.hour == 0:
    time_now_tod = "Midnight"
elif time_now.hour <= 5:
    time_now_tod = "Early Morning"
elif time_now.hour <= 11:
    time_now_tod = "Morning"
elif time_now.hour == 12:
    time_now_tod = "Noon"
elif time_now.hour <= 15:
    time_now_tod = "Afternoon"
elif time_now.hour <= 20:
    time_now_tod= "Evening"
elif time_now.hour <= 23:
    time_now_tod = "Night"


#Coordinated Universal Time
current_utc = datetime.datetime.utcnow()

current_utc_tod = "error"
if current_utc.hour == 0:
    current_utc_tod = "Midnight"
elif current_utc.hour <= 5:
    current_utc_tod = "Early Morning"
elif current_utc.hour <= 11:
    current_utc_tod = "Morning"
elif current_utc.hour == 12:
    current_utc_tod = "Noon"
elif current_utc.hour <= 15:
    current_utc_tod = "Afternoon"
elif current_utc.hour <= 20:
    current_utc_tod= "Evening"
elif current_utc.hour <= 23:
    current_utc_tod = "Night"


#Central European Time
timezone_cet = zoneinfo.ZoneInfo('Etc/GMT-1')
current_cet = datetime.datetime.now(tz=timezone_cet)

current_cet_tod = "error"
if current_cet.hour == 0:
    current_cet_tod = "Midnight"
elif current_cet.hour <= 5:
    current_cet_tod = "Early Morning"
elif current_cet.hour <= 11:
    current_cet_tod = "Morning"
elif current_cet.hour == 12:
    current_cet_tod = "Noon"
elif current_cet.hour <= 15:
    current_cet_tod = "Afternoon"
elif current_cet.hour <= 20:
    current_cet_tod= "Evening"
elif current_cet.hour <= 23:
    current_cet_tod = "Night"


#Eastern European Time
timezone_eet = zoneinfo.ZoneInfo('Etc/GMT-2')
current_eet = datetime.datetime.now(tz=timezone_eet)

current_eet_tod = "error"
if current_eet.hour == 0:
    current_eet_tod = "Midnight"
elif current_eet.hour <= 5:
    current_eet_tod = "Early Morning"
elif current_eet.hour <= 11:
    current_eet_tod = "Morning"
elif current_eet.hour == 12:
    current_eet_tod = "Noon"
elif current_eet.hour <= 15:
    current_eet_tod = "Afternoon"
elif current_eet.hour <= 20:
    current_eet_tod= "Evening"
elif current_eet.hour <= 23:
    current_eet_tod = "Night"


#East African Time
timezone_eat = zoneinfo.ZoneInfo('Etc/GMT-3')
current_eat = datetime.datetime.now(tz=timezone_eat)

current_eat_tod = "error"
if current_eat.hour == 0:
    current_eat_tod = "Midnight"
elif current_eat.hour <= 5:
    current_eat_tod = "Early Morning"
elif current_eat.hour <= 11:
    current_eat_tod = "Morning"
elif current_eat.hour == 12:
    current_eat_tod = "Noon"
elif current_eat.hour <= 15:
    current_eat_tod = "Afternoon"
elif current_eat.hour <= 20:
    current_eat_tod= "Evening"
elif current_eat.hour <= 23:
    current_eat_tod = "Night"

    
#Samara Time
timezone_st = zoneinfo.ZoneInfo('Etc/GMT-4')
current_st = datetime.datetime.now(tz=timezone_st)

current_st_tod = "error"
if current_st.hour == 0:
    current_st_tod = "Midnight"
elif current_st.hour <= 5:
    current_st_tod = "Early Morning"
elif current_st.hour <= 11:
    current_st_tod = "Morning"
elif current_st.hour == 12:
    current_st_tod = "Noon"
elif current_st.hour <= 15:
    current_st_tod = "Afternoon"
elif current_st.hour <= 20:
    current_st_tod= "Evening"
elif current_st.hour <= 23:
    current_st_tod = "Night"

    
#Pakistan Lahore Time
timezone_plt = zoneinfo.ZoneInfo('Etc/GMT-5')
current_plt = datetime.datetime.now(tz=timezone_plt)

current_plt_tod = "error"
if current_plt.hour == 0:
    current_plt_tod = "Midnight"
elif current_plt.hour <= 5:
    current_plt_tod = "Early Morning"
elif current_plt.hour <= 11:
    current_plt_tod = "Morning"
elif current_plt.hour == 12:
    current_plt_tod = "Noon"
elif current_plt.hour <= 15:
    current_plt_tod = "Afternoon"
elif current_plt.hour <= 20:
    current_plt_tod= "Evening"
elif current_plt.hour <= 23:
    current_plt_tod = "Night"

    
#Bangladesh Standard Time
timezone_bst = zoneinfo.ZoneInfo('Etc/GMT-6')
current_bst = datetime.datetime.now(tz=timezone_bst)

current_bst_tod = "error"
if current_bst.hour == 0:
    current_bst_tod = "Midnight"
elif current_bst.hour <= 5:
    current_bst_tod = "Early Morning"
elif current_bst.hour <= 11:
    current_bst_tod = "Morning"
elif current_bst.hour == 12:
    current_bst_tod = "Noon"
elif current_bst.hour <= 15:
    current_bst_tod = "Afternoon"
elif current_bst.hour <= 20:
    current_bst_tod= "Evening"
elif current_bst.hour <= 23:
    current_bst_tod = "Night"

    
#Vietnam Standard Time
timezone_vst = zoneinfo.ZoneInfo('Etc/GMT-7')
current_vst = datetime.datetime.now(tz=timezone_vst)

current_vst_tod = "error"
if current_vst.hour == 0:
    current_vst_tod = "Midnight"
elif current_vst.hour <= 5:
    current_vst_tod = "Early Morning"
elif current_vst.hour <= 11:
    current_vst_tod = "Morning"
elif current_vst.hour == 12:
    current_vst_tod = "Noon"
elif current_vst.hour <= 15:
    current_vst_tod = "Afternoon"
elif current_vst.hour <= 20:
    current_vst_tod= "Evening"
elif current_vst.hour <= 23:
    current_vst_tod = "Night"

    
#China Taiwan Time
timezone_ctt = zoneinfo.ZoneInfo('Etc/GMT-8')
current_ctt = datetime.datetime.now(tz=timezone_ctt)

current_ctt_tod = "error"
if current_ctt.hour == 0:
    current_ctt_tod = "Midnight"
elif current_ctt.hour <= 5:
    current_ctt_tod = "Early Morning"
elif current_ctt.hour <= 11:
    current_ctt_tod = "Morning"
elif current_ctt.hour == 12:
    current_ctt_tod = "Noon"
elif current_ctt.hour <= 15:
    current_ctt_tod = "Afternoon"
elif current_ctt.hour <= 20:
    current_ctt_tod= "Evening"
elif current_ctt.hour <= 23:
    current_ctt_tod = "Night"

    
#Japan Standard Time
timezone_jst = zoneinfo.ZoneInfo('Etc/GMT-9')
current_jst = datetime.datetime.now(tz=timezone_jst)

current_jst_tod = "error"
if current_jst.hour == 0:
    current_jst_tod = "Midnight"
elif current_jst.hour <= 5:
    current_jst_tod = "Early Morning"
elif current_jst.hour <= 11:
    current_jst_tod = "Morning"
elif current_jst.hour == 12:
    current_jst_tod = "Noon"
elif current_jst.hour <= 15:
    current_jst_tod = "Afternoon"
elif current_jst.hour <= 20:
    current_jst_tod= "Evening"
elif current_jst.hour <= 23:
    current_jst_tod = "Night"

    
#Australian Eastern Time
timezone_aet = zoneinfo.ZoneInfo('Etc/GMT-10')
current_aet = datetime.datetime.now(tz=timezone_aet)

current_aet_tod = "error"
if current_aet.hour == 0:
    current_aet_tod = "Midnight"
elif current_aet.hour <= 5:
    current_aet_tod = "Early Morning"
elif current_aet.hour <= 11:
    current_aet_tod = "Morning"
elif current_aet.hour == 12:
    current_aet_tod = "Noon"
elif current_aet.hour <= 15:
    current_aet_tod = "Afternoon"
elif current_aet.hour <= 20:
    current_aet_tod= "Evening"
elif current_aet.hour <= 23:
    current_aet_tod = "Night"

    
#Solomon Standard Time
timezone_sst = zoneinfo.ZoneInfo('Etc/GMT-11')
current_sst = datetime.datetime.now(tz=timezone_sst)

current_sst_tod = "error"
if current_sst.hour == 0:
    current_sst_tod = "Midnight"
elif current_sst.hour <= 5:
    current_sst_tod = "Early Morning"
elif current_sst.hour <= 11:
    current_sst_tod = "Morning"
elif current_sst.hour == 12:
    current_sst_tod = "Noon"
elif current_sst.hour <= 15:
    current_sst_tod = "Afternoon"
elif current_sst.hour <= 20:
    current_sst_tod= "Evening"
elif current_sst.hour <= 23:
    current_sst_tod = "Night"


#New Zealand Standard Time
timezone_nzst = zoneinfo.ZoneInfo('Etc/GMT-12')
current_nzst = datetime.datetime.now(tz=timezone_nzst)

current_nzst_tod = "error"
if current_nzst.hour == 0:
    current_nzst_tod = "Midnight"
elif current_nzst.hour <= 5:
    current_nzst_tod = "Early Morning"
elif current_nzst.hour <= 11:
    current_nzst_tod = "Morning"
elif current_nzst.hour == 12:
    current_nzst_tod = "Noon"
elif current_nzst.hour <= 15:
    current_nzst_tod = "Afternoon"
elif current_nzst.hour <= 20:
    current_nzst_tod= "Evening"
elif current_nzst.hour <= 23:
    current_nzst_tod = "Night"


#Midway Islands Time
timezone_mit = zoneinfo.ZoneInfo('Etc/GMT+11')
current_mit = datetime.datetime.now(tz=timezone_mit)

current_mit_tod = "error"
if current_mit.hour == 0:
    current_mit_tod = "Midnight"
elif current_mit.hour <= 5:
    current_mit_tod = "Early Morning"
elif current_mit.hour <= 11:
    current_mit_tod = "Morning"
elif current_mit.hour == 12:
    current_mit_tod = "Noon"
elif current_mit.hour <= 15:
    current_mit_tod = "Afternoon"
elif current_mit.hour <= 20:
    current_mit_tod= "Evening"
elif current_mit.hour <= 23:
    current_mit_tod = "Night"


#Hawaii Standard Time
timezone_hst = zoneinfo.ZoneInfo('Etc/GMT+10')
current_hst = datetime.datetime.now(tz=timezone_hst)

current_hst_tod = "error"
if current_hst.hour == 0:
    current_hst_tod = "Midnight"
elif current_hst.hour <= 5:
    current_hst_tod = "Early Morning"
elif current_hst.hour <= 11:
    current_hst_tod = "Morning"
elif current_hst.hour == 12:
    current_hst_tod = "Noon"
elif current_hst.hour <= 15:
    current_hst_tod = "Afternoon"
elif current_hst.hour <= 20:
    current_hst_tod= "Evening"
elif current_hst.hour <= 23:
    current_hst_tod = "Night"


#Alaska Standard Time
timezone_ast = zoneinfo.ZoneInfo('Etc/GMT+9')
current_ast = datetime.datetime.now(tz=timezone_ast)

current_ast_tod = "error"
if current_ast.hour == 0:
    current_ast_tod = "Midnight"
elif current_ast.hour <= 5:
    current_ast_tod = "Early Morning"
elif current_ast.hour <= 11:
    current_ast_tod = "Morning"
elif current_ast.hour == 12:
    current_ast_tod = "Noon"
elif current_ast.hour <= 15:
    current_ast_tod = "Afternoon"
elif current_ast.hour <= 20:
    current_ast_tod= "Evening"
elif current_ast.hour <= 23:
    current_ast_tod = "Night"


#Pacific Standard Time
timezone_pst = zoneinfo.ZoneInfo('US/Pacific')
current_pst = datetime.datetime.now(tz=timezone_pst)

current_pst_tod = "error"
if current_pst.hour == 0:
    current_pst_tod = "Midnight"
elif current_pst.hour <= 5:
    current_pst_tod = "Early Morning"
elif current_pst.hour <= 11:
    current_pst_tod = "Morning"
elif current_pst.hour == 12:
    current_pst_tod = "Noon"
elif current_pst.hour <= 15:
    current_pst_tod = "Afternoon"
elif current_pst.hour <= 20:
    current_pst_tod= "Evening"
elif current_pst.hour <= 23:
    current_pst_tod = "Night"


#Mountain Standard Time
timezone_mst = zoneinfo.ZoneInfo('US/Mountain')
current_mst = datetime.datetime.now(tz=timezone_mst)

current_mst_tod = "error"
if current_mst.hour == 0:
    current_mst_tod = "Midnight"
elif current_mst.hour <= 5:
    current_mst_tod = "Early Morning"
elif current_mst.hour <= 11:
    current_mst_tod = "Morning"
elif current_mst.hour == 12:
    current_mst_tod = "Noon"
elif current_mst.hour <= 15:
    current_mst_tod = "Afternoon"
elif current_mst.hour <= 20:
    current_mst_tod= "Evening"
elif current_mst.hour <= 23:
    current_mst_tod = "Night"


#Central Standard Time
timezone_cst = zoneinfo.ZoneInfo('US/Central')
current_cst = datetime.datetime.now(tz=timezone_cst)

current_cst_tod = "error"
if current_cst.hour == 0:
    current_cst_tod = "Midnight"
elif current_cst.hour <= 5:
    current_cst_tod = "Early Morning"
elif current_cst.hour <= 11:
    current_cst_tod = "Morning"
elif current_cst.hour == 12:
    current_cst_tod = "Noon"
elif current_cst.hour <= 15:
    current_cst_tod = "Afternoon"
elif current_cst.hour <= 20:
    current_cst_tod= "Evening"
elif current_cst.hour <= 23:
    current_cst_tod = "Night"


#Eastern time and date
timezone_est = zoneinfo.ZoneInfo('US/Eastern')
current_est = datetime.datetime.now(tz=timezone_est)

current_est_tod = "error"
if current_est.hour == 0:
    current_est_tod = "Midnight"
elif current_est.hour <= 5:
    current_est_tod = "Early Morning"
elif current_est.hour <= 11:
    current_est_tod = "Morning"
elif current_est.hour == 12:
    current_est_tod = "Noon"
elif current_est.hour <= 15:
    current_est_tod = "Afternoon"
elif current_est.hour <= 20:
    current_est_tod= "Evening"
elif current_est.hour <= 23:
    current_est_tod = "Night"


#Peurto Rico Time
timezone_prt = zoneinfo.ZoneInfo('Etc/GMT+4')
current_prt = datetime.datetime.now(tz=timezone_prt)

current_prt_tod = "error"
if current_prt.hour == 0:
    current_prt_tod = "Midnight"
elif current_prt.hour <= 5:
    current_prt_tod = "Early Morning"
elif current_prt.hour <= 11:
    current_prt_tod = "Morning"
elif current_prt.hour == 12:
    current_prt_tod = "Noon"
elif current_prt.hour <= 15:
    current_prt_tod = "Afternoon"
elif current_prt.hour <= 20:
    current_prt_tod= "Evening"
elif current_prt.hour <= 23:
    current_prt_tod = "Night"


#Brazil Eastern Time
timezone_bet = zoneinfo.ZoneInfo('Etc/GMT+3')
current_bet = datetime.datetime.now(tz=timezone_bet)

current_bet_tod = "error"
if current_bet.hour == 0:
    current_bet_tod = "Midnight"
elif current_bet.hour <= 5:
    current_bet_tod = "Early Morning"
elif current_bet.hour <= 11:
    current_bet_tod = "Morning"
elif current_bet.hour == 12:
    current_bet_tod = "Noon"
elif current_bet.hour <= 15:
    current_bet_tod = "Afternoon"
elif current_bet.hour <= 20:
    current_bet_tod= "Evening"
elif current_bet.hour <= 23:
    current_bet_tod = "Night"


#Fernando de Noronha Time
timezone_fdnt = zoneinfo.ZoneInfo('Etc/GMT+2')
current_fdnt = datetime.datetime.now(tz=timezone_fdnt)

current_fdnt_tod = "error"
if current_fdnt.hour == 0:
    current_fdnt_tod = "Midnight"
elif current_fdnt.hour <= 5:
    current_fdnt_tod = "Early Morning"
elif current_fdnt.hour <= 11:
    current_fdnt_tod = "Morning"
elif current_fdnt.hour == 12:
    current_fdnt_tod = "Noon"
elif current_fdnt.hour <= 15:
    current_fdnt_tod = "Afternoon"
elif current_fdnt.hour <= 20:
    current_fdnt_tod= "Evening"
elif current_fdnt.hour <= 23:
    current_fdnt_tod = "Night"


#Eastern Greenland Time
timezone_egt = zoneinfo.ZoneInfo('Etc/GMT+1')
current_egt = datetime.datetime.now(tz=timezone_egt)

current_egt_tod = "error"
if current_egt.hour == 0:
    current_egt_tod = "Midnight"
elif current_egt.hour <= 5:
    current_egt_tod = "Early Morning"
elif current_egt.hour <= 11:
    current_egt_tod = "Morning"
elif current_egt.hour == 12:
    current_egt_tod = "Noon"
elif current_egt.hour <= 15:
    current_egt_tod = "Afternoon"
elif current_egt.hour <= 20:
    current_egt_tod= "Evening"
elif current_egt.hour <= 23:
    current_egt_tod = "Night"


#label for current time and date
label = tk.Label(
    text="Current date and time is: " + time_now.strftime("%y-%m-%d %H:%M:%S.") + " It's " + time_now_tod,
    fg="white",
    bg="black",
    width=50,
    height=5
)

# enables label
label.pack()

def press_current_time():
    label.config(text="Current date and time is: " + time_now.strftime("%y-%m-%d %H:%M:%S.") + " It's " + time_now_tod)

def press_utc():
    label.config(text="UTC date and time is: " + current_utc.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_utc_tod)

def press_cet():
    label.config(text="CET date and time is: " + current_cet.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_cet_tod)

def press_eet():
    label.config(text="EET date and time is: " + current_eet.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_eet_tod)

def press_eat():
    label.config(text="EAT date and time is: " + current_eat.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_eat_tod)

def press_st():
    label.config(text="SAMT date and time is: " + current_st.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_st_tod)

def press_plt():
    label.config(text="PLT date and time is: " + current_plt.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_plt_tod)

def press_bst():
    label.config(text="BST date and time is: " + current_bst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_bst_tod)

def press_vst():
    label.config(text="VST date and time is: " + current_vst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_vst_tod)

def press_ctt():
    label.config(text="CTT date and time is: " + current_ctt.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_ctt_tod)
    
def press_jst():
    label.config(text="JST date and time is: " + current_jst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_jst_tod)

def press_aet():
    label.config(text="AET date and time is: " + current_aet.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_aet_tod)

def press_sst():
    label.config(text="SST date and time is: " + current_sst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_sst_tod)

def press_nzst():
    label.config(text="NZST date and time is: " + current_nzst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_nzst_tod)

def press_mit():
    label.config(text="MIT date and time is: " + current_mit.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_mit_tod)

def press_hst():
    label.config(text="HST date and time is: " + current_hst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_hst_tod)

def press_ast():
    label.config(text="AST date and time is: " + current_ast.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_ast_tod)

def press_pst():
    label.config(text="PST date and time is: " + current_pst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_pst_tod)

def press_mst():
    label.config(text="MST date and time is: " + current_mst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_mst_tod)
    
def press_cst():
    label.config(text="CST date and time is: " + current_cst.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_cst_tod)  
      
def press_est():
    label.config(text="EST date and time is: " + current_est.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_est_tod)

def press_prt():
    label.config(text="PRT date and time is: " + current_prt.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_prt_tod)

def press_bet():
    label.config(text="BET date and time is: " + current_bet.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_bet_tod)    

def press_fdnt():
    label.config(text="FDNT date and time is: " + current_fdnt.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_fdnt_tod)

def press_egt():
    label.config(text="EGT date and time is: " + current_egt.strftime("%y-%m-%d %H:%M:%S.") + " It's " + current_egt_tod)


#buttons
button_utc = tk.Button(
    text="Current Time and Date",
    width=20,
    height=1,
    command=press_current_time).pack()



button_utc = tk.Button(
    text="Universal Coordinated Time",
    width=20,
    height=1,
    command=press_utc).pack()


button_utc = tk.Button(
    text="Centeral European Time",
    width=20,
    height=1,
    command=press_cet).pack()
    
button_utc = tk.Button(
    text="East European Time",
    width=20,
    height=1,
    command=press_eet).pack()

button_utc = tk.Button(
    text="East African Time",
    width=20,
    height=1,
    command=press_eat).pack()

button_utc = tk.Button(
    text="Samara Time",
    width=20,
    height=1,
    command=press_st).pack()

button_utc = tk.Button(
    text="Pakistan Lahore Time",
    width=20,
    height=1,
    command=press_plt).pack()

button_utc = tk.Button(
    text="Bangladesh Standard Time",
    width=20,
    height=1,
    command=press_bst).pack()

button_utc = tk.Button(
    text="Vietnam Standard Time",
    width=20,
    height=1,
    command=press_vst).pack()

button_utc = tk.Button(
    text="China Taiwan Time",
    width=20,
    height=1,
    command=press_ctt).pack()

button_utc = tk.Button(
    text="Japan Standard Time",
    width=20,
    height=1,
    command=press_jst).pack()

button_utc = tk.Button(
    text="Australian Eastern Time",
    width=20,
    height=1,
    command=press_aet).pack()

button_utc = tk.Button(
    text="Solomon Standard Time",
    width=20,
    height=1,
    command=press_sst).pack()

button_utc = tk.Button(
    text="New Zealand Standard Time",
    width=20,
    height=1,
    command=press_nzst).pack()

button_utc = tk.Button(
    text="Midway Islands Time",
    width=20,
    height=1,
    command=press_mit).pack()

button_utc = tk.Button(
    text="Hawaii Standard Time",
    width=20,
    height=1,
    command=press_hst).pack()

button_utc = tk.Button(
    text="Alaska Standard Time",
    width=20,
    height=1,
    command=press_ast).pack()

button_utc = tk.Button(
    text="Pacific Standard Time",
    width=20,
    height=1,
    command=press_pst).pack()

button_utc = tk.Button(
    text="Mountain Standard Time",
    width=20,
    height=1,
    command=press_mst).pack()
    
button_utc = tk.Button(
    text="Central Standard Time",
    width=20,
    height=1,
    command=press_cst).pack()

button_utc = tk.Button(
    text="Eastern Standard Time",
    width=20,
    height=1,
    command=press_est).pack()

button_utc = tk.Button(
    text="Peurto Rico Time",
    width=20,
    height=1,
    command=press_prt).pack()

button_utc = tk.Button(
    text="Brazil Eastern Time",
    width=20,
    height=1,
    command=press_bet).pack()

button_utc = tk.Button(
    text="Fernando de Noronha Time",
    width=20,
    height=1,
    command=press_fdnt).pack()

button_utc = tk.Button(
    text="Eastern Greenland Time",
    width=20,
    height=1,
    command=press_egt).pack()


window.mainloop()
