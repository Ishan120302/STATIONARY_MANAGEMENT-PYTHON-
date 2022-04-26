import pymysql as sq
import sys
def main():
    def addpr():
        print("---------------------------------Add Product------------------------------------")
        idp=int(input("Enter Product ID:"))
        n=input("Enter Product Name:")
        t=input("Enter Product type:")
        t=t.capitalize()
        q=int(input("Enter quantity of product:"))
        r=int(input("Enter rating (0-10):"))
        qu="insert into prd values({},'{}','{}',{},{})"
        myc.execute(qu.format(idp,n,t,q,r))
        print("Adding product id:",idp,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r)
        b=input("Do you want to continue(Y/N):")
        if b in ['Y','y']:
            con.commit()
            print("Added product id:",idp,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r)
            main()
        elif b in ['N','n']:
            con.rollback()
            print ("Process Cancelled\nExiting.......................................")
            main()
        else:
            print("Enter Valid Response")
            addpr()

    def rempr():
        print("---------------------------------Remove Product------------------------------------")
        a=int(input("Enter Product Id:"))
        qu="delete from prd where pr_id={}"
        qu2="select * from prd where pr_id={}"
        myc.execute(qu2.format(a))
        cur=myc.fetchone()
        n,t,q,r=cur[1],cur[2],cur[3],cur[4]
        myc.execute(qu.format(a))
        print("Removing product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r)
        b=input("Do you want to continue(Y/N):")
        if b in ['Y','y']:
            con.commit()
            print("Removed product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r)
            main()
        elif b in ['N','n']:
            con.rollback()
            print ("Process Cancelled\nExiting.......................................")
            main()
        else:
            print("Enter Valid Response")
            rempr()
    def cquan():
        print("---------------------------------Change Product Quantity----------------------")
        a=int(input("Enter Product Id:"))
        qu="update prd set quan={} where pr_id={}"
        qu2="select * from prd where pr_id={}"
        myc.execute(qu2.format(a))
        cur=myc.fetchone()
        n,t,q,r=cur[1],cur[2],cur[3],cur[4]
        z=int(input("Enter New Product Quantity:"))
        myc.execute(qu.format(z,a))
        print("Changing product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q," To New Quantity:",z,"\nRating:",r)
        b=input("Do you want to continue(Y/N):")
        if b in ['Y','y']:
            con.commit()
            print("Changed product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",z,"\nRating:",r)
            main()
        elif b in ['N','n']:
            con.rollback()
            print ("Process Cancelled\nExiting.......................................")
            main()
        else:
            print("Enter Valid Response")
            cquan()
    def crate():
        print("---------------------------------Change Product Rating---------------------------")
        a=int(input("Enter Product Id:"))
        qu="update prd set rate={} where pr_id={}"
        qu2="select * from prd where pr_id={}"
        myc.execute(qu2.format(a))
        cur=myc.fetchone()
        n,t,q,r=cur[1],cur[2],cur[3],cur[4]
        z=int(input("Enter New Product Rating:"))
        myc.execute(qu.format(z,a))
        print("Changing product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r," To Rating:",z)
        b=input("Do you want to continue(Y/N):")
        if b in ['Y','y']:
            con.commit()
            print("Changed product id:",a,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",z)
            main()
        elif b in ['N','n']:
            con.rollback()
            print ("Process Cancelled\nExiting.......................................")
            main()
        else:
            print("Enter Valid Response")
            crate()
    def search():
        print("---------------------------------Search Product---------------------------")
        print("Search by==>\n1)Product ID\n2)Name\n3)Type\n4)Advanced Search\n5)Exit To Menu")
        a=input("Enter choice to continue:")
        def idsearch():
            x=int(input("Enter product ID:"))
            qu2="select * from prd where pr_id={}"
            myc.execute(qu2.format(x))
            cur=myc.fetchone()
            n,t,q,r=cur[1],cur[2],cur[3],cur[4]
            print("Product id:",x,"\nProduct name:",n,"\nType:",t,"\nQuantity:",q,"\nRating:",r)
            main()
        def nsearch():
            x=(input("Enter Name to search:"))
            print("Sort By==>\n1)Quantity\n2)Rating\n3)Do not sort")
            j=input("Enter choice to continue:")
            if j in ['1','1)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where name like '%{}%' order by quan asc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where name like '%{}%' order by quan desc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['2','2)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where name like '%{}%' order by rate asc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where name like '%{}%' order by rate desc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['3','3)']:
                qu2="select * from prd where name like '%{}%'"
                rec=myc.fetchall()
                print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                for row in rec:
                    print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
        def tsearch():
            x=(input("Enter Type to search:"))
            print("Sort By==>\n1)Quantity\n2)Rating\n3)Do not sort")
            j=input("Enter choice to continue:")
            if j in ['1','1)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where type like '%{}%' order by quan asc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where type like '%{}%' order by quan desc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['2','2)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where type like '%{}%' order by rate asc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where type like '%{}%' order by rate desc"
                    myc.execute(qu2.format(x))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['3','3)']:
                qu2="select * from prd where type like '%{}%'"
                rec=myc.fetchall()
                print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                for row in rec:
                    print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
        def advsearch():
            x=(input("Enter Name to search:"))
            y=(input("Enter Type to search:"))
            print("Sort By==>\n1)Quantity\n2)Rating\n3)Do not sort")
            j=input("Enter choice to continue:")
            if j in ['1','1)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where name like '%{}%' and type like '%{}%' order by quan asc"
                    myc.execute(qu2.format(x,y))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where name like '%{}%' and type like '%{}%' order by quan desc"
                    myc.execute(qu2.format(x,y))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['2','2)']:
                print("1)Ascending\n2)Decending")
                k=input("Enter choice to continue:")
                if k in ['1','1)']:  
                    qu2="select * from prd where name like '%{}%' and type like '%{}%' order by rate asc"
                    myc.execute(qu2.format(x,y))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
                elif k in ['2','2)']:  
                    qu2="select * from prd where name like '%{}%' and type like '%{}%' order by rate desc"
                    myc.execute(qu2.format(x,y))
                    rec=myc.fetchall()
                    print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                    for row in rec:
                        print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
            elif j in ['3','3)']:
                qu2="select * from prd where name like '%{}%' and type like '%{}%'"
                rec=myc.fetchall()
                print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
                for row in rec:
                    print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
        if a in ['1','1)']:
            idsearch()
        elif a in ['2','2)']:
            nsearch()
        elif a in ['3','3)']:
            tsearch()
        elif a in ['4','4)']:
            advsearch()
        elif a in ['5','5)']:
            main()
    def dispall():
        print("----------------------------All Products--------------------------------")
        myc.execute("select * from prd")
        rec=myc.fetchall()
        print('Prod_ID'.ljust(15),'Name'.rjust(0),'Type'.rjust(15),'Quantity'.rjust(15),'Rating'.rjust(14))
        for row in rec:
            print(str(row[0]).rjust(4),str(row[1]).rjust(15),str(row[2]).rjust(15),str(row[3]).rjust(12),str(row[4]).rjust(15))
        main()
    print("-------------------------------Product Management-------------------------------")
    print("Menu\n1)Add New Product\n2)Remove Existing Product(By PR_ID)\n3)Change Quantity of Product(By PR_ID)\n4)Search For Product\n5)Change Rating for Product(By PR_ID)\n6)Display All Product\n7)Exit")
    a=(input("Enter your choice(1/2/3/4/5/6/7):"))
    if a in ['1','1)']:
        addpr()
        main()
    elif a in ['2','2)']:
        rempr()
        main()
    elif a in ['3','3)']:
        cquan()
        main()
    elif a in ['4','4)']:
        search()
        main()
    elif a in ['5','5)']:
        crate()
        main()
    elif a in ['6','6)']:
        dispall()
        main()
    elif a in ['7','7)']:
        print("Exiting..........................................")
        sys.exit()


con=sq.connect(user='root',password='sunbeam',host='localhost')
myc=con.cursor()
ch=input("Do you want to create new Product Management Software(Y/N):")
if ch in ['Y','y']:
    myc.execute('create database if not exists product')
    myc.execute('use product')
    myc.execute('create table if not exists prd(pr_id int(4) primary key,name varchar(50),type varchar(15),quan int(4),rate int(2))')
else:
    print('Exiting....................................')
con=sq.connect(user='root',password='sunbeam',host='localhost',database='product')
myc=con.cursor()
main()
