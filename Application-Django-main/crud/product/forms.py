from django import forms
from product import models

# forms et models sont des modules
class ProductForm(forms.ModelForm):

     class Meta:
        model = models.Product
        # le model associé à form: Product
        fields = "__all__"
        # stocker tous les Fields dans BDD automatiqement