from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    college = models.CharField(max_length=20, blank=True, null=True)
    school = models.CharField(max_length=20, blank=True, null=True)
    cource = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ManyToManyField('users.User',  blank=True)
    num = models.IntegerField(default=0)
    liked_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="講義の感想・評価")
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    like = models.OneToOneField(Like, on_delete=models.CASCADE, default=False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username





















