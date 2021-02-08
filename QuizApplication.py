import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                     database='Quizes',
                                     user='root',
                                     password='root')
cursor = connection.cursor()


def SetQue(QueId, SuperUserId, QueName, OptionA, OptionB, OptionC, OptionD):
    mySql_insert_query = """INSERT INTO QueSet (QueId, SuperUserId, QueName, OptionA, OptionB, OptionC, OptionD)
                                      VALUES (%s, %s, %s, %s, %s, %s, %s) """

    recordTuple = (QueId, SuperUserId, QueName, OptionA, OptionB, OptionC, OptionD)
    cursor.execute(mySql_insert_query, recordTuple)
    connection.commit()
    print("inserted successfully ")


def SetAns(AnsId, Ans):
    mySql_insert_query = """INSERT INTO AnsSet(AnsId,Ans)
                         VALUES (%s, %s) """
    record = (AnsId, Ans)
    cursor.execute(mySql_insert_query, record)
    connection.commit()
def UpdateAns(Ans,AnsId):
    mySql_update_query = """UPDATE AnsSet
                            SET Ans = %s
                            WHERE AnsId = %s """
    record = (Ans, AnsId)
    cursor.execute(mySql_update_query, record)
    connection.commit()
    print("Updated successfully ")


def newRecord():
    UserId = int(input("Enter user id:\n"))
    ch1 = int(input("1 First:"
                    "2 next"))
    if ch1 == 1:

        QueID = int(input("Enter Question Id:\n"))
        sql_select_query = """select * from QueSet  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        for r in record:
            if QueID == r[0]:
                print("Question = ", r[2], )
                print("OptionA= ", r[3])
                print("OptionB = ", r[4])
                print("OptionC = ", r[5])
                print("OptionD= ", r[6])
                print()
        user_ans = input("Select Your Option:\n")
        sql_select_query = """select * from AnsSet  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()

        for r in record:
            if user_ans == r[1]:
                mySql_insert_query = """INSERT INTO Result(Id,Marks,ResultStatus)
                                                             VALUES (%s, %s, %s) """
                record = (UserId, 10, 'Fail')
                cursor.execute(mySql_insert_query, record)
                connection.commit()
        newRecord()

    if ch1 == 2:
        QueID = int(input("Enter Question Id:\n"))
        sql_select_query = """select * from QueSet  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        for r in record:
            if QueID == r[0]:
                print("Question = ", r[2], )
                print("OptionA= ", r[3])
                print("OptionB = ", r[4])
                print("OptionC = ", r[5])
                print("OptionD= ", r[6])
        test_ans = input("Select Your Option:\n")
        sql_select_query = """select * from AnsSet  """
        cursor.execute(sql_select_query)
        rec = cursor.fetchall()
        # sql_select_query = """select * from Result  """
        # cursor.execute(sql_select_query)
        # record1 = cursor.fetchall()
        global marks
        sql_select_query = """select * from Result  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        for r in record:
                marks = r[1]
                marks += 10
        for r in rec:
            if test_ans == r[1]:
                mySql_update_query = """UPDATE Result
                                        SET Marks = %s
                                        WHERE Id = %s """
                record = (marks, UserId)
                cursor.execute(mySql_update_query, record)
                connection.commit()
            if marks < 20:
                status = "Fail"
            else:
                status = "Pass"
            mySql_update_query = """UPDATE Result
                                SET ResultStatus = %s
                                WHERE Id = %s """
            record = (status, UserId)
            cursor.execute(mySql_update_query, record)
            connection.commit()
        newRecord()
    if ch1 == 0:

        exit()
def display():
    print("Please Enter your choice:")
    print("**********************************************************************")
    print("0. Exit")
    print("1. Set Quiz (Only super_user)")
    print("2. Modify Ans(Only super user)")
    print("3. Attempt Quiz")
    print("4. Display Result")
    choice = int(input("Enter your choice:\n"))
    if choice == 0:
        exit()
    if choice == 1:
        SuperUserId = int(input("Enter the super user id:\n"))
        QueId = int(input("Enter the QueId:\n"))
        AnsId = QueId
        QueName = input("Enter the question:\n")
        OptionA = input("Enter the optionA:\n")
        OptionB = input("Enter the optionB:\n")
        OptionC = input("Enter the optionC:\n")
        OptionD = input("Enter the optionD:\n")
        ans = input("Enter the correct Answer:\n")
        SetQue(QueId, SuperUserId, QueName, OptionA, OptionB, OptionC, OptionD)
        SetAns(AnsId, ans)
    if choice == 2:
        updateId = int(input("Enter the Question Id:\n"))
        sql_select_query = """select * from QueSet  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        for r in record:
            if updateId == r[0]:
                print("Question = ", r[2], )
                print("OptionA= ", r[3])
                print("OptionB = ", r[4])
                print("OptionC = ", r[5])
                print("OptionD= ", r[6])
                print()
        new_ans = input("Enter new ans:\n")
        UpdateAns(new_ans, updateId)
    if choice == 3:
        newRecord()
    if choice == 4:
        updateId = int(input("Enter the user Id:\n"))
        sql_select_query = """select * from Test_Taker  """
        cursor.execute(sql_select_query)
        record = cursor.fetchall()
        for r in record:
            if updateId == r[0]:
                print("Id = ", r[0], )
                print("First Name= ", r[1])
                print("Last Name = ", r[2])
                print("Gender = ", r[3])

                print()
        sql_select_que = """select * from Result  """
        cursor.execute(sql_select_que)
        rec = cursor.fetchall()
        for i in rec:
            if updateId == i[0]:
                print("Marks= ", i[1])
                print("Status = ", i[2])


                print()

display()