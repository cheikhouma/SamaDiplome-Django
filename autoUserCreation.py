from django.contrib.auth.models import User

user = User.objects.all()

new1 = User.objects.create_user(
first_name="Matar",
last_name="Faly",
username="matarfaly",
email="matarfaly@ept.sn",
password="matarek"
)

new2 = User.objects.create_user(
first_name="Bar",
last_name="LeVaran",
username="barlevaran",
email="bar@ept.sn",
password="dragon"
)

new1.save()
new2.save()

