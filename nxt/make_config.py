##Source: https://github.com/Eelviny/nxt-python/blob/master/nxt/locator.py
##Raphael Holzer, 2018-04-27

import traceback, configparser, os

def make_config(confpath=None):
    conf = configparser.RawConfigParser()
    if not confpath: confpath = os.path.expanduser('~/.nxt-python')
    print("Welcome to the nxt-python config file generator!")
    print("This function creates an example file which find_one_brick uses to find a brick.")
    try:
        if os.path.exists(confpath): input("File already exists at %s. Press Enter to overwrite or Ctrl+C to abort." % confpath)
    except KeyboardInterrupt:
        print("Not writing file.")
        return
    conf.add_section('Brick')
    conf.set('Brick', 'name', 'MyNXT')
    conf.set('Brick', 'host', '54:32:59:92:F9:39')
    conf.set('Brick', 'strict', 0)
    conf.set('Brick', 'method', 'usb=True, bluetooth=False')
    conf.write(open(confpath, 'w'))
    print("The file has been written at %s" % confpath)
    print("The file contains less-than-sane default values to get you started.")
    print("You must now edit the file with a text editor and change the values to match what you would pass to find_one_brick")
    print("The fields for name, host, and strict correspond to the similar args accepted by find_one_brick")
    print("The method field contains the string which would be passed to Method()")
    print("Any field whose corresponding option does not need to be passed to find_one_brick should be commented out (using a # at the start of the line) or simply removed.")
    print("If you have questions, check the wiki and then ask on the mailing list.")
    
make_config()