# Create a new model called 'User' with the information above.

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # userManager = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.first_name, self.last_name, self.email_address, self.age)

# Successfully create and run the migration files

python manage.py makemigrations
python manage.py migrate

# Using the shell...

pip install ipython
python manage.py shell
In [1]: from apps.user_login.models import User

# Create a few records in the users

In [2]: User.objects.create(first_name = "Abby", last_name = "Ramiscal", email_address = "abby@ramiscal.com", age = "9")
   ...:
Out[2]: <User: User object>

In [3]: User.objects.create(first_name = "Bella", last_name = "Ramiscal", email_address = "bella@ramiscal.com", age = "1
   ...: 0")
Out[3]: <User: User object>

In [4]: User.objects.create(first_name = "Girly", last_name = "Ramiscal", email_address = "girly@ramiscal.com", age = "1
   ...: 4")
Out[4]: <User: User object>

# See if it allows you to insert some records when the fields are not meeting the validation rules we set (e.g. try to create a record where age is 5 or above 150, or where the first name is just one character, etc).

# Make sure your console returns appropriate error messages when you try to save something that's not meeting the validation rules.


# Know how to retrieve all users.

In [2]: print User.objects.all()
<QuerySet [<User object: Abby Ramiscal abby@ramiscal.com 9>, <User object: Bella Ramiscal bella@ramiscal.com 10>, <User object: Girly Ramiscal girly@ramiscal.com 14>]>

# Know how to get the first user.

In [4]: User.objects.first()
Out[4]: <User object: Abby Ramiscal abby@ramiscal.com 9>

# Know how to get the last user.

In [5]: User.objects.last()
Out[5]: <User object: Girly Ramiscal girly@ramiscal.com 14>

# Know how to get the users sorted by their first name (order by first_name DESC)

In [16]: User.objects.order_by("first_name")
Out[16]: <QuerySet [<User object: Abby Ramiscal abby@ramiscal.com 9>, <User object: Bella Ramiscal bella@ramiscal.com 10>, <User object: Girly Ramiscal girly@ramiscal.com 14>]>

# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save

In [17]: User.objects.get(id=3)
Out[17]: <User object: Girly Ramiscal girly@ramiscal.com 14>

In [18]: b = User.objects.get(id=3)

In [19]: b.first_name
Out[19]: u'Girly'

In [20]: b.last_name
Out[20]: u'Ramiscal'

In [21]: b.last_name = "Egana"

In [22]: b
Out[22]: <User object: Girly Egana girly@ramiscal.com 14>


# Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...)

In [23]: User.objects.create(first_name = "Test", last_name = "Testy", email_address = "test@test.com", age = "2")
Out[23]: <User object: Test Testy test@test.com 2>

In [24]: print User.objects.all()
<QuerySet [<User object: Abby Ramiscal abby@ramiscal.com 9>, <User object: Bella Ramiscal bella@ramiscal.com 10>, <User object: Girly Ramiscal girly@ramiscal.com 14>, <User object: Test Testy test@test.com 2>]>

In [25]: User.objects.get(id=4).delete()
Out[25]: (1, {u'user_login.User': 1})

In [26]: print User.objects.all()
<QuerySet [<User object: Abby Ramiscal abby@ramiscal.com 9>, <User object: Bella Ramiscal bella@ramiscal.com 10>, <User object: Girly Ramiscal girly@ramiscal.com 14>]>
