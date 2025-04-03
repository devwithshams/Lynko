from django import forms

from .models import Category, Link

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('category', 'name', 'description', 'url')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view

        super().__init__(*args, **kwargs)
        # Filter categories based on 'is_active' being True
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user, is_active=True)
