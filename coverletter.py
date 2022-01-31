import datetime as dollarsigndate
import os

position = ""
company = ""
towhom = ""
tdate = dollarsigndate.datetime.today().strftime('%b %d %Y')
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')


def step1():
    global cl
    name = input("What is your name? ") or "Kyle Reneau"
    position = input("What position is this for? ") or "System Engineer"
    company = input("What company is this for? ")
    towhom = input("To whom may this concern? (default \"To Whom it may Concern)\": ") or "To Whom it may Concern"
    cl = (f"""{towhom}:
I am thrilled to be able to apply for the {position} position that you currently have at {company}. I can bring an extreme focus on my work and a keen and incisive analytical intelligence to the job. I am simply fascinated by the way in which computer systems and networks function, and I never tire of learning more about them. Motivated by this passionate interest, I believe that I can be a valuable addition to your team as I will not tire until I find the cleanest and most efficient solution to whatever problem is put before me.
I have experience designing, implementing and overseeing all aspects of computer systems to configuring routers, installing additional devices, designing encryption systems, collaborating with Systems Analysts to find and analyze data that might point to possible weaknesses in a network, monitoring and improving system performance and so on.
I am earnestly grateful to you for your time and consideration. I look forward to learning more about precisely what needs {company} has that I might be able to fulfill for you as a {position} and a trusted member of your team. As we move ahead through the hiring process, I will be excited to share and demonstrate my expertise to you and be of service.
    
Thank you for your time,

{name} {tdate}""")
    print(cl)

def check():
    correct = input("is this correct? Y or N: ")
    correct.lower

    if (correct[0] == "y"):
        file = open(f"{desktop}/Coverletter.txt", 'w')
        file.write(cl)
        file.close()
    else:
        main()

def main():
    step1()
    check()

main()