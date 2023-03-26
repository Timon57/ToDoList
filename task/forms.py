from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Task Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea({'class':'form-control'}),label = 'Descripton',max_length = 1000,required = False)
    date_completed = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control'}),label = 'Due date', required=False)
    completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}),label = 'Completed?', required=False)
