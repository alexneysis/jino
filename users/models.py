from django.db import models


class Status(models.Model):
    class Meta:
        db_table = "status"

    status = models.IntegerField(primary_key=True)


class Client(models.Model):
    class Meta:
        db_table = "clients"

    id_client = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)


class Clinic(models.Model):
    class Meta:
        db_table = "clinics"

    id_clinic = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class History(models.Model):
    class Meta:
        db_table = "history"

    id_history = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    status_before = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_before')
    status_after = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_after')
    date = models.DateTimeField()
