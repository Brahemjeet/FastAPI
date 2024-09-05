from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

    
def test_post_a_book():
    response = client.post("/book/",
                           json = {
                               "year": 202,
                               "title": "ABC",
                               "author" : "Author"
                           })
    print(response.text)
   
   
def main():
    test_post_a_book()
    
if __name__ == "__main__":
    main()