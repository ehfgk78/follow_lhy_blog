from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'content',
                'placeholder': '댓글 달기...',
            }
        )
    )
