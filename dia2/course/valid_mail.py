def func(*args):
    print([arg for arg in args])

func()
func("a")
func("a", 1)
func(1,2,3)