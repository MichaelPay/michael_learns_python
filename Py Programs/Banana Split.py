available = "banana split;hot fudge;cherry;malted;black and white"
available.split(';')
sundaes = available.split(';')
menu = "Our available flavors are: {}."
", ".join(sundaes)
display_menu = sundaes
menu.format(display_menu)