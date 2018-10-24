from django import forms


class PostCreateForm(forms.Form):
    photo = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control-file'
            }
        )
    )
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
            }
        ),
    )

    #widget를 쓰는이유는 class를 적용하기 위해서이다?