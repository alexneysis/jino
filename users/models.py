from django.db import models


class User(models.Model):
    class Meta:
        db_table = "users"

    id_user = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=19)
    email = models.CharField(max_length=255, blank=True, null=True)


class Status(models.Model):
    class Meta:
        db_table = "status"

    status = models.IntegerField(primary_key=True)


class Clinic(models.Model):
    class Meta:
        db_table = "clinics"

    id_clinic = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Pool(models.Model):
    class Meta:
        db_table = "pool"

    id_user = models.ForeignKey(User, on_delete=models.CASCADE, )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


class RecordedUsers(models.Model):
    class Meta:
        db_table = "recorded_users"

    id_recorded = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date = models.DateTimeField()


class History(models.Model):
    class Meta:
        db_table = "history"

    id_history = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    status_before = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_before')
    status_after = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status_after')
    date = models.DateTimeField()
