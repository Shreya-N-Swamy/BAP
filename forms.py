from django import forms


class EmailForm(forms.Form):
    fromWho = forms.CharField(max_length=25)
    fromEmail = forms.EmailField()
    toEmail = forms.EmailField()
    mailContent = forms.CharField(required=False,
                                  widget=forms.Textarea)
