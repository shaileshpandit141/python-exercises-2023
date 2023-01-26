'''
Q9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

def Display_examination_schedule(myexam_st_date):
    print("The examination will start from :",myexam_st_date[0], "/", myexam_st_date[1], "/", myexam_st_date[2])


if __name__=="__main__":
    exam_st_date = (11, 12, 2014)
    Display_examination_schedule(exam_st_date)