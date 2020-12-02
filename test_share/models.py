from django.db import models
from app.models import Subject, Like
from django.utils import timezone

class Test_Image(models.Model):
    YEAR_CHOICES = []
    for y in range(timezone.now().year, timezone.now().year - 10 , -1):
        YEAR_CHOICES.append((y, y))
    TITLE_CHOICES = [
        ('中間テスト', '中間テスト'),
        ('期末テスト', '期末テスト'),
        ('レポート', 'レポート'),
        ('小テスト', '小テスト'),
        ('授業資料', '授業資料'),
        ('その他', 'その他'),
    ]
    image = models.ImageField(upload_to='test_image')
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="テスト実施年度", choices=YEAR_CHOICES, default=timezone.now().year)
    title = models.CharField(choices=TITLE_CHOICES, max_length=50, default='中間テスト')
    comment = models.TextField(verbose_name="テストへのコメント", blank=True, null=True)
    like = models.OneToOneField(Like, on_delete=models.CASCADE)

    def __str__(self):
        return self.title