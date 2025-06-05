filetypes = [
    {'.jpg': 'picture'},
    {'.jpeg': 'picture'},
    {'.pdf': 'document'},
    {'.txt': 'document'},
    {'.zip': 'file'}
]

def identify(file_type):
    for _ in filetypes:
        if user_files in _:
                print (_)
        break
   

def main():
    users_file = input ("please insert your file type with '.' format? ").lower().strip()
    result = identify(users_file)
    print(f"Your file type is: {result}")


main()

# ask user for media type




