from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200);
    item_desc = models.CharField(max_length=200);
    item_price = models.IntegerField();
    item_image = models.CharField(max_length=500, default="https://hips.hearstapps.com/hmg-prod/images/detroit-style-pizza-recipe-1-64429e4a2e324.jpg?crop=0.974xw:0.974xh;0.0255xw,0&resize=640:*")
    
class Order(models.Model):
    def __str__(self):
        return super().__str__()
    
    item_order = models.ForeignKey(Item, on_delete=models.CASCADE);
    order_date = models.DateTimeField(auto_now_add=True);   
    order_status = models.CharField(max_length=200);
