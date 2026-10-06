import streamlit as st
import random
st.title("Guess the number Game")
st.write("Enter Quit to exit the game")
st.write("When ask do you wanna play the game Enter y / n or quit")
st.write("I pick a secret number between 3 and 30 (both included).")
st.write("You have 5 tries. I'll tell you if each guess is too low or too high.")

def play_again():
   
    st.session_state.question = st.text_input("You wanna play again(enter y for yes or n for no-: ")
    if st.session_state.question.lower()=="y":
        del st.session_state.secret_number
        st.session_state.game_over = False
        st.rerun()
        
    elif st.session_state.question.lower()=="n"or st.session_state.question.lower()=="quit":
        st.write("Okay bie See ya next time")
            
        
    else:
        st.write("Enter only y or n")

def GuessANumber():
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(3,30) 
    
        st.session_state.guessCountLimit = 0
  
    st.session_state.your_number = st.text_input("Enter Your number(between 3 and 30/quit to exit the game)-: ")
    if st.session_state.your_number=="":
         return
    if st.session_state.your_number.lower() == "quit":          
        st.write("Okay bie See ya next time")  
        st.session_state.game_over =True   
        return
    try:
        st.session_state.your_number = int(st.session_state.your_number)
        if st.session_state.your_number>30 or st.session_state.your_number<3:
            st.write("Enter number between 3 and 30 ")
               
        if st.session_state.your_number== st.session_state.secret_number:
            st.write("You won the game", st.session_state.your_number, "is equal to", st.session_state.secret_number)
            st.session_state.game_over = True
            return
                
                
        elif st.session_state.your_number>st.session_state.secret_number:
                st.write("Too High!Try again")
        elif st.session_state.your_number<st.session_state.secret_number:
                st.write("Too Low! Try again")
            
        else:
                pass

        st.session_state.guessCountLimit+=1
        if st.session_state.guessCountLimit<5:
            pass
            st.write(st.session_state.guessCountLimit)
        else:
            st.write("You exceede the max try limit of",st.session_state.guessCountLimit, "Please try again. The original number was :", st.session_state.secret_number,)
            st.write(st.session_state.your_number,"is not equal to secret number Hence You lost!")
            st.session_state.game_over = True
                
            
            
               
            
                    
    except ValueError:
        st.write("only integers")

if "game_over" not in st.session_state:
    st.session_state.game_over = False
            
if not st.session_state.game_over:
    GuessANumber()
else:
    play_again()