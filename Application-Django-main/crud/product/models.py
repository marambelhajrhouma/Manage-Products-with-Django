from django.db import models

# Create your models here.

# models->module
# models.Model: classe de base(deDjango)->vous permet d'hériter lorsque vous définissez un modèle de données 
#-->Permet de créer une table de BDD: lorqu'on fait les migrations
class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    details = models.TextField()
    # Field ->champs dans BDD

    def __str__(self):
        return "%s" % (self.pname)

    class Meta:
        db_table = "product"
        #class Meta avec db_table permet de personnaliser tab product (dans BDD)

#_____présente la BDD de projet pour définir les modèles de données