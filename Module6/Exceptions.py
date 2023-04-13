def foo():
    try:
        raise ValueError()
    except Exception as e:
        print("wow")
        #raise Exception()
    finally:
        print("gg")
        
        
try:
    foo()
except Exception:
    print("okay")