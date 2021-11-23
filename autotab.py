import webbrowser as wb

browser = None  #change this to your desired browser, or else default browser will be used
w = wb.get(using=browser)

try:
    with open('sitelist.txt') as f:  #opens sitelist for parsing
        site_list = f.readlines()
    try:
        first_site = site_list[0]
        w.open(first_site, new=1) #opens first site in a new window
    except:
        print("Site list is empty. Add some sites to open :)")
    for i in site_list[1:]:  #opens all other sites in previously opened window
        w.open_new_tab(i)
except:
    print("Ensure that file sitelist.txt is available in the working directory.")
#end
