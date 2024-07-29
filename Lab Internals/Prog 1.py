total_subjects=3

name=input("Enter the students name ")
usn=input("Enter the students usn ")

sub1=int(input("Enter the marks of subject 1 "))
sub2=int(input("Enter the marks of subject 2 "))
sub3=int(input("Enter the marks of subject 3 "))

total=int(input("Enter the total marks of the subjects "))
total_mark=sub1+sub2+sub3
percent=((total_mark)/(total_subjects*total))*100

print(f"Total marks is {total_mark}")
print(f"Percentage obtained is {percent}")
