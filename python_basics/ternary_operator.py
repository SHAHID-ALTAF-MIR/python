pcm = True
passed = True   # better to avoid using 'pass' since it's a Python keyword

print("selected") if pcm and passed else print("not selected")
