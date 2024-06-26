class multiFunction():
    def SubfieldsInAI():
        lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for subfi in lists:
            print(subfi)
        return subfi
    def odd_Even():
        num1=int(input("Enter a Number: "))
        if(num1%2==0):
            print(num1,"is Even Number")
        else:
            print(num1,"is Odd Number")
        return num1
    
    def marriageEligibility1():
        gender=input("Your Gender: ").lower()
        age=int(input("Your Age: "))
        if (gender in ("male","m")):
            if(age<21):
                print("Not Eligible")
            else:
                print("Eligible")
        if (gender in ("female","f")):
            if(age<18):
                print("Not Eligible")
            else:
                print("Eligible")
        return age 

    def mark_per():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        total=sub1+sub2+sub3+sub4+sub5
        per=(total/500)*100
        print("Total : ",total)
        print("Percentage : ", per)
        return total

    def triangleAB():
        h1=float(input("Height1: "))
        h2=float(input("Height2: "))
        br=float(input("Breadth: "))
        area=(h1*br)/2
        print("Area of Triangle: ",area)
        perimeter=h1+h2+br
        print("Perimeter of Triangle: ",perimeter)
        return area