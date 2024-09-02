def windows_banner():
    print("""

     __      __.__            .___                   
    /  \\    /  \\__| ____    __| _/______  _  ________
    \\   \\/\\/   /  |/    \\  / __ |/  _ \\ \\/ \\/ /  ___/
     \\        /|  |   |  \\/ /_/ (  <_> )     /\\___ \\ 
      \\__\\/  / |__|___|  /\\____ |\\____/ \\/\\_//____  >
           \\/          \\/      \\/                 \\/ 

    ----- * Meterpreter Stager Payloads * -----
      [1] payload/windows/x86/meterpreter/reverse_tcp
      [2] payload/windows/x64/meterpreter/reverse_tcp 
      [3] payload/windows/x86/meterpreter/reverse_http
      [4] payload/windows/x64/meterpreter/reverse_http  
      [5] payload/windows/x86/meterpreter/reverse_https
      [6] payload/windows/x64/meterpreter/reverse_https 

    ----- * Meterpreter Inline Payloads * -----
      [7] payload/windows/x86/meterpreter_reverse_tcp
      [8] payload/windows/x64/meterpreter_reverse_tcp  
      [9] payload/windows/x86/meterpreter_reverse_http
      [10] payload/windows/x64/meterpreter_reverse_http   
      [11] payload/windows/x86/meterpreter_reverse_https  
      [12] payload/windows/x64/meterpreter_reverse_https  

    ----- *  Shell  Stager  Payloads  * -----
      [13] payload/windows/x86/shell/reverse_tcp
      [14] payload/windows/x64/shell/reverse_tcp   

    ----- *  Shell  Inline  Payloads  * -----
      [15] payload/windows/x86/shell_reverse_tcp  
      [16] payload/windows/x64/shell_reverse_tcp

      [00] Back
    """)


# Define the payloads dictionary
win_payloads = {
    1: "windows/meterpreter/reverse_tcp",
    2: "windows/x64/meterpreter/reverse_tcp",
    3: "windows/meterpreter/reverse_http",
    4: "windows/x64/meterpreter/reverse_http",
    5: "windows/meterpreter/reverse_https",
    6: "windows/x64/meterpreter/reverse_https",
    7: "windows/meterpreter_reverse_tcp",
    8: "windows/x64/meterpreter_reverse_tcp",
    9: "windows/meterpreter_reverse_http",
    10: "windows/x64/meterpreter_reverse_http",
    11: "windows/meterpreter_reverse_https",
    12: "windows/x64/meterpreter_reverse_https",
    13: "windows/shell/reverse_tcp",
    14: "windows/x64/shell/reverse_tcp",
    15: "windows/shell_reverse_tcp",
    16: "windows/x64/shell_reverse_tcp"
}


def linux_banner():
    print("""

    .____    .__                     
    |    |   |__| ____  __ _____  ___
    |    |   |  |/    \\|  |  \\  \\/  /
    |    |___|  |   |  \\  |  />    < 
    |_______ \\__|___|  /____//__\\/__\\

    ----- * Meterpreter Stager Payloads * -----
      [1] payload/linux/x86/meterpreter/reverse_tcp
      [2] payload/linux/x64/meterpreter/reverse_tcp

    ----- * Meterpreter Inline Payloads * -----
      [3] payload/linux/x86/meterpreter_reverse_tcp
      [4] payload/linux/x64/meterpreter_reverse_tcp
      [5] payload/linux/x86/meterpreter_reverse_http
      [6] payload/linux/x64/meterpreter_reverse_http   
      [7] payload/linux/x86/meterpreter_reverse_https  
      [8] payload/linux/x64/meterpreter_reverse_https  

    ----- *  Shell  Stager  Payloads  * -----
      [9] payload/linux/x86/shell/reverse_tcp
      [10] payload/linux/x64/shell/reverse_tcp   

    ----- *  Shell  Inline  Payloads  * -----
      [11] payload/linux/x86/shell_reverse_tcp  
      [12] payload/linux/x64/shell_reverse_tcp

      [00] Back
    """)


# Define the payloads dictionary
linux_payloads = {
    1: "linux/x86/meterpreter/reverse_tcp",
    2: "linux/x64/meterpreter/reverse_tcp",
    3: "linux/x86/meterpreter_reverse_tcp",
    4: "linux/x64/meterpreter_reverse_tcp",
    5: "linux/x86/meterpreter_reverse_http",
    6: "linux/x64/meterpreter_reverse_http",
    7: "linux/x86/meterpreter_reverse_https",
    8: "linux/x64/meterpreter_reverse_https",
    9: "linux/x86/shell/reverse_tcp",
    10: "linux/x64/shell/reverse_tcp",
    11: "linux/x86/shell_reverse_tcp",
    12: "linux/x64/shell_reverse_tcp"
}


def android_banner():
    print("""

       _____              .___             .__    .___
      /  _  \\   ____    __| _/______  ____ |__| __| _/
     /  /_\\  \\ /    \\  / __ |\\_  __ \\/  _ \\|  |/ __ | 
    /    |    \\   |  \\/ /_/ | |  | \\(  <_> )  / /_/ | 
    \\____|___ /___|  /\\____ | |__|   \\____/|__\\____ | 

    ----- * Meterpreter Stager Payloads * -----
      [1] payload/android/meterpreter/reverse_tcp
      [2] payload/android/meterpreter/reverse_http
      [3] payload/android/meterpreter/reverse_https

    ----- * Meterpreter Inline Payloads * -----
      [4] payload/android/meterpreter_reverse_tcp 
      [5] payload/android/meterpreter_reverse_http
      [6] payload/android/meterpreter_reverse_https

    ----- *  Shell  Stager  Payloads  * -----
      [7] payload/android/shell/reverse_tcp
      [8] payload/android/shell/reverse_http
      [9] payload/android/shell/reverse_https 

      [00] Back
    """)


# Define the payloads dictionary
android_payloads = {
    1: "android/meterpreter/reverse_tcp",
    2: "android/meterpreter/reverse_http",
    3: "android/meterpreter/reverse_https",
    4: "android/meterpreter_reverse_tcp",
    5: "android/meterpreter_reverse_http",
    6: "android/meterpreter_reverse_https",
    7: "android/shell/reverse_tcp",
    8: "android/shell/reverse_http",
    9: "android/shell/reverse_https"
}


def php_banner():
    print("""

    __________  ___ ____________ 
    \\______   \\/   |   \\______  \\
     |     ___/   ---   \\     __/
     |    |   \\    Y    /    |    
     |____|    \\___|_  /|____|    
                     \\/           

    ----- * Meterpreter Stager Payloads * -----
      [1] payload/php/meterpreter/reverse_tcp   

    ----- * Meterpreter Inline Payloads * -----
      [2] payload/php/meterpreter_reverse_tcp

    ----- * PHP  Command Shell Payloads * -----
      [3] payload/php/reverse_php  


      [00] Back
    """)


# Define the payloads dictionary
php_payloads = {
    1: "php/meterpreter/reverse_tcp",
    2: "php/meterpreter_reverse_tcp",
    3: "php/reverse_php"
}


def encoder_banner():
    print("""

    ___________                       .___            
    \\_   _____/ ____   ____  ____   __| _/___________ 
     |    __)_ /    \\_/ ___\\/  _ \\ / __ |/ __ \\_  __ \\
     |        \\   |  \\  \\__(  <_> ) /_/ \\  ___/|  | \\/
     /_______  /___|  /\\___  >____/\\____ |\\___  >__|       

    ----- * Encoder for x86 payloads * -----
      [1] encoder/x86/shikata_ga_nai 
      [2] encoder/x86/xor_dynamic 
      [3] encoder/x86/alpha_mixed 
      [4] encoder/x86/unicode_mixed  
      [5] encoder/x86/jmp_call_additive

    ----- * Encoder for x64 payloads * -----
      [6] encoder/x64/zutto_dekiru 
      [7] encoder/x64/xor_dynamic
      [8] encoder/x64/xor_context 

      [00] Back
    """)


# Define the payloads dictionary
encoders = {
    1: "x86/shikata_ga_nai",
    2: "x86/xor_dynamic",
    3: "x86/alpha_mixed",
    4: "x86/unicode_mixed",
    5: "x86/jmp_call_additive",
    6: "x64/zutto_dekiru ",
    7: "x64/xor_dynamic",
    8: "x64/xor_context",
}


def keygen_banner():
    print("""
    
     ____  __.             ________               
    |    |/ _|____ ___.__./  _____/  ____   ____  
    |      <_/ __ <   |  /   \\  ____/ __ \\ /    \\ 
    |    |  \\  ___/\\___  \\    \\_\\  \\  ___/|   |  \\
    |____|__ \\___  > ____|\\______  /\\____ >___| _/
    
    Generate certificate for your APK payloads o=|=====>
    【1】 View Key
    【2】 Generate Key
    【3】 Delete Key
    
    【00】 Back
    """)


def keysign_banner():
    print("""
    
                   __                         __    
    _____  ______ |  | _____________    ____ |  | __
    \\__  \\ \\____ \\|  |/ /\\____ \\__  \\ _/ ___\\|  |/ /
     / __ \\|  |_> >    < |  |_> > __ \\  \\___|    < 
    (____  /   __/|__|_ \\|   __(____  /\\___  >__|_ \\
         \\/|__|        \/|__|       \/     \/     \/

    Generate certificate for your APK payloads o=|=====>
    
    【1】 Sign APK
    【2】 Verify APK
    
    【00】 Back
    """)
