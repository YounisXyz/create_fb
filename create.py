import os,platform
os.system('git pull')
os.system('xdg-open https://youtube.com/@YounisXyz?si=q_OCozPQq1pLYzIp')
 
xyz=platform.architecture()[0]
if xyz=="32bit":
    print('\033[1;91mSorry Your Device Is 32bit,This Tool Is Only For 64bit, Please Upgrade Your Phone ....')
elif xyz=="64bit":
    __import__("Xyz_Create")
 
