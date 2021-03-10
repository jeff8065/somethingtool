#from selenium import webdriver
#from selenium.webdriver.opera.options import Options
from time import sleep
#driver = webdriver.Opera(executable_path=r'/usr/bin/operadriver')
#driver.get('opera://settings/privacy')
#driver.get('https://whatismyipaddress.com')
#sleep(10)
#driver.quit()


# Before running the code...
# 1. Set VPN function in Opera
# 2. Download Opera Webdriver from https://github.com/operasoftware/operachromiumdriver/releases
# 3. Type about://about in Opera and get profile path and installation path.
# 4. Set the variables.
# opera_profile = r"C:\profile path"
# options._binary_location = r"C:\\installation path."

from selenium import webdriver

#options = webdriver.ChromeOptions()
#opera_profile = r"/home/pega/.config/opera/"
#options.add_argument('user-data-dir=' + opera_profile)
#options._binary_location = r'/usr/bin/operadriver'
#driver = webdriver.Opera(options=options)

#driver.get('https://whatismyipaddress.com')
#html = driver.page_source
#print(html)
#sleep(10)
#driver.quit()



# The profile where I enabled the VPN previously using the GUI.
for i in range(3000): 
	opera_profile = '/home/pega/.config/opera/' 
	options = webdriver.ChromeOptions()
	options.add_argument('user-data-dir=' + opera_profile)
	driver = webdriver.Opera(options=options)
	driver.get('https://www.google.com/search?q=%E4%BD%B3%E9%8B%92%E5%86%B7%E6%B0%A3&oq=%E4%BD%B3%E9%8B%92%E5%86%B7%E6%B0%A3&aqs=chrome..69i57j0.28317j0j15&sourceid=chrome&ie=UTF-8')
	sleep(6)
	driver.get('https://www.google.com/search?q=%E4%BD%B3%E9%8B%92%E5%86%B7%E6%B0%A3&oq=%E4%BD%B3%E9%8B%92%E5%86%B7%E6%B0%A3&aqs=chrome..69i57j0.28317j0j15&sourceid=chrome&ie=UTF-8&tbs=lf:1,lf_ui:14&tbm=lcl&sxsrf=ALeKk03Y_9sCqwW6Nvty23FBN4JVNAh2cA:1615300690888&rflfq=1&num=10&rldimm=8326941079044138608&lqi=CgzkvbPpi5LlhrfmsKNaIAoO5L2zIOmLkiDlhrfmsKMiDuS9syDpi5Ig5Ya35rCjegblj7DljJeSARthaXJfY29uZGl0aW9uaW5nX2NvbnRyYWN0b3KqAQ4QASoKIgblhrfmsKMoRQ&ved=2ahUKEwjH3Ir_t6PvAhWEGaYKHXLWAXkQvS4wAHoECAIQLg&rlst=f#rlfi=hd:;si:8326941079044138608,l,CgzkvbPpi5LlhrfmsKNaIAoO5L2zIOmLkiDlhrfmsKMiDuS9syDpi5Ig5Ya35rCjegblj7DljJeSARthaXJfY29uZGl0aW9uaW5nX2NvbnRyYWN0b3KqAQ4QASoKIgblhrfmsKMoRQ;mv:[[25.3676477,121.5698504],[23.3579383,120.16067480000001]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3,lf:1,lf_ui:14')
	#html = driver.page_source
	#print(html)
	sleep(6)
	driver.get('https://www.google.com/maps/place/%E4%BD%B3%E9%8B%92%E5%B7%A5%E7%A8%8B%E8%A1%8C/@25.2599847,121.4921702,17z/data=!3m1!4b1!4m5!3m4!1s0x3442b77b44f2270f:0x738f3ccb1a08a670!8m2!3d25.2599847!4d121.4943589')
	#html = driver.page_source
	#print(html)
	sleep(6)
	driver.get('https://www.google.com/maps/place/%E4%BD%B3%E9%8B%92%E5%B7%A5%E7%A8%8B%E8%A1%8C/@25.2599847,121.4943589,3a,75y/data=!3m8!1e2!3m6!1sAF1QipPN86bIm3cclj1DFaJ7VG-igVBGqEUgJIg_krRA!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPN86bIm3cclj1DFaJ7VG-igVBGqEUgJIg_krRA%3Dw397-h298-k-no!7i1478!8i1108!4m7!3m6!1s0x3442b77b44f2270f:0x738f3ccb1a08a670!8m2!3d25.2599847!4d121.4943589!14m1!1BCgIgAQ')
	sleep(6)
	
	driver.quit()
	print(i)
#1. Go to https://github.com/operasoftware/operachromiumdriver/releases
#2. Right click on  operadriver_linux64.zip 
#3. Copy link address 
#4. Open Terminal 
#5. type wget https://github.com/operasoftware/operachromiumdriver/releases/download/v.78.0.3904.87/operadriver_linux64.zip (this is the address you copied before)
#6. unzip operadriver_linux64.zip
#7. sudo mv operadriver /usr/bin/operadriver
#8. sudo chown root:root /usr/bin/operadriver
#9. sudo chmod +x /usr/bin/operadriver
#10. Verify it is correct installation by typing... which operadriver (you should get the path like usr/bin/operadriver.



