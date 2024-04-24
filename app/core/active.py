import hmac
import hashlib
from datetime import datetime
from tkinter import *
from tkinter import ttk
import re
try:
    from app.core.appvectors import *
except:
    pass




def convert_and_validate_date(input_date):
    try:
        # Convert input date string to datetime object
        date_obj = datetime.strptime(input_date, '%d/%m/%Y')

        # Check if the date is valid
        if date_obj.year < 1000 or date_obj.year > 9999:
            return None

        # Format the date as DDMMYYYY
        formatted_date = date_obj.strftime('%d%m%Y')

        return formatted_date
    except ValueError:
        return None
    
def generaor(expaire_date,serial_number):
    # Secret key
    secret_key = b'*#%$!&'
    # Message
    message = b'@#$~~@#$'

    expaire_date  = str(convert_and_validate_date(str(expaire_date).strip()))
    serial_number = str(serial_number).strip()
    if len(serial_number)<8: serial_number = serial_number.rjust(8,'0')

    message_ = f'{expaire_date}_{serial_number}'

    # Calculate HMAC-SHA256 hash
    hmac_hash = hmac.new(secret_key, message, hashlib.sha1).hexdigest()
    print(hmac_hash)

    generatd_key = ''
    par_four = ''
    count = 0
    for index,character in enumerate(hmac_hash[:32]):
        index = index+1
        par_four += character
        if (index) % 4 == 0 and (index != len(hmac_hash)):
            generatd_key += message_.split('_')[0][count]+par_four +message_.split('_')[1][count]
            if index != 32 :
                generatd_key +=  '-'
            par_four = ''
            count += 1
    print('>>',generatd_key.upper())


    return generatd_key.upper()





# #todo reconstraction
# def reconstract_licence(generatd_key):
#     # Secret key
#     secret_key = b'*#%$!&'
#     # Message
#     message = b'@#$~~@#$'


#     date = ''
#     serial = ''
#     hash_val = ''

#     reconst = generatd_key.lower().split('-')
#     for each_segment in reconst:
#         date += each_segment[0]
#         serial += each_segment[-1]
#         hash_val += each_segment[1:-1]


#     print(date)
#     print(serial)
#     print(hash_val)
        
#     provided_hmac_hash = hash_val
#     calculated_hmac_hash = hmac.new(secret_key, message, hashlib.sha1).hexdigest()[:32]
#     if provided_hmac_hash == calculated_hmac_hash:
#         print("Message is authentic.")
#     else:
#         print("Message is not authentic.")



# reconstract_licence(generatd_key)















class LicenceActivation:
    def __init__(self,root) -> None:
        self.root = root
        pass


    def first_time(self):
        ...

    def licence_key_activation_window(self):

        # Calculate the center coordinates of the root window
        self.root.update_idletasks()  # Update the window dimensions
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        center_x = root_x + root_width // 2
        center_y = root_y + root_height // 2

        # Calculate the position for the top-level window to be centered
        top_level_width = 450  # Set your desired width
        top_level_height = 300-150  # Set your desired height
        top_level_x = (center_x - top_level_width // 2) - 8
        top_level_y = (center_y - top_level_height // 2) - 50



        self.top_level = Toplevel(self.root)
        # Set the geometry of the top-level window to be centered
        self.top_level.geometry(f"{top_level_width}x{top_level_height}+{top_level_x}+{top_level_y}")
        self.top_level.title("License Activation")
        self.top_level.resizable(False, False)
        # Make the top-level window modal
        self.top_level.grab_set()
        self.root.attributes('-topmost', True) 
        self.top_level.attributes('-topmost', True) 
        self.top_level.iconphoto(False, APP_VECT.get('appicon',(16,16)))




        # Make a beep when the main window is selected while the top-level window is opening
    
        def ring_bell(e):
            # print('---')
            self.root.bell()

        self.root.bind("<Button-1>", ring_bell)


        def disable_close():
            self.root.attributes('-topmost', False) 
            self.top_level.attributes('-topmost', False) 
            self.top_level.destroy()
        self.top_level.protocol("WM_DELETE_WINDOW", disable_close)



        self.licence_key_frame =  Frame(self.top_level ,border=0, borderwidth=0, highlightthickness=0)
        self.licence_key_frame.pack(expand=True,fill=Y)

        # Entry(self.licence_key_frame).pack()
        self.licence_key_entry = ttk.Entry(self.licence_key_frame,width=57)
        self.licence_key_entry.pack(side=LEFT)

        self.check_licence_key_btn = ttk.Button(self.licence_key_frame, text='Activate' ,command=self.check_licence_key)
        self.check_licence_key_btn.pack(side=LEFT)

    def check_licence_key(self):      
        pattern = re.compile(r'\b\d\w{4}\d\b(?:-\d\w{4}\d\b){7}')
        inputed_licence = str(self.licence_key_entry.get()).strip()
        if pattern.fullmatch(inputed_licence):
            print("Valid format")
            self.reconstract_licence(inputed_licence)
        else:
            print("Invalid format")
        
        

    #todo reconstraction
    def reconstract_licence(self,generatd_key):
        # Secret key
        secret_key = b'*#%$!&'
        # Message
        message = b'@#$~~@#$'


        date , serial , hash_val= ['','','']
   

        reconst = generatd_key.lower().split('-')
        for each_segment in reconst:
            date += each_segment[0]
            serial += each_segment[-1]
            hash_val += each_segment[1:-1]


        print(date)
        print(serial)
        print(hash_val)
            
        provided_hmac_hash = hash_val
        calculated_hmac_hash = hmac.new(secret_key, message, hashlib.sha1).hexdigest()[:32]
        if provided_hmac_hash == calculated_hmac_hash:

            #! if self.days_left(date)
            
            print("Message is authentic.")
            self.licence_key_entry['state'] = DISABLED
            self.check_licence_key_btn['state'] = DISABLED
            self.check_licence_key_btn['text'] = 'Activated'

            print('[1] -- >> >')
            self.appmenu.is_running_trail = False
            self.appmenu.update_activation_date(f'{self.days_left(date)} days left')
            #!need to add a loader
            self.top_level.destroy()
            # self.root.unbind("<Button-1>")

        else:
            self.licence_key_entry['state'] = NORMAL
            self.check_licence_key_btn['state'] = NORMAL
            self.check_licence_key_btn['text'] = 'Activate'
            print("Message is not authentic.")

    

    

    def days_left(self,date_str):
        try:
            # Convert the input date string to a datetime object
            date = datetime.strptime(date_str, '%d%m%Y')
            # Get today's date
            today = datetime.now()

            # Check if the given date is before today
            if date < today:
                return False

            # Calculate the difference in days
            delta = date - today
            return delta.days
        except ValueError:
            # If the input date is invalid
            return False

    # # Example usage:
    # input_date = '01052024'  # Example date in DDMMYYYY format
    # result = days_left(input_date)
    # if result is False:
    #     print("Invalid date or date is in the past.")
    # else:
    #     print("Days left until the given date:", result)



    def get_menu_class(self,appmenu):
        self.appmenu = appmenu






if __name__ == '__main__':
    # root = Tk()

    # def  a():
    #     LicenceActivation(root).licence_key_activation_window()

    # Button(root,text='check',command=a).pack()
    # root.geometry('600x600')
    # root.mainloop()


    # 395660-01B840-10B950-24FB40-297FF0-02B350-271C05-4FCAE6
    # 395660-01B840-10B950-24FB40-297FF0-02B350-371C05-0FCAE6

    generatd_key = generaor('30/12/2030','56')