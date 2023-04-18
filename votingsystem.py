nominee1 = input("Enter The Name Of The First Nominee:  ")
nominee2 = input("Enter The Name Of The Second Nominee:  ")


nm1_votes = 0
nm2_votes = 0


voter_id = [1,2,3,4,5]

no_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("Voting Session Is Over !!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1,"has won the election with",percent,"% of votes")
            break
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2,"has won the election with",percent,"% of votes")
            break
        else:
            print("Both Have Equal No Of VOtes !!! ")

    print("*************************************************")
    voter =int(input("Enter Your Voter Id : "))
    if voter in voter_id:
        print("You Are A Valid Voter")
        voter_id.remove(voter)
        print("---------------------------------------")
        print("To Give Vote To ",nominee1,"Press 1")
        print("To Give Vote To ",nominee2,"Press 2")
        print("---------------------------------------")
        vote = int(input("Enter Your Precious Vote : "))
        if vote == 1:
            nm1_votes += 1
            print("Thank You For Voting",nominee1)
        elif vote == 2:
            nm2_votes += 1
            print("Thank You For Voting",nominee2)
        elif vote > 2 :
            print("You Press Wrong Key")
    else:
        print("You Are Not A Voter or You Are Already Voted")