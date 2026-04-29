from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    credits = models.IntegerField()
    hours = models.CharField(max_length=10)
    status = models.CharField(max_length=20, default="Draft")
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    hours = models.IntegerField()
    content = models.TextField(default="NA")
    hands_on = models.TextField(default="NA")
    self_learning = models.TextField(default="NA")

    def __str__(self):
        return self.title


class CO(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description


class COPOMapping(models.Model):
    co = models.ForeignKey(CO, on_delete=models.CASCADE)
    po = models.IntegerField()  # 1 to 7
    value = models.IntegerField()  # 1,2,3

    def __str__(self):
        return f"{self.co} - PO{self.po}"

