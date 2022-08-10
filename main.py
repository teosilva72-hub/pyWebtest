
#py .\main.py < execute/run
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get("http://172.20.10.227/admin/config.php")
login = web.find_element(By.ID, "login_admin")
login.click()

sleep(2)

web.execute_script("""
        let form = document.getElementById('loginform');
        let user = form.querySelector("[name=username]");
        let passw = form.querySelector("[name=password]");

        user.value = 'admin';
        passw.value = 'R0d0v14s';

        form.submit();
    """)


sleep(2)

for num in range(0, 206):
    web.get("http://172.20.10.227/admin/config.php?display=extensions&tech_hardware=pjsip_generic")
    
    sip = 1000 + num

    ramal = web.find_element(By.ID, "extension")
    ramal.send_keys(sip)

    name = web.find_element(By.ID, "name")
    name.send_keys(sip)

    web.execute_script(f"""
        let passw = document.getElementById('devinfo_secret');

        passw.value = 'Sip{sip}';
    """)

    submit = web.find_element(By.ID, "submit")
    submit.click()

web.close()