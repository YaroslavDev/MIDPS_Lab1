from subprocess import call
import subprocess
import smtplib
import getpass

#Email data
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'rapyorock@gmail.com'
password = 'blah-blah'
recipent = 'rapyorock@gmail.com'
subject = 'Lab1_Maker compilation errors!'
body = """This message was generated automatically. Do not respond to it!<br>
          Following compilation errors had place:<br>"""

print "MIDPS Lab1 Maker runned..."
success_flag = 0;
#========================================================
#Python
print "==================================="
print "Python script execution..."
proc = subprocess.Popen(["python", "python/hello.py"], stderr=subprocess.PIPE)
python_errs = proc.stderr.read()
if python_errs:
    print "Python execution errors:\r\n", python_errs
    success_flag += 1
else:
    print "Execution succeded!"
print "==================================="
#=========================================================
#Ruby
print "Ruby script execution..."
proc = subprocess.Popen(["ruby", "ruby/hello.rb"],stderr=subprocess.PIPE)
ruby_errs = proc.stderr.read()
if ruby_errs:
    print "Ruby execution errors:\r\n", ruby_errs
    success_flag += 1
else:
    print "Execution succeeded!"
print "==================================="
#=========================================================
#C
print "C compiling via gcc..."
proc=subprocess.Popen(['gcc', 'c/hello.c', '-o', 'hello'],stderr=subprocess.PIPE)
c_errs = proc.stderr.read()
if c_errs:
    print "C compilation errors:\r\n", c_errs
    success_flag += 1
else:
    print "Compilation succeeded!"
    print "C program execution..."
    if call(["c/hello"]):
        print "Execution failed!"
        success_flag += 1
    else:
        print "Execution succeeded!"
print "==================================="
#=========================================================
#C++
print "C++ compiling via g++..."
proc =  subprocess.Popen(["g++", "-o", "hello", "cpp/hello.cpp"], stderr=subprocess.PIPE)
cpp_errs = proc.stderr.read()
if cpp_errs:
    print "Cpp compilation errors:\r\n", cpp_errs
    success_flag += 1
else:
    print "Compilation succeeded!"
    print "C++ program execution..."
    if call(["cpp/hello"]):
        print "Execution failed!"
        success_flag += 1
    else:
        print "Execution succeeded!"
print "==================================="
#=========================================================
#Java
print "Java compiling via javac..."
proc = subprocess.Popen(["javac", "java/hello.java"], stderr=subprocess.PIPE)
java_errs = proc.stderr.read()
if java_errs:
    print "Java compilation errors:\r\n", java_errs
    success_flag += 1
else:
    print "Compilation succeeded!"
    print "Java program execution via java"
    if call(["java", "--cp", "java", "HelloWorld"]):
        print "Exectuion failed!"
        success_flag += 1
    else:
        print "Execution succeeded!"
print "==================================="
#=====================================================
if success_flag:
    print "Errors occured during script execution!"
    print "Sending report to rapyorock@gmail.com"
    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo
    password = getpass.getpass("Email password: ")
    #password = raw_input("Email Password: ")
    session.login("rapyorock@gmail.com", password)
    headers = ["from: " + sender,
               "subject: " + subject,
               "to: " + recipent,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    
    if python_errs:
        body = body + "<b>Python errors:</b><br>" + python_errs + "<br>"
    if ruby_errs:
        body = body + "<b>Ruby errors:</b><br>" + ruby_errs + "<br>"
    if c_errs:
        body = body + "<b>C errors:</b><br>" + c_errs + "<br>"
    if cpp_errs:
        body = body + "<b>Cpp errors:</b><br>" + cpp_errs + "<br>"
    if java_errs:
        body = body + "<b>Java errors:</b><br>" + java_errs + "<br>"

    session.sendmail(sender, 
                     recipent, 
                     headers + "\r\n\r\n" + body)
    session.quit()
else:
    print "Ready for commit!"
    print "Commiting..."
    call(["git", "commit", "-a", "-m", "Successfully compiled programs!"])
print "Lab1_maker finished execution!"

