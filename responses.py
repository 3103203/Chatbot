import random

R_ADVICE= "\n If you want more information then visit our website https://krct.ac.in/index.php \n or \n make a call for principle office the number is : 8978690812"
R_EATING = "\nI am a chat bot and i am work for educational instutes to help strangers to clearyfy their queries based on instutes"
R_RANK="\n K. Ramakrishnan College of Technology NIRF Ranking 2022 is 251-300 for B Tech. \n In 2020, India Today Survey ranked 194th place for B Tech. \n KRCE Ranking in Tamil Nadu is 24th among Top Engineering Colleges. \n The WEEK Survey ranked 152nd for B Tech in 2020."
R_DEPT="\n CIVIL ENGINEERING \n COMPUTER SCIENCE AND ENGINEERING \n ELECTRICAL AND ELECTRONICS ENGINEERING \n ELECTRONICS AND COMMUNICATION ENGINEERING \n MECHANICAL ENGINEERING \n SCIENCE AND HUMANITIES \n PHYSICAL EDUCATION \n ARTIFICIAL INTELLIGENCE"
R_degree="\n BE \n B.Tech \n ME \n Ph.D"
R_cutoff="\n totat 200 marks((physics+chemistry/2)+maths) \n CIVIL ENGINEERING - above 100 \n COMPUTER SCIENCE AND ENGINEERING - above 120 \n ELECTRICAL AND ELECTRONICS ENGINEERING - above 100 \n ELECTRONICS AND COMMUNICATION ENGINEERING - above 110 \n MECHANICAL ENGINEERING - above 90\n SCIENCE AND HUMANITIES - above 120\n PHYSICAL EDUCATION - above 100 \n ARTIFICIAL INTELLIGENCE - above 130"
R_tution="\n     Councling fee: \n\n BE- 65000 per year \n B.Tech - 65000 per year \n ME - 30000 per year \n\n    Managment fee: \n\n BE- 80000 per year \n B.Tech - 80000 per year \n ME - 50000 per year"
R_hostal="\n Roomrent : 2000 per month \n Mess : 4500 per month \n per room four members are allowed \n hostal timing : morning-06:00 to evening-08:00"
R_cantien="\n IN our college there are 4 - cantiens are avaliable \n veg , non-veg , north-indian , tea-cantien"
R_location="\n State - Tamilnadu \n District - Trichy \n City - Samiyapuram \n pincode - 621112 \n near kariamanikam road"
R_placement="\n IN our college 85-90 percent of students got placed. \n Highest package- 12 lpa, lowest package-3 lpa and average package-5 lpa. \n Zoho, Amazon, Wipro, Infosys are the top recruiting companies of my course."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
