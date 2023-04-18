# INSERT
from members.models import Member
Member.objects.all()
member = Member(firstname='Emil', lastname='Refsnes')
member.save()
Member.objects.all().values()

#UPDATE DATA
x = Member.objects.all()[4]
x.firstname = "Stalikken"
x.save()

#DELETE
x = Member.objects.all()[5]
x.delete()

#UPDATE MODEL
# class Member(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)
#   phone = models.IntegerField()
#   joined_date = models.DateField()
# py manage.py makemigrations members
# AFTER THIS WILL THROW ERROR THEN NEED TO CHANGE fields to null
# phone = models.IntegerField(null=True)
# joined_date = models.DateField(null=True)
# py manage.py makemigrations members
# py manage.py makemigrations members
# py manage.py migrate