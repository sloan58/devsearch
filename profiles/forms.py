from django.forms import ModelForm

from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'user',
            'name',
            'username',
            'email',
            'short_intro',
            'bio',
            'profile_image',
            'social_github',
            'social_twitter',
            'social_linkedin',
            'social_youtube',
            'social_website',
        ]
