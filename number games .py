
l1=["In this game you have to choose a number between 1 to 1000 . So your probability of winning is 0.1%. It might be a fun way to see how many times it will take for you to guess the correct number.But the number will change everytime you put another number", "Choose a number between 1 to 1000 : ",
      "Looks like you got lucky for no reason. Yeap the number was:",
      "Nope,The number was :"  ]

l2=["If you know the math about probability then you might know that the probability of 0.1% means that out of 1000 tries you will win once. So you might expect to put the number at least 1000 times to win once.",
    "0.1% doesn't always meant that it will take you 1000 tries to win it may take more or less who knows.",
    "One of the greatest reason I hate probability that the result also unpredictable .",
    "Probability is some kind of math that won't give you any solid answer .But physics says you could predict the solid answer if you know the value of all the variables acting upon a force but those variables are alot and counting them would take a lot of time and also they changes overtime .So, you also need to find their rate of changes by using constants of the scientific calculations .But I am afraid science haven't discovered all the universal constants beside light speed (C)",
    "The main reason I love programming because it is an art not some messy words .","Just like a normal man won't understand why Monalisa is priceless , a nonprogrammer won't understad the beauty of programming as same as I don't understand the beauty of Flowers .",
    "The reason I started with python because it is easy to learn.",
    "Do you know that programming has a phrase called beautiful code?",
    "Sometimes I think my whole life could be better .Then I remember that those bad moments might be the reasons I can feel how happiness feels like.",
    "That might be my 1st python project I will publish on internet .",
    "I don't know why I am writing these random facts .Maybe because I am bored ."
    ]

import random

print(l1[0])

while True:

    x=int(input(l1[1]))
    y=random.randint(1,1000)
    if x==y:
        print(l1[2],y)
    else:
        print(l1[3],y)

    print(random.choice(l2))
         