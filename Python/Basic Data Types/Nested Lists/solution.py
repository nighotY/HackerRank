if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records+=[[name, score]]
        

    marks = [j[1] for i,j in enumerate(records)]
    marks.sort()
    second_highest=marks[0]
    for i,val in enumerate(marks):
        if second_highest == val and second_highest < marks[i+1]:
            second_highest = marks[i+1]
            break
    

    second_highest_student = [lst[0] for i,lst in enumerate(records) if lst[1] == second_highest]
    second_highest_student.sort()
    for name in second_highest_student:
        print(name)