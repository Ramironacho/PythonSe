def exceptionHandling(key):
    try:
        car = {'make': 'BMW', 'model': '550i', 'year': 2018}
        print(car[key])
    except:
        print("exception block")
    finally:
        print("finally block")

exceptionHandling('color')