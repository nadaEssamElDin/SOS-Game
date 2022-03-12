x = [[0], [0], [0],[0],
    [0] ,[0], [0], [0],
    [0], [0], [0], [0],
    [0], [0], [0], [0]]
score_player_one=0
score_player_two=0
i=0

player=1

#def printboard():
 #       print("-----------------------")
  #      print(x[0],"|",x[1],"|", x[2],"|",x[3],"|")
   #     print("-----------------------")
    #    print(x[4],"|",x[5],"|",x[6],"|", x[7],"   |")
     #   print("-----------------------")
      #  print(x[8],"|",x[9],"|", x[10],"|",x[11]," |")
       # print("-----------------------")
#print(x[12],"|",x[13],"|",x[14],"|", x[15]," |")
        #print("-----------------------")
   
while i<16:

    #printboard()
    f1=int(input(str(player) + "  choose where you want to play "))-1
    s1=(input(str(player) + "  choose what you want to play "))
    if f1>16:
        continue
    if not(s1=="s"or s1=="o"):
        continue
    if x[f1]==["s"] or x[f1]==["o"]:      
        print("  invalide try again  ")
        continue
    else:
        x[f1]=[s1]
    if player ==1 and s1=="s":
        if 0<=f1+1<=15 and 0<=f1+2<=15:
            if x[f1]==["s"] and x[f1+1]==["o"] and x[f1+2]==["s"]:
                score_player_one+=1
        if 0<=f1-1<=15 and 0<=f1-2<=15:
            if x[f1]==["s"] and x[f1-1]==["o"] and x[f1-2]==["s"]:
                score_player_one+=1
        if 0<=f1+4<=15 and 0<=f1+8<=15:        
            if x[f1]==["s"] and x[f1+4]==["o"] and x[f1+8]==["s"]:
                score_player_one+=1
        if 0<=f1-4<=15 and 0<=f1-8<=15:      
            if x[f1]==["s"] and x[f1-4]==["o"] and x[f1-8]==["s"]:
                score_player_one+=1
        if 0<=f1+5<=15 and 0<=f1+10<=15:        
            if x[f1]==["s"] and x[f1+5]==["o"] and x[f1+10]==["s"]:
                score_player_one+=1 
        if 0<=f1-5<=15 and 0<=f1-10<=15:       
            if x[f1]==["s"] and x[f1-5]==["o"] and x[f1-10]==["s"]:
                score_player_one+=1
        if 0<=f1-3<=15 and 0<=f1-6<=15:       
            if x[f1]==["s"] and x[f1-3]==["o"] and x[f1-6]==["s"]:
                score_player_one+=1     
        if 0<=f1+3<=15 and 0<=f1+6<=15:       
            if x[f1]==["s"] and x[f1+3]==["o"] and x[f1+6]==["s"]:
                score_player_one+=1     


    elif  player ==1 and s1=="o":
            if 0<=f1+1<=15 and 0<=f1-1<=15:
                if x[f1]==["o"] and x[f1-1]==["s"] and x[f1+1]==["s"]:
                    score_player_one+=1
            if 0<=f1+4<=15 and 0<=f1-4<=15:
                if x[f1]==["o"] and x[f1+4]==["s"] and x[f1-4]==["s"]:
                    score_player_one+=1
            if 0<=f1+5<=15 and 0<=f1-5<=15:
                if x[f1]==["o"] and x[f1+5]==["s"] and x[f1-5]==["s"]:
                    score_player_one+=1
            if 0<=f1+3<=15 and 0<=f1-3<=15:
                if x[f1]==["o"] and x[f1+3]==["s"] and x[f1-3]==["s"]:
                    score_player_one+=1


    elif player ==2 and s1=="s":
        if 0<=f1+1<=15 and 0<=f1+2<=15:
            if x[f1]==["s"] and x[f1+1]==["o"] and x[f1+2]==["s"]:
                score_player_two+=1
        if 0<=f1-1<=15 and 0<=f1-2<=15:
            if x[f1]==["s"] and x[f1-1]==["o"] and x[f1-2]==["s"]:
                score_player_two+=1
        if 0<=f1+4<=15 and 0<=f1+8<=15:        
            if x[f1]==["s"] and x[f1+4]==["o"] and x[f1+8]==["s"]:
                score_player_two+=1
        if 0<=f1-4<=15 and 0<=f1-8<=15:      
            if x[f1]==["s"] and x[f1-4]==["o"] and x[f1-8]==["s"]:
                score_player_two+=1
        if 0<=f1+5<=15 and 0<=f1+10<=15:        
            if x[f1]==["s"] and x[f1+5]==["o"] and x[f1+10]==["s"]:
                score_player_two+=1 
        if 0<=f1-5<=15 and 0<=f1-10<=15:       
            if x[f1]==["s"] and x[f1-5]==["o"] and x[f1-10]==["s"]:
                score_player_two+=1 
        if 0<=f1-3<=15 and 0<=f1-6<=15:       
            if x[f1]==["s"] and x[f1-3]==["o"] and x[f1-6]==["s"]:
                score_player_two+=1     
        if 0<=f1+3<=15 and 0<=f1+6<=15:       
            if x[f1]==["s"] and x[f1+3]==["o"] and x[f1+6]==["s"]:
                score_player_two+=1     

    else:
        if player ==2 and s1=="o":
            if 0<=f1+1<=15 and 0<=f1-1<=15:
                if x[f1]==["o"] and x[f1-1]==["s"] and x[f1+1]==["s"]:
                    score_player_two+=1
            if 0<=f1+4<=15 and 0<=f1-4<=15:
                if x[f1]==["o"] and x[f1+4]==["s"] and x[f1-4]==["s"]:
                    score_player_two+=1
            if 0<=f1+5<=15 and 0<=f1-5<=15:
                if x[f1]==["o"] and x[f1+5]==["s"] and x[f1-5]==["s"]:
                    score_player_two+=1
            if 0<=f1+3<=15 and 0<=f1-3<=15:
                if x[f1]==["o"] and x[f1+3]==["s"] and x[f1-3]==["s"]:
                    score_player_two+=1    
    player=player%2+1        
    i=i+1
if score_player_one>score_player_two:
    print("player one won")
elif score_player_one<score_player_two:
    print("player two won")
if score_player_one==score_player_two:
    print("drawn")