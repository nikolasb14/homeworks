# შექმენით თქვენი რაზმელებისგან სია, ამოირჩიეთ რენდომულად 3 ბავშვი და მიუწერეთ გვერდში "კარგად სწავლობს"

import random

crew_members = ['ლაზარე ღოღობერიძე', 'ლუკა თელია', 'ლექსო პატარაია', 'თორნიკე ქარელიძე', 'ნინო ოჩიგავა', 'ლუკა გამრეკლიძე', 'ნიკო ქუთათელაძე', 'ნიკოლას ბობოხიძე',]

for i in range(1, 4):
    winner = random.choice(crew_members)
    print(winner, "კარგად სწავლობს")
    crew_members.remove(winner)


crew_members_name = ['ლაზარე', 'ლუკა', 'ლექსო', 'თორნიკე', 'ნინო', 'ლუკა', 'ნიკო', 'ნიკოლას',]

if crew_members_name[-1] == "ი":
    print("cool")
else:
    print('No ones name ended with "ი", but they are cool anyways')


