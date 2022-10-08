import glob

import cv2

import numpy as np



id_box=[(254, 38),(464, 278)]

q_box=[(40, 299),(240, 1499)]
ans=["A","B","C","D","E"]
ladder1=[]
ladder2=[]
ladder3=[]
ladder4=[]
ladder1_mark=[]
ladder2_mark=[]
ladder3_mark=[]
ladder4_mark=[]

std=[]

answers1=[]
answers2=[]
answers3=[]
answers4=[]
select_ladder1=False
select_ladder2=False
select_ladder3=False
select_ladder4=False
path1=""
path2=""
path3=""
path4=""
supject_name=""
num_q=""
num_std=""
mark=""
laders=""
no_ids=0

qq = 0

# get paper corners
def crop(frame1,org):
    boxes = []
    cw=50
    ch=50
    frame1 = np.asarray(frame1)
    row, col = frame1.shape
    lt = (0, 0)
    lb = (0, 0)
    rt = (0, 0)
    rb = (0, 0)
    ########                 left - top
    for j in range(cw):
        found = 0
        for i in range(ch):
             if(frame1[i][j]<=50):
                 ii=i
                 jj=j
                 while(frame1[ii][jj]<=10):
                     ii+=1

                 while(frame1[ii-1][jj]<=10):
                     jj+=1
                 # frame1 = cv2.circle(image, (ii-3,jj-3), radius=0, color=255, thickness=-1)
                 # frame1[ii-3,jj-3]=250
                 lt=(jj-2,ii-2)
                 found=1
                 break
        if(found==1):
            break


     #####                     left - bottom

    # print(row,"   ",col)
    for j in range(cw):
        found = 0
        for i in range(ch):
             r=row-i-1
             if(frame1[r][j]<=10):
                 ii=i
                 jj=j
                 while(frame1[row-ii][jj]<=10):
                     ii+=1

                 while(frame1[row-ii-1][jj]<=10):
                     jj+=1
                 lb=(jj-1,row-ii+3)
                 found=1
                 break
        if(found==1):
            break

    ########                 right - top
    for j in range(cw):
            found = 0
            for i in range(ch):
                c = col - j - 1
                if (frame1[i][c] <= 50):
                    ii = i
                    jj = j
                    while (frame1[ii][c] <= 10):
                        ii += 1

                    while (frame1[ii - 1][c] <= 10):
                        c -= 1
                    rt=(c+3,ii-2)
                    found = 1
                    break
            if (found == 1):
                break
            #####                     right - bottom

            # print(row,"   ",col)
    for j in range(cw):
        found = 0
        for i in range(ch):
            r = row - i - 1
            c = col - j - 1
            if (frame1[r][c] <= 10):
                ii = i
                jj = j
                while (frame1[r][c] <= 10):
                    r -= 1
                while (frame1[r][c] <= 10):
                    c -= 1
                # frame1 = cv2.circle(image, (r-2,c-3), radius=0, color=255, thickness=-1)
                # frame1[r- 2, c-3] = 250
                rb=(c,r+5)
                found = 1
                break
        if (found == 1):
            break
    orginal_frame=np.float32([lt,rt,lb,rb])
    new_frame=np.float32([[0,0],[col,0],[0,row],[col,row ]])
    p=cv2.getPerspectiveTransform(orginal_frame,new_frame)
    frame1=cv2.warpPerspective(frame1,p,(1004,1500))

    org = cv2.resize(org, (500, 600))
    org=cv2.warpPerspective(org,p,(500,600))
    return frame1,org

def get_id(frame1):
    ref = frame1[id_box[0][1]:id_box[1][1], id_box[0][0]:id_box[1][0]]
    itemss=splitBoxes_id(ref)
    dd=[]
    id=0
    for i in itemss:

        number_of_black_pix = np.sum(i == 0)
        # print("num Black in ID",number_of_black_pix)
        if number_of_black_pix > 70 :
          dd.append('1')
        else:
          dd.append('0')
    dd = np.asarray(dd)
    dd = np.reshape(dd, (10,10))

    for i in range(10):
      on = 0
      for j in range(10):
          if dd[j][9-i]=='1':
              on+=j
      if i==0:
          id=on
      else :
          id=id+(on*pow(10,i))

    # print(" stu ID : ",id)
    return id

# split ID Box
def splitBoxes_id(frame1):
    boxes = []
    (x, y, w, h) = cv2.boundingRect(frame1)
    cw=int(w/10)
    ch=int(h/10)
    x1=0
    y1=0
    cw1=cw
    ch1=ch
    cell = [(x, y), (cw, ch)]
    for i in range(10):
        for j in range(10):
            ref=frame1[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]
            x1=x1+cw
            cw1=cw1+cw
            cell = [(x1, y1), (cw1, ch1)]
            boxes.append(ref)
        y1=y1+ch
        ch1=ch1+ch
        x1=0
        cw1=cw
        cell = [(x1, y1), (cw1, ch1)]

    return boxes
def get_q(frame1,q=q_box):
    ref = frame1[q[0][1]:q[1][1], q[0][0]:q[1][0]]
    cv2.imshow("Answers image", ref)
    itemss=splitBoxes_q(ref)
    dd = []
    answers=[]
    for i in itemss:
        # cv2.imshow("aaaaaaaaaaaaaaa",i)
        # cv2.waitKey()
        number_of_black_pix = np.sum(i == 0)
        print(number_of_black_pix)
        if number_of_black_pix >= 50:
            dd.append('1')
        else:
            dd.append('0')
    dd = np.asarray(dd)
    dd = np.reshape(dd, (50, 5))

    for i in range(50):
      answer=""
      for j in range(5):
          if dd[i][j]=='1':
               answer+=ans[j]
      if answer != "":
          answers.append(answer)
    return answers
# Know Question answers
def get_q_stu(frame1,q=q_box):
    ref = frame1[q[0][1]:q[1][1], q[0][0]:q[1][0]]
    itemss=splitBoxes_q(ref)
    dd = []
    answers=[]
    for i in itemss:
        number_of_black_pix = np.sum(i == 0)

        if number_of_black_pix >60:
            dd.append('1')

        elif number_of_black_pix > 50 and number_of_black_pix <=50:
            dd.append('*')
        else:
            dd.append('0')
    dd = np.asarray(dd)
    dd = np.reshape(dd, (50, 5))

    for i in range(50):
      answer=""
      for j in range(5):
          if dd[i][j]=='1':
               answer+=ans[j]
          elif dd[i][j]=='*':
              answer += "*"
      answers.append(answer)
    return answers

#split paper - Student ID department
def splitBoxes_q(frame1):
    boxes = []
    (x, y, w, h) = cv2.boundingRect(frame1)
    cw=int(w/5)
    ch=int(h/50)
    x1=0
    y1=0
    cw1=cw
    ch1=ch
    cell = [(x, y), (cw, ch)]
    for i in range(50):
        for j in range(5):
            ref=frame1[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]
            x1=x1+cw
            cw1=cw1+cw
            cell = [(x1, y1), (cw1, ch1)]
            boxes.append(ref)
        y1=y1+ch
        ch1=ch1+ch
        x1=0
        cw1=cw
        cell = [(x1, y1), (cw1, ch1)]

    return boxes

#split paper - questions department
def split_Q(frame1,i,org,q=q_box):
    ref = frame1[q[0][1]:q[1][1], q[0][0]:q[1][0]]
    org1 = org[q[0][1]:q[1][1], q[0][0]:q[1][0]]
    boxes = []
    (x, y, w, h) = cv2.boundingRect(ref)
    cw = int(w / 5)
    ch = int(h / 50)

    cell = [(x, ch*i+2), (w, ch*i+ch+2)]
    ref = ref[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]
    org = org1[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]


    return ref,org

# image processing
def img_processing(img):
    image = cv2.resize(img, (500, 600))
    a = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",a)
    a = cv2.bilateralFilter(a, 9, 31, 31)
    cv2.imshow("fillter", a)
    ret, aa = cv2.threshold(a, 50, 255, cv2.THRESH_BINARY)
    cv2.imshow("thesh", aa)

    return ret, aa
def img_processing2(img,x=50):
    image = cv2.resize(img, (1004, 1500))
    a = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray",a)
    a = cv2.bilateralFilter(a, 7, 31, 31)
    ret, aa = cv2.threshold(a, x, 255, cv2.THRESH_BINARY)

    # cv2.imshow("fillter", a)
    # cv2.imshow("thesh", aa)

    return ret, aa
def Q_processing(q,x=50):
    a = cv2.cvtColor(q, cv2.COLOR_BGR2GRAY)
    a = cv2.bilateralFilter(a, 9, 31, 31)
    ret, aa = cv2.threshold(a, x, 255, cv2.THRESH_BINARY)
    return aa
def get_one_q_answer(q):
    (x, y, w, h) = cv2.boundingRect(q)
    cw = int(w / 5)

    cell = [(x, y), (cw, h)]
    ref1 = q[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]

    cell = [(cw, y), (cw*2, h)]
    ref2 = q[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]

    cell = [(cw*2, y), (cw * 3, h)]
    ref3 = q[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]

    cell = [(cw * 3, y), (cw * 4, h)]
    ref4 = q[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]

    cell = [(cw * 4, y), (w, h)]
    ref5 = q[cell[0][1]:cell[1][1], cell[0][0]:cell[1][0]]

    answers=""
    number_of_black_pix = np.sum(ref1 == 0)
    if number_of_black_pix > 70:
        answers+=('A')

    elif number_of_black_pix > 2 and number_of_black_pix <= 10:
        answers+=('*')

    number_of_black_pix = np.sum(ref2 == 0)

    if number_of_black_pix > 70:
        answers+=('B')

    elif number_of_black_pix > 2 and number_of_black_pix <= 10:
        answers+=('*')

    number_of_black_pix = np.sum(ref3 == 0)
    if number_of_black_pix > 70:
        answers+=('C')

    elif number_of_black_pix > 2 and number_of_black_pix <= 10:
        answers+=('*')

    number_of_black_pix = np.sum(ref4 == 0)
    if number_of_black_pix > 70:
        answers+=('D')

    elif number_of_black_pix > 2 and number_of_black_pix <= 10:
        answers+=('*')

    number_of_black_pix = np.sum(ref5 == 0)
    if number_of_black_pix > 10:
        answers+=('E')

    elif number_of_black_pix > 2 and number_of_black_pix <= 10:
        answers+=('*')
    return answers
def correct(ladder,marks,path):
    images = glob.glob(path)
    for image in images:
        img = cv2.imread(image, 1)
        image = img.copy()
        ret, aa=img_processing(image)
        f1=crop(aa)
        id=get_id(f1)
        answers=get_q_stu(f1)
        sum=0
        for i in range (len(answers)):
            if (ladder[i]==answers[i]):
                sum+=float(marks[i])

        std.append([id,sum])
    return std
