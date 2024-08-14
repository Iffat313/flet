
#This script will use the flet library to create login app
 
#import the flet library
 
import flet as ft
 
#we use "ft.syntax" to grab a peice of code from the flet library.
 
#create a main function. Let us recall the syntax needed to create a function.
# The purpose is to hold the functionality and other buttons.
#  def function_name(parameter: data_type) -> return_type:
# """Docstring"""
#   body of the function
#   return expression
# Please keep in mind that data type is not required
 
#Page is a Tool from the flet library. As stated, Page is like a box or a container that contains all the controls and styles you want on
#the page. To make changes to the "Page", you have to use the properties and set values to those properties. The tools are considered as "Layouts"
def main(page: ft.Page) -> None:
   
 
    page.add( #anytime you want to add any other main tool besides page and use it's properties, what must come before is page.add
        ft.Row(
            [
                ft.Container( #afterwards you must do ft.maintool
                    alignment = ft.alignment.center, #because we created ft.container, notice how the properties underneath ARE NOT container.xyz. Therefore to use any main tools follow this template. "Page is an exception"
                    #image_src = "https://cdn.dribbble.com/users/1770290/screenshots/6183149/bg_79.gif",
                    #image_src = "https://media3.giphy.com/media/M8tZRmqgGUxfdCizH8/giphy.gif?cid=6c09b952p5otx25iaoa28p9nsrlty5m70of3v0c9q68qsxxt&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=s",
                    image_src = "https://www.qomplx.com/assets/images/careers/integrity-icon.gif?v=b1525ea9c0",
                    width = 100,
                    height = 100,
                )
            ],
            alignment = ft.MainAxisAlignment.CENTER,
        ),
    )
    #layouts require ft.
 
 
    #dictionary syntax, key/value pairs! The font format here is otf. Set the following
    page.fonts = {"SF":"https://github.com/sahibjotsaggu/San-Francisco-Pro-Fonts/blob/master/SF-Pro-Display-Regular.otf"}
   
   
    #title will appear on the top of the page
    page.title = "Welcome to the Grid!"
 
    #size but with a desktop only command. The app will appear through as a desktop app not a web browser app
    page.window_height = 750
    page.window_width = 750
 
    #make the page of the app appear in the middle of the screen
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
    #allow the user to scroll on the GUI
    page.scroll = "ScrollMode"
 
    #change the theme of the page
    page.theme_mode = "dark"
 
    #to add text to a page use the following code below
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
 
 
    page.controls.append(ft.Text("Before you enter the command line, tell us, who are you?"))
 
    #nested function used to create a textfield of a user
    def textbox_changed(e):
        t.value = e.control.value
        page.update()
 
    t = ft.Text() #t is the value (user's string) for input
    tb = ft.TextField( #tb is the value for the constant change in text from user
        #below are the properties of TextField
        label = "Enter Your Username:",
        on_change=textbox_changed
       
   
 
    )
   
 
    page.add(tb, t) #add the text and textfield to the page via their variables
 
 
    #Now create a password textbox
    #page.add(
        #PASS=ft.TextField(
           # label = "Enter in the Password:",  #one way to add containers and it's properties
           # password = True,
          #  can_reveal_password = True
        #)
   # )
 
    variable = ft.TextField(
        label = "Enter in the Password:",  #another way to add containers and it's properties, the difference is the variable usage.
        password = True,
        can_reveal_password = True,
    )
 
    page.add(variable)
 
    #function used to determine whether the user can hit the submit or reset button
    def visible(e):
        button_one.disabled = False #despite this variable being called when it's introduced below, it recognizes it!
        t.value = e.control.value
        page.update()
       
 
 
   
 
    #PART 1 IS ABOVE
    #QUE PART 2: THE BUTT ARC, this is where we implement functionality via buttons
 
 
    #create the functions needed for each button, this is the backend portion of the program
    def clear_form(e):
        t.value = ""
        tb.value = ""
        variable.value = ""
        #x = main
        page.update()
   
    #function for submission button, which creates a new page #************************
    def sub_form(e):
        page.clean()
 
        #function used to
        def on_submit_called(e):
            page.add(
                ft.Text(
                    "welcome",
                    color = ft.colors.BLUE,
                ),
 
               
            )
 
        #function for radio button (note: don't implement functions under page.add)
        def radio_button(e):
            page.add(
            ft.TextField(
                label = f"Enter your: {cg.value}",
                on_submit = on_submit_called,
            )
            )
            page.update()
       
        #this is the submit button that calls the function radio button
        b = ft.ElevatedButton( #b is a variable of the class ElevatedButton
            text = "submit",
            on_click = radio_button,
 
        )
 
        #this is the button themselves
        cg = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "Phone Number; press Enter when done", label = "Phone Number"),
                ft.Radio(value = "Email; press Enter when done", label = "Email")
            ])
        )
 
        page.title = "2FA Time!"
 
        page.add(
            ft.Row(
                [
                    ft.Container(
                        alignment = ft.alignment.center,
                        #image_src = "https://static.wikia.nocookie.net/fivenightsatfreddys/images/c/c2/Helpy.gif/revision/latest?cb=20180818182103",
                        image_src = "https://ps.w.org/sg-security/assets/icon-256x256.gif?rev=2971855",
                        width = 100,
                        height = 100,
                    )
 
                ],
                alignment = ft.MainAxisAlignment.CENTER
            ),
            ft.Text("welcome!"),
            ft.Text(
                t.value,
                size = 20,
                weight = "LARGE"
               
                ),
            ft.Text(
           
                "Using the checkbox below, use the appropriate 2FA method. Rates and SMS may apply!",
                weight = "LARGE",
                italic = True,
                    ),
            cg,
            b
           
           
        )
 
 
        page.update()
   
    #create a function that re-directs the user for a HPC account creation page
    def create_account(e):
        page.launch_url("https://csm.wayne.edu/CherwellPortal/IT?Locale=en-US&_=528a2a15")
        page.update()
 
 
    #function for submit button and setting the button to empty string
    t.value = ""
    page.update()
   
    button_one = ft.ElevatedButton(
        text = "submit",
        icon = "check",
        on_click = sub_form,
       
       
    )
 
    #Now that textfield for user is empty, the submit button will remain disabled.
    if t.value == "":
        button_one.disabled = True
        page.update()
   
   
    tb.on_change = visible
 
 
 
   
    #conditional statment for allowing button to be visibile or not.
    page.update()
 
   
    #function for reset button
    button_two = ft.ElevatedButton(
        text = "reset",
        on_click = clear_form,
        icon = "refresh"
    )
 
   
    button_three = ft.ElevatedButton(
        text = "create a new account",
        on_click = create_account
    )
 
    page.add(button_one,button_two,button_three)
   
 
   
 
 
   
 
    #The line below updates the page, without this line there will be 0 changes added to the page
    page.update()
 
   
 
 
ft.app(main)
 
 
    