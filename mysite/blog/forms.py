from  django import  forms
# Form: Allows you to build standard forms by defining fields and validations


class EmailPostForm(forms.Form):
    name =  forms.CharField(max_length=25)
    #name: An instance of CharField with
    # a maximum length of 25 characters. We will use it for the
    # name of the person sending the post.
    email  = forms.EmailField()
    #email: An instance of EmailField. We will use the email of the person sending the post recommendation.
    to  = forms.EmailField()
    #An instance of EmailField we use the email of recipient , who will recieve email recommending post recommendation
    Comments  =  forms.CharField(required=False,widget=forms.Textarea)
    #An instance of  CharField we use  it  for comments  to include in  post recommendation email