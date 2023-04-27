def my_function(a,b):
      print('my name is {} {}'.format(a,b))

def my_function2(* args):
      print('my name is {} {}'.format(args[0],args[1]))

def my_function3(**args):
      print('my name is {} {}'.format(args['b'],args['a']))


my_function(b = "ASSOGBA", a = "Charbel")

my_function2("ASSOGBA", "Charbel")

my_function3(b = "ASSOGBA", a = "Charbel")