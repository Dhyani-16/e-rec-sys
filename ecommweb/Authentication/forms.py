from django.forms import ModelForm
from .models import Profile

class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','first_name2','last_name','last_name2','contact_no','contact_no2','address1','address2','city','city2','state','state2','pincode','pincode2']        