import wikipedia

def show_suggestion(keyword):
    suggestions=wikipedia.search(keyword, results=10, suggestion=True)
    if suggestions[0]==[]:
        return "Sorry, The provided keyword may be invalid Check for spelling mistakes."
    return suggestions[0]

def wiki_content(keyword):
    wikiText = wikipedia.page(keyword)
    return wikiText.content