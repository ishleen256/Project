"""
create table Customer(
   id int primary key auto_increment,
   name varchar(256),
   phone varchar(10),
   email varchar(256),
   created_on datetime DEFAULT CURRENT_TIMESTAMP,
   remarks varchar(1024),
   points int DEFAULT 100,
   type int Default 1
   );
DELETE FROM Customer WHERE Name='John';




"""




class Customer:
    def __init__(self, id="none", name="none", phone="none", email="none", created_on="none", remarks="none",
                 points="none", type="none"):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.created_on = created_on
        self.remarks = remarks
        self.points = points
        self.type = type

    def insert_sql(self):
        return"insert into Customer(name,phone,email,remarks)values('{name}','{phone}','{email}','{remarks}')".format_map(vars(self))

    def update_sql(self):
        pass


    def delete_sql(self):
        return"delete from Customer where id= {}".format(self.id)

    def select_sql(self):
        return"select * from Customer"

    def select_sql_where(self):
        return "select * from Customer where id = {}".format(self.id)



c1 = Customer()
print(vars(c1))
