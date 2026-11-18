from django.db import models

# Create your models here.
class Employee(models.Model):
	name=models.CharField(max_length=10)
	address=models.CharField(max_length=20)

	def __str__(self):
		return self.name
	class Meta:
		db_table='myapp_employee'


#ORM-Object Relational Mapping
#datatypes-Field type
#IntegerField(),DecimalField()
#BigIntegerField()
#EmailField()
#DateField()
#DateTimeField()
#TextField(),
# CharField()-256
#ImageField()
#FileField()

#__str_:The __str__ method just tells Django what to print when 
# it needs to print out an instance of the any model.

# python manage.py makemigrations
# python manage.py migrate


# create table myapp_employee(id int primary key,name varchar(100), address varchar(100));