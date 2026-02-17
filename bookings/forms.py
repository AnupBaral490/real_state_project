from django import forms
from .models import Booking, Inquiry


class BookingForm(forms.ModelForm):
    requested_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local',
            'placeholder': 'Select date & time'
        }),
        help_text='Select your preferred visit date and time'
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Any special requests or questions? (Optional)'
        })
    )

    class Meta:
        model = Booking
        fields = ['requested_date', 'message']


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['email', 'phone', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your phone number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Your message or inquiry...'
            })
        }
