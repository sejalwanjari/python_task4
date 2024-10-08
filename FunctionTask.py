#Example 1 of function:
print('Example 1 of function')


def libraryUser(StudentID,StudentName,StudentMob,StudentDepartment,BookCheckout):
    print(f'StudentID = {StudentID}')
    print(f'StudentName = {StudentName}')
    print(f'StudentMob = {StudentMob}')
    print(f'StudentDepartment = {StudentDepartment}')
    print(f'BookCheckout = {BookCheckout}')
    print()

    return {
        'Student-ID': StudentID,
        'Student-Name' : StudentName,
        'Student-Mob': StudentMob,
        'Student-Department': StudentDepartment,
        'BookCheckout': BookCheckout
    }
print()

Student1 = libraryUser(13,'Aniket',45678,'CS',2)
print(f'Student1 = {Student1}')
print()

Student2 = libraryUser(16,'Sejal',36465,'ETC',1)
print(f'Student2 = {Student2}')
print()

Student3 = libraryUser(7,'Bhavik',45987,'AI',5)
print(f'Student3 = {Student3}')
print()

print()





# Example 2 of Function
print('Example 2 of function')


def CreateAccount(AccountID,AccountNo,AccountName,Mobileno,Address,Nationality):
    print(f'AccountID = {AccountID}')
    print(f'AccountNo = {AccountNo}')
    print(f'AccountName = {AccountName}')
    print(f'Mobileno = {Mobileno}')
    print(f'Address = {Address}')
    print(f'Nationality = {Nationality}')
    print()

    return {
        'Account-ID': AccountID,
        'Account-No' : AccountNo,
        'Account-Name': AccountName,
        'Mobile-no': Mobileno,
        'Address': Address,
        'Nationality': Nationality
    }
print()

Account1 = CreateAccount(101,857395867365,'Sanjay Tiwari',45678,'Itwari','Indian')
print(f'Account1 = {Account1}')
print()

Account2 = CreateAccount(102,690274638925,'Ankush Gupta',36465,'Ravi Nagar','Indian')
print(f'Account2 = {Account2}')
print()

Account3 = CreateAccount(103,774728449506,'AAkash Sahare',45987,'Laxmi Nagar','Indian')
print(f'Account3 = {Account3}')
print()

Account4 = CreateAccount(104,738591236587,'Anjali Mehta',45679,'Kalamna','Indian')
print(f'Account4 = {Account4}')
print()

Account5 = CreateAccount(105,274855476925,'Preeti Bansod',65837,'Itwari','Indian')
print(f'Account5 = Account5')

