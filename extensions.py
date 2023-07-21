def main():
    file = input("File name: ")
    findFormat(file)

def findFormat(format):
    if format.endswith(".jpg") or format.endswith(".jpeg"):
        print("image/jpeg")
    elif format.endswith(".png"):
        print("image/png")
    elif format.endswith(".gif"):
        print("image/gif")
    elif format.endswith(".pdf"):
        print("application/pdf")
    elif format.endswith(".zip"):
        print("application/zip")
    elif format.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

main()