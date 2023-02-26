from django.db import models

# Create your models here.
class Categories(models.Model):
    cat_id = models.CharField(max_length=10, primary_key=True, default="")
    cat_name = models.CharField(max_length=50, default="")
    cat_desc = models.TextField(default="")
    def __str__(self):
        return self.cat_id + ":" + self.cat_name

class Contents(models.Model):
    cont_id = models.CharField(max_length=10, primary_key=True, default="",db_column="cont_id")
    cont_name = models.CharField(max_length=50, default="")
    content = models.TextField(default="")
    cont_address = models.TextField(default="")
    cont_image = models.ImageField(upload_to ='static/images/Content/', default="")
    cont_date = models.DateField(default=None)
    cont_phonenumber = models.CharField(max_length=15, default="")
    cont_email = models.CharField(max_length=70, default="")
    cat_id = models.ForeignKey(Categories ,on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.cont_id + " : " + self.cont_name + "   " + self.content




