def average(n, tot):
    avg = tot / n
    return avg
def total():
    tot = 0
    score = input("score : ").split()
    for i in score:
        tot += int(i)
    avg = average(len(score), tot)
    print("total score : %d" % tot)
    print("average score : %.2f" % avg)
total()