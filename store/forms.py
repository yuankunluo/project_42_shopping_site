from django import forms
from store.models import Product


#==========================================================================
# ProductAdmin
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




#==========================================================================
# ProductAddToCart
#==========================================================================
class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={'size':2, 'value':1, 'class':'quantity', 'maxlength':'5'}),
        error_messages={'invalid':'Please Input the right number'},
        min_value=1)
    product_slug = forms.CharField(widget=forms.HiddenInput())


    def __init__(self, request=None, *args, **kwargs):
        """
        override the default __init__ so we can set the request

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        custom validation to check for cookies

        :return:
        """
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data
