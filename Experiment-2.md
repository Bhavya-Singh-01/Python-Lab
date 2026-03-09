# Experiment 2
## Control Flow and Looping Statements in Python

### Aim
To write a Python program to implement control flow statements and looping statements.

### Algorithm
1. Start the program.
2. Take an integer input from the user.
3. Use an **if-else control statement** to check whether the number is positive or negative.
4. Use a **for loop** to print numbers from 1 to 5.
5. Use a **while loop** to print numbers from 1 to the entered number.
6. Display the results.
7. Stop the program.

Source Code
runs=int(input("enter runs:"))
balls=int(input("enter the number of balls faced:"))
strike_rate=runs/balls*100
if runs>50 and strike_rate>120:
    print("excellent batter")
elif runs>30 and strike_rate>100:
    print("good batter")
elif runs>20:
    print("average batter")
else:
    print("poor batter")

run_conceded=int(input("enter run conceded:"))
overs=int(input("enter overs:"))
wickets=int(input("enter wickets taken:"))
economy=run_conceded/overs
if wickets>3 and economy<6:
    print("excellent bowler")
elif wickets>2 and economy<8:
    print("good bowler")
else:
    print("poor bowler")

catches=int(input("enter number of catches:"))
if catches>2:
    print("outstanding fielder")
elif catches==1:
    print("active fielder")
else:
    print("needs improvement")


Output:
enter runs:150
enter the number of balls faced:30
excellent batter
enter run conceded:40
enter overs:6
enter wickets taken:7
good bowler
enter number of catches:7
outstanding fielder
