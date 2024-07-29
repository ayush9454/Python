def add_bullets_to_wiki_markup(wiki_text):
  
    lines = wiki_text.split('\n')
    
    bulleted_lines = ['* ' + line for line in lines]
    
    bulleted_text = '\n'.join(bulleted_lines)
    
    return bulleted_text

wiki_markup = """
Item 1
Item 2
Item 3
Item 4
"""

bulleted_wiki_markup = add_bullets_to_wiki_markup(wiki_markup.strip())

print("Original Wiki Markup:\n", wiki_markup)
print("\nBulleted Wiki Markup:\n", bulleted_wiki_markup)
