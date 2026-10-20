from pyscript import display, document

def add_member(e):
    document.getElementById("output1").innerHTML = ""
    
    names = {'Pio Oquendo', 'Gian Ibit', 'Keisha Valiente', 'Mira Gille', 'Cameron Bufford'}
    
    input_name1 = document.getElementById("name1").value
    input_name2 = document.getElementById("name2").value

    #assign the value to set variables
    new_name_set ={input_name1 + " " + input_name2}  

    all_names = names | new_name_set

    total_names = len(names | new_name_set)

    #display the items in ascending order (A-Z) seperated by br
    name_list = "<br>".join(sorted(all_names))

    #display
    document.getElementById("output1").innerHTML = f'All Members: <br> {name_list}'
    display(f'Total Members: {total_names}', target = "output1")