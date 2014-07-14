from django import forms
from store.models import Product


#==========================================================================
# Product Admin
#==========================================================================
class ProductAdminForm(forms.ModelForm):
    """
    The Admin form for Product
    """

    class Meta:
        model = Product

    def clean_price(self):
        """
        Must make sure this product has a non-negative price

        :return: The price
        """
        if self.cleaned_data['default_price'] <= 0 :
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['default_price']