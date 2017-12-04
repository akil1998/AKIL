import wolframalpha
import wikipedia
while True:
    a=input("quiestion:")
    try:
        app_id="L7PRE7-2UWJGRQ6AU"
        client=wolframalpha.Client(app_id)
        res=client.query(a)
        answer=next(res.results).text
        print(answer)
    except:
        a=a.split(' ')
        a=" ".join(a[2:])
        print(wikipedia.summary(a))
