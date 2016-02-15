import random
import os

def insultMe(num=1, Speak=False):
      adj="""
      aggressive
      aloof
      arrogant
      belligerent
      big-headed
      bitchy
      boastful
      bone-idle
      boring
      bossy
      callous
      cantankerous
      careless
      changeable
      clinging
      compulsive
      conservative
      cowardly
      cruel
      cunning
      cynical
      deceitful
      detached
      dishonest
      dogmatic
      domineering
      finicky
      flirtatious
      foolish
      foolhardy
      fussy
      greedy
      grumpy
      gullible
      harsh 
      impatient
      impolite
      impulsive
      inconsiderate
      inconsistent
      indecisive
      indiscreet
      """

      noun="""
      Alcoholic
      Amateur
      Analphabet
      Anarchist
      Ape
      Arse
      Arselicker
      Ass
      Ass master
      Ass-kisser
      Ass-nugget
      Ass-wipe
      Asshole
      Baby
      Backwoodsman
      Balls
      Bandit
      Barbar
      Bastard
      Bastard
      Beavis
      Beginner
      Biest
      Bitch
      Blubber gut
      Bogeyman
      Booby
      Boozer
      Bozo
      Brain-fart
      Brainless
      Brainy
      Brontosaurus
      Brownie
      Bugger
      Bugger, silly
      Bulloks
      Bum
      Bum-fucker
      Butt
      Buttfucker
      Butthead
      Callboy
      Callgirl
      Camel
      Cannibal
      Cave man
      Chaavanist
      Chaot
      Chauvi
      Cheater
      Chicken
      Children fucker
      Clit
      Clown
      Cock
      Cock master
      Cock up
      Cockboy
      Cockfucker
      Cockroach
      Coky
      Con merchant
      Con-man
      Country bumpkin
      Cow
      Creep
      Creep
      Cretin
      Criminal
      Cunt
      Cunt sucker
      Daywalker
      Deathlord
      Derr brain
      Desperado
      Devil
      Dickhead
      Dinosaur
      Disguesting packet
      Diz brain
      Do-Do
      Dog
      Dog, dirty
      Dogshit
      Donkey
      Drakula
      Dreamer
      Drinker
      Drunkard
      Dufus
      Dulles
      Dumbo
      Dummy
      Dumpy
      Egoist
      Eunuch
      Exhibitionist
      Fake
      Fanny
      Farmer
      Fart
      Fart, shitty
      Fatso
      Fellow
      Fibber
      Fish
      Fixer
      Flake
      Flash Harry
      Freak
      Frog
      Fuck
      Fuck face
      Fuck head
      Fuck noggin
      Fucker
      Gangster
      Ghost
      Goose
      Gorilla
      Grouch
      Grumpy
      Head, fat
      Hell dog
      Hillbilly
      Hippie
      Homo
      Homosexual
      Hooligan
      Horse fucker
      Idiot
      Ignoramus
      Jack-ass
      Jerk
      Joker
      Junkey
      Killer
      Lard face
      Latchkey child
      Learner
      Liar
      Looser
      Lucky
      Lumpy
      Luzifer
      Macho
      Macker
      Man, old
      Minx
      Missing link
      Monkey
      Monster
      Motherfucker
      Mucky pub
      Mutant
      Neanderthal
      Nerfhearder
      Nobody
      Nurd
      Nuts, numb
      Oddball
      Oger
      Oil dick
      Old fart
      Orang-Uthan
      Original
      Outlaw
      Pack
      Pain in the ass
      Pavian
      Pencil dick
      Pervert
      Pig
      Piggy-wiggy
      Pirate
      Pornofreak
      Prick
      Prolet
      Queer
      Querulant
      Rat
      Rat-fink
      Reject
      Retard
      Riff-Raff
      Ripper
      Roboter
      Rowdy
      Rufian
      Sack
      Sadist
      Saprophyt
      Satan
      Scarab
      Schfincter
      Shark
      Shit eater
      Shithead
      Simulant
      Skunk
      Skuz bag
      Slave
      Sleeze
      Sleeze bag
      Slimer
      Slimy bastard
      Small pricked
      Snail
      Snake
      Snob
      Snot
      Son of a bitch 
      Square
      Stinker
      Stripper
      Stunk
      Swindler
      Swine
      Teletubby
      Thief
      Toilett cleaner
      Tussi
      Typ
      Unlike
      Vampir
      Vandale
      Varmit
      Wallflower
      Wanker
      Wanker, bloody
      Weeze Bag
      Whore
      Wierdo
      Wino
      Witch
      Womanizer
      Woody allen
      Worm
      Xena
      Xenophebe
      Xenophobe
      XXX Watcher
      Yak
      Yeti
      Zit face"""


      asplit = adj.split()
      nsplit = noun.split()
      #for i in range(1,50):
            #global asplit
            #global a

      for i in range(1,num+1):
            r = random.randint(1,len(asplit)-1)
            r2 = random.randint(1,len(nsplit)-1)
            insult = "you are a "+asplit[r]+" "+nsplit[r2]+"!"
            print(insult)
            if Speak:
                  os.system("say "+insult)
            

