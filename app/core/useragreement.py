from  tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from app.core.appvectors import *


aggrements='''SOFTWARE LICENSE AGREEMENT

This Software License Agreement ("Agreement") is entered into by and between [Your Company Name], a company organized and existing under the laws of [Your Country/State], with its principal place of business at [Your Address] ("Licensor"), and the user of the software ("Licensee").

1. LICENSE GRANT

Subject to the terms and conditions of this Agreement, Licensor hereby grants Licensee a [non-exclusive, non-transferable, revocable] license to use the software ("Software") provided by Licensor, including any updates and modifications, solely for Licensee's internal business purposes.

2. RESTRICTIONS

Licensee shall not:
- Modify, adapt, or create derivative works of the Software.
- Reverse engineer, decompile, or disassemble the Software.
- Remove or alter any copyright, trademark, or other proprietary notices from the Software.
- Rent, lease, sublicense, or otherwise transfer the Software to any third party.

3. OWNERSHIP

Licensor retains all right, title, and interest in and to the Software, including all intellectual property rights therein. This Agreement does not grant Licensee any ownership rights in the Software.

4. SUPPORT AND MAINTENANCE

Licensor may, at its sole discretion, provide support and maintenance services for the Software. Licensee acknowledges that any such services are provided on an "as-is" basis, and Licensor makes no warranties or representations regarding the availability or quality of such services.

5. DISCLAIMER OF WARRANTIES

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL LICENSOR BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

6. TERMINATION

This Agreement shall remain in effect until terminated by either party. Licensor may terminate this Agreement immediately upon written notice if Licensee breaches any term or condition of this Agreement. Upon termination, Licensee shall cease all use of the Software and destroy all copies thereof.

7. MISCELLANEOUS

This Agreement constitutes the entire agreement between the parties concerning the subject matter hereof and supersedes all prior agreements and understandings, whether written or oral, relating to such subject matter. This Agreement may be amended only by a written instrument signed by both parties. This Agreement shall be governed by and construed in accordance with the laws of [Your Jurisdiction]. Any dispute arising under or in connection with this Agreement shall be subject to the exclusive jurisdiction of the courts located in [Your Jurisdiction].

IN WITNESS WHEREOF, the parties hereto have executed this Agreement as of the Effective Date.

[Your Company Name]

By: _______________________
Name: _____________________
Title: ______________________
Date: ______________________

Licensee

By: _______________________
Name: _____________________
Title: ______________________
Date: ______________________

'''






class UserAgreementWindow:
    def __init__(self, root , aggrement_text ) -> None:
        self.show_first_time_trail_message = False
        self.root = root
        self.aggrement_text_file = aggrement_text



       


        # self.top_level.geometry('450x300')
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
        top_level_height = 300  # Set your desired height
        top_level_x = (center_x - top_level_width // 2) - 8
        top_level_y = (center_y - top_level_height // 2) - 50



        self.top_level = Toplevel(self.root)

        


        # Set the geometry of the top-level window to be centered
        self.top_level.geometry(f"{top_level_width}x{top_level_height}+{top_level_x}+{top_level_y}")


        def disable_close():
            self.root.destroy()
            pass  # This function does nothing, effectively disabling the close button

        
        self.top_level.title("User terms agreement")
    
        # Make the top-level window modal
        self.top_level.grab_set()
        # Make a beep when the main window is selected while the top-level window is opening
        
        # def ring_bell(e):
        #     print('---')
        #     self.root.bell()

        # self.root.bind("<Button-1>", ring_bell)
        self.top_level.resizable(False, False)
        # self.root.attributes('-topmost', True) 
        # self.top_level.attributes('-topmost', True) 
        self.top_level.protocol("WM_DELETE_WINDOW", disable_close)

        self.top_level.iconphoto(False, APP_VECT.get('appicon',(16,16)))



        #?--
        Label(self.top_level,padx=8, border=0, borderwidth=0, highlightthickness=0).pack()
        
        self.aggrement_texts_frame =  Frame(self.top_level ,border=0, borderwidth=0, highlightthickness=0)
        self.aggrement_texts_frame.pack(expand=True,fill=X)
        
        self.decision_frame =  Frame(self.top_level ,pady=10, border=0, borderwidth=0, highlightthickness=0)
        self.decision_frame.pack(expand=True,fill=X)


        #?--
        #Left Margin
        Label(self.aggrement_texts_frame,padx=8, border=0, borderwidth=0, highlightthickness=0).pack(side=LEFT)
        self.aggrement_text = scrolledtext.ScrolledText(self.aggrement_texts_frame, width=150, height=14, wrap=WORD, font=('Roboto', 10))
        self.aggrement_text.insert(INSERT, self.aggrement_text_file)
        self.aggrement_text.pack(side=LEFT)
        self.aggrement_text.configure(state='disabled')
        self.aggrement_text.bind('<MouseWheel>', self.on_scroll)


        #?--
        #Left Margin
        Label(self.decision_frame,padx=8, border=0, borderwidth=0, highlightthickness=0).pack(side=LEFT)
        # Create checkbox for agreeing to terms
        self.checkbox_boolVar = BooleanVar()
        self.checkbox_boolVar.set(False)
        self.agree_checkbox = ttk.Checkbutton(self.decision_frame, text="I agree to the terms and conditions", variable=self.checkbox_boolVar, state=DISABLED, command=self.agree_checkbox_state)
        self.agree_checkbox.pack(side=LEFT)
        # Right Margin
        Label(self.decision_frame,padx=8, border=0, borderwidth=0, highlightthickness=0).pack(side=RIGHT)
        # Create button to confirm agreement
        self.next_btn = ttk.Button(self.decision_frame, text="Next", state=DISABLED, command=self.next_btn_click)
        self.next_btn.pack(side=RIGHT)
        # Create button to confirm agreement
        self.cancel_btn = ttk.Button(self.decision_frame, text="Cancel", state=NORMAL, command=self.cancel_btn_click      )
        self.cancel_btn.pack(side=RIGHT)



    def trail_info_only_first_time(self):
        messagebox.showinfo("Licence", "Congratulations! You have received a five-day trial period. Enjoy all the access to the product.")
        
    def on_scroll(self,e):
        # Get the current position of the scrollbar
        scroll_position = self.aggrement_text.yview()[1]
        # print(scroll_position)

        if scroll_position == 1.0:
            self.agree_checkbox['state'] = NORMAL            
            self.next_btn['state'] = DISABLED
        else:            
            self.checkbox_boolVar.set(False)
            self.cancel_btn['state'] = NORMAL
            self.agree_checkbox['state'] = DISABLED

    
    def agree_checkbox_state(self):
        if self.checkbox_boolVar.get():
            self.next_btn.config(state=NORMAL)
            self.cancel_btn['state'] = DISABLED
        else:
            self.next_btn.config(state=DISABLED)
            self.cancel_btn['state'] = NORMAL

    def cancel_btn_click(self):
        self.root.destroy()

    def next_btn_click(self):
        # self.root.attributes('-topmost', False) 
        # self.top_level.attributes('-topmost', False) 
        # self.root.unbind("<Button-1>")
        self.top_level.grab_release()
        self.top_level.destroy()
        if self.show_first_time_trail_message : self.trail_info_only_first_time()




if __name__ == '__main__':
    root = Tk()
    root.title("User Agreement")


    def popup():
        UserAgreementWindow(root,aggrement_text= aggrements)

    Button(root,text='Click to popup' ,command=popup).pack()
    root.geometry('500x500')
    root.mainloop()