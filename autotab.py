import webbrowser as wb

browser = None
w = wb.get(using=browser)

try:
    with open('sitelist.txt') as f:
        site_list = f.readlines()
    try:
        first_site = site_list[0]
        w.open(first_site, new=1)
    except:
        print("Site list is empty. Add some sites to open :)")
    for i in site_list[1:]:
        w.open_new_tab(i)
except:
    print("Ensure that file sitelist.txt is available in the working directory.")



