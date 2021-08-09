from django.forms import ModelForm

from commentapp.models import Comment


class CommentCrationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']