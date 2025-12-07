# Student marks calculator
print("=== Student Grade Calculator ===")
name = input("Student Name: ").title()
marks = [int(x) for x in input("Enter 5 subject marks: ").split()]

if len(marks) != 5:
    print("Please enter exactly 5 marks!")
else:
    total = sum(marks)
    avg = total / 5
    grade = "A" if avg >= 90 else "B" if avg >= 70 else "C" if avg >= 50 else "F"
    
    print(f"\n{name}'s Report:")
    print(f"Total: {total}/500")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")