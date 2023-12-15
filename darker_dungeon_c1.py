import time
print(R"""
              /000\         /000\
       /000000/   \00\   /00/   \000000\    
  /0000/            \0\ /0/            \0000\
<0                   >0X0<                   0>
  \0000\            /0/|\0\            /0000/
       \000000\   /00/|||\00\   /000000/
              \000/   |||   \000/
                     |||||
                     |||||
 ____               |||||||
|____|         ______  o          o   |   |      |
||___  | ___   |       |  | ___   | --+-- |      |
|____| |/   \  |----   |  |/   \  |   |    \____ |
||___  |     | |       |  |     | |   |          |
|____| |     | |       |  |     | |   |     ____/
  /========\                                   ___
 //        \\                                /   \
||          ||   _____    | _   _      _____  \
||     =====_   /     \   |/ \ / \    /_____\   \
||     ||   || |      |\  |   |   |  |            \
 \\________//   \____/  \ |   |   |   \_____/ \___/
      """)


hp = 1
power = 0
i = []

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


player = input('your name : ')
while True :
   print(F' {player} : where am i ? ')
   print('you look around')
   time.sleep(3)
   print(" but you can't see any thing ")
   time.sleep(1)
   print(f'{player}:i must find a light')
   time.sleep(1)
   print('1.look carefully for light')
   print('2.stand up')
   q1 = input(':')
   time.sleep(3)
   if q1 == '1':
      print("you see a litle light source in front of you")
      time.sleep(1)
      print('you go to light')
      print(f'(chain sound){player}:hu? im locked !')   
      print('1.toch gruond aruond you') 
      q3 = input(':')
      time.sleep(3)
      if q3 == "1":
         time.sleep(1)
         print(f'{player}:Ooch  what was that?')
         time.sleep(2)
         print(color.RED + 'you found sharp stone' + color.END)
   elif q1 == '2' :
      print(f'(chain sound){player}:hu? im locked !')
      time.sleep(1)
      print('1.toch gruond aruond you') 
      q3 = input(':')
      if q3 == "1":
            print(f'{player}:Ooch  what was that?')
            time.sleep(2)
            print(color.RED + 'you found sharp stone' + color.END)
            time.sleep(2)
   print(f'{player}:this can be usefull')
   time.sleep(1)
   print("1.throw it to light source")
   time.sleep(1)
   print("2.try to pick the lock of chain")
   q4 = input(":")
   if q4 == '1':
      print(f'{player}:ha')
      time.sleep(2)
      print('ding')
      time.sleep(2)
      print(f"{player}:Ooch!that didn't do any thing")
      print("you try to pick the lock of chain")
   elif q4 == '2' :
      print('chlik,chlik,tick')
      time.sleep(1)
      print(f"WHAT!HOW!")
      time.sleep(2)
      print('tuk,tuk,tuk')
      time.sleep(1)
      print(f"{player}:someone is coming im need to hide")
      time.sleep(1)
      print("1.hide next to door")
      time.sleep(1)
      print('2.hide in corner')
      q6 = input(":")
   if  q6 == '1' :
      print('gard:o no he escaped boss going to kill me')
      time.sleep(1)
      print("1.jump and kill the gard")
      q7 = input(":")
   if q7 == '1':
      print(f"{player}:haaa")
      time.sleep(1)
      print("gard:AAA")
      time.sleep(1)
      print(color.YELLOW + 'you found the key ring' + color.END)
      time.sleep(1)
      print(color.RED + 'you found the sword' + color.END)
      time.sleep(1)
   elif q6 == "2" :
      print("gard:WAIT THRE")
      time.sleep(1)
      print(F"{player}:i mustn't do that")
      hp = 0
      if hp == 0:
         print(color.RED + 'GAME OVER' + color.END) 
         break
   print(f'{player}:well.what should i do now?')
   time.sleep(1)
   print('1.pick up the sword and key rind')
   q8 = input(":")
   if q8 == "1" :
      i.append('sword')
      i.append('gard key ring')
      power += 1
   time.sleep(1)
   print(f'{player}: well done')
   time.sleep(1)
   print('you get out of dungeon.')
   print(color.CYAN + 'now yoou can see' + color.END)
   time.sleep(1)
   print("""
   ▊▊▊▊▊▊▊▊▊|▊|▊|_________|▊▊▊▊|||▊▊▊▊▊▊|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊|▊|▊|_________|▊▊▊|||▊▊▊▊▊▊|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_________|▊▊|||▊▊▊▊▊▊|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊    
   ▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_________|▊|||▊▊▊▊▊▊|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_________||||▊▊▊▊▊▊|||▊▊▊▒▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_________|||▊▊▊▊▊▊|||▊▊░░░▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|________|||▊▊▊▊▊▊|||▊▒░▓░▒▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_______||||▊▊▊▊▊|||▊▊░▓░▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|______|||_|▊▊▊▊|||▊▊▊|▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_____|||__|▊▊▊|||▊▊▊|▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|____|||___|▊▊|||▊▊▊|▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|___|||____|▊|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|__|||_____||||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|_|||______|||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊||||_______||▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊|▊|||________|▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
   ▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊|▊||||        |▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊
      """)
   time.sleep(6)
   print(color.CYAN + 'end of capter one' + color.END)
   time.sleep(3)
   print(color.BLUE + 'thanks for playng' + color.END)
   time.sleep(3)
   print(color.GREEN + 'a game by' + color.END)
   print(color.PURPLE + '' + color.BOLD)
   print('Enfinity Games')
   print(color.PURPLE + '' + color.END)