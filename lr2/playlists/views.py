from django.shortcuts import render
from .forms import PreferencesForm, SongForm

def index(request):
    songs = [
        {"title": "Song A", "artist": "Artist 1"},
        {"title": "Song B", "artist": "Artist 2"},
        {"title": "Song C", "artist": "Artist 3"},
    ]
    theme = request.COOKIES.get("theme", "light")
    language = request.COOKIES.get("language", "en")

    pref_form = PreferencesForm(initial={"theme": theme, "language": language})
    song_form = SongForm()

    if request.method == "POST":
        if "theme" in request.POST and "language" in request.POST:
            pref_form = PreferencesForm(request.POST)
            if pref_form.is_valid():
                theme = pref_form.cleaned_data["theme"]
                language = pref_form.cleaned_data["language"]

        elif "title" in request.POST and "artist" in request.POST:
            song_form = SongForm(request.POST)
            if song_form.is_valid():
                songs.append({
                    "title": song_form.cleaned_data["title"],
                    "artist": song_form.cleaned_data["artist"]
                })

    response = render(request, "index.html", {
        "songs": songs,
        "theme": theme,
        "language": language,
        "pref_form": pref_form,
        "song_form": song_form
    })

    response.set_cookie("theme", theme)
    response.set_cookie("language", language)

    return response
