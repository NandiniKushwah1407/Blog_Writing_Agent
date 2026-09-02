from graph import app

def main():
    out = app.invoke({
        "topic": "Write a blog on Self Introduction in an interview", "sections":[]
    })
    print(out)

if __name__ == "__main__":
    main()