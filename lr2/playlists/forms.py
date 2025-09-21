from django import forms

class PreferencesForm(forms.Form):
    THEME_CHOICES = [
        ("light", "Светлая"),
        ("dark", "Тёмная"),
    ]
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("ru", "Русский"),
    ]

    theme = forms.ChoiceField(choices=THEME_CHOICES, label="Тема")
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, label="Язык")


class SongForm(forms.Form):
    title = forms.CharField(max_length=100, label="Название композиции")
    artist = forms.CharField(max_length=100, label="Исполнитель")
