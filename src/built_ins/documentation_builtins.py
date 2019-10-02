dir_info = "\n".join((dir(__builtins__)))
print(dir_info)

"""
##############Exceptions #################### 
Exception -> All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.

ArithmeticError -> The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError

AssertionError -> Raised when an assert statement fails.

AttributeError -> Raised when an attribute reference or assignment fails. (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)

BaseException -> The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined classes (for that, use Exception)

BlockingIOError -> Raised when an operation would block on an object (e.g. socket) set for non-blocking operation. Corresponds to errno EAGAIN, EALREADY, EWOULDBLOCK and EINPROGRESS.

BrokenPipeError -> A subclass of ConnectionError, raised when trying to write on a pipe while the other end has been closed, or trying to write on a socket which has been shutdown for writing. Corresponds to errno EPIPE and ESHUTDOWN.

BufferError -> Raised when a buffer related operation cannot be performed.

ChildProcessError -> Raised when an operation on a child process failed. Corresponds to errno ECHILD.

ConnectionAbortedError -> A subclass of ConnectionError, raised when a connection attempt is aborted by the peer. Corresponds to errno ECONNABORTED.

ConnectionError -> A base class for connection-related issues.

ConnectionRefusedError -> A subclass of ConnectionError, raised when a connection attempt is refused by the peer. Corresponds to errno ECONNREFUSED.

ConnectionResetError -> A subclass of ConnectionError, raised when a connection is reset by the peer. Corresponds to errno ECONNRESET.

EOFError -> Raised when the input() function hits an end-of-file condition (EOF) without reading any data.

EnvironmentError -> kept for compatibility with previous versions; starting from Python 3.3, they are aliases of OSError.

FileExistsError -> Raised when trying to create a file or directory which already exists. Corresponds to errno EEXIST.

FileNotFoundError -> aised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.

FloatingPointError -> Not currently used.

GeneratorExit -> Exception: Raised when a generator or coroutine is closed; see generator.close() and coroutine.close()

IOError -> kept for compatibility with previous versions; starting from Python 3.3, they are aliases of OSError.

ImportError -> Raised when the import statement has troubles trying to load a module. Also raised when the “from list” in from ... import has a name that cannot be found.

IndentationError -> Base class for syntax errors related to incorrect indentation. This is a subclass of SyntaxError.

IndexError -> Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)

InterruptedError -> Raised when a system call is interrupted by an incoming signal. Corresponds to errno EINTR.

IsADirectoryError -> Raised when a file operation (such as os.remove()) is requested on a directory. Corresponds to errno EISDIR.

KeyError -> Raised when a mapping (dictionary) key is not found in the set of existing keys.

KeyboardInterrupt -> Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.

LookupError -> The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid: IndexError, KeyError.

MemoryError -> Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects).

ModuleNotFoundError ->A subclass of ImportError which is raised by import when a module could not be located. It is also raised when None is found in sys.modules.

NameError ->Raised when a local or global name is not found. This applies only to unqualified names. The associated value is an error message that includes the name that could not be found.

NotADirectoryError -> Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory. Corresponds to errno ENOTDIR.

NotImplementedError ->This exception is derived from RuntimeError. In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method, or while the class is being developed to indicate that the real implementation still needs to be added.

OSError -> This exception is raised when a system function returns a system-related error, including I/O failures such as “file not found” or “disk full” (not for illegal argument types or other incidental errors).

OverflowError ->Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for integers (which would rather raise MemoryError than give up).

PermissionError -> Raised when trying to run an operation without the adequate access rights - for example filesystem permissions. Corresponds to errno EACCES and EPERM.

ProcessLookupError -> Raised when a given process doesn’t exist. Corresponds to errno ESRCH.

RecursionError -> This exception is derived from RuntimeError. It is raised when the interpreter detects that the maximum recursion depth (see sys.getrecursionlimit()) is exceeded.

ReferenceError -> This exception is raised when a weak reference proxy, created by the weakref.proxy() function, is used to access an attribute of the referent after it has been garbage collected. For more information on weak references, see the weakref module.

RuntimeError -> Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong.

StopAsyncIteration -> Must be raised by __anext__() method of an asynchronous iterator object to stop the iteration.

StopIteration -> Raised by built-in function next() and an iterator’s __next__() method to signal that there are no further items produced by the iterator.

SyntaxError -> Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions exec() or eval(), or when reading the initial script or standard input (also interactively).

SystemError -> Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms).

SystemExit -> This exception is raised by the sys.exit() function. It inherits from BaseException instead of Exception so that it is not accidentally caught by code that catches Exception. This allows the exception to properly propagate up and cause the interpreter to exit. When it is not handled, the Python interpreter exits; no stack traceback is printed. 

TabError -> Raised when indentation contains an inconsistent use of tabs and spaces. This is a subclass of IndentationError.

TimeoutError -> Raised when a system function timed out at the system level. Corresponds to errno ETIMEDOUT.

TypeError -> Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.

UnboundLocalError -> Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. This is a subclass of NameError.

UnicodeDecodeError -> Raised when a Unicode-related error occurs during decoding. It is a subclass of UnicodeError.

UnicodeEncodeError -> Raised when a Unicode-related error occurs during encoding. It is a subclass of UnicodeError.

UnicodeError -> Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of ValueError.

UnicodeTranslateError -> Raised when a Unicode-related error occurs during translating. It is a subclass of UnicodeError.

ValueError -> Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.

WindowsError -> kept for compatibility with previous versions; starting from Python 3.3, they are aliases of OSError. Only on Windows
ZeroDivisionError ->Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.


############################ Warnings ############################
Warning -> This is the base class of all warning category classes. It is a subclass of Exception.

UserWarning -> Base class for warnings generated by user code.

DeprecationWarning -> Base class for warnings about deprecated features when those warnings are intended for other Python developers.

PendingDeprecationWarning -> Base class for warnings about features which are obsolete and expected to be deprecated in the future, but are not deprecated at the moment.

SyntaxWarning -> Base class for warnings about dubious syntax.

RuntimeWarning -> Base class for warnings about dubious runtime behavior.

FutureWarning -> Base class for warnings about deprecated features when those warnings are intended for end users of applications that are written in Python.

ImportWarning -> Base class for warnings about probable mistakes in module imports.

UnicodeWarning -> Base class for warnings related to Unicode.

BytesWarning -> Base class for warnings related to bytes and bytearray.

ResourceWarning -> Base class for warnings related to resource usage. Ignored by the default warning filters.


########## Others ##############

Ellipsis -> useful for slicing(Special value used in conjunction with extended slicing syntax.); recognize as ...

False -> the false value of the bool type.

True -> The true value of the bool type.

None -> The sole value of types.NoneType. None is frequently used to represent the absence of a value, as when default arguments are not passed to a function.

NotImplemented-> Special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the operation is not implemented with respect to the other type; may be returned by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.) for the same purpose. Its truth value is true.

__build_class__ -> Internal helper function used by the class statement.

__debug__ -> the built-in variable __debug__ is True under normal circumstances, False when optimization is requested (command line option -O).

__doc__ -> function’s documentation string

__import__ -> imports a module: importlib.__import__

__loader__ -> The loader used to load the module. 


__name__ -> The __name__ attribute must be set to the fully-qualified name of the module. This name is used to uniquely identify the module in the import system; used for eg to see if a module is imported by anoter module or run as a script

__package__ -> Its value must be a string, but it can be the same value as its __name__. When the module is a package, its __package__ value should be set to its __name__. When the module is not a package, __package__ should be set to the empty string for top-level modules, or for submodules, to the parent package’s name.

__spec__ -> The __spec__ attribute must be set to the module spec that was used when importing the module. This is used primarily for introspection and during reloading.

abs -> Return the absolute value of the argument

all -> Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.

any - > Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.

ascii ->  Return an ASCII-only representation of an object.

bin -> Return the binary representation of an integer.

bool ->  Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.

!! breakpoint -> Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept whatever arguments are passed. By default, this drops you into the pdb debugger.

bytearray ->  Construct a mutable bytearray object from: an iterable yielding integers in range(256)/ a text string encoded using the specified encoding/ a bytes or a buffer object/ any object implementing the buffer API./ an integer

bytes -> Construct an immutable array of bytes from: an iterable yielding integers in range(256)/ a text string encoded using the specified encoding/ any object implementing the buffer API/ an integer

callable -> Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances of classes with a__call__() method.

chr -> Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

classmethod -> A class method receives the class as implicit first argument, just like an instance method receives the instance.

compile -> The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).
    codeInString = 'a = 1\nb=2\nsum=a+b\nprint("sum =",sum)'
    codeObejct = compile(codeInString, 'sumstring', 'exec')
    exec(codeObejct)

complex -> Create a complex number from a real part and an optional imaginary part.

copyright -> interactive prompt objects for printing the license text, a list of contributors and the copyright notice.

credits -> interactive prompt objects for printing the license text, a list of contributors and the copyright notice

delattr -> Deletes the named attribute from the given object. delattr(x, 'y') is equivalent to ``del x.y''

dict -> dictionary

dir -> If called without an argument, return the names in the current scope. Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it.

divmod -> Return the tuple (x//y, x%y).  Invariant: div*y + mod == x

enumerate -> The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.

eval -> Evaluate the given source in the context of globals and locals.
    x = 1
    print(eval('x + 1'))
    >> 2
    
exec ->Execute the given source in the context of globals and locals.
    x = 1
    exec('x=x + 1')
    print(x)
    >> 2
    
exit -> same as quit, raises SystemExit

filter -> Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true; filter(function or None, iterable) --> filter object

float -> Convert a string or number to a floating point number, if possible.

format -> The built-in format() method returns a formatted representation of the given value controlled by the format specifier.

frozenset ->Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.

getattr -> Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, getattr(x, 'foobar') is equivalent to x.foobar

globals -> Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

hasattr -> The arguments are an object and a string. The result is True if the string is the name of one of the object’s attributes, False if not. 

hash ->Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0)

help -> Invoke the built-in help system.

hex -> Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.

id -> Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

input -> If the prompt argument is present, it is written to standard output without a trailing newline. 

int ->Return an integer object constructed from a number or string x, or return 0 if no arguments are given.

isinstance -> Return true if the object argument is an instance of the classinfo argument, or of a (direct, indirect or virtual) subclass thereof. If object is not an object of the given type, the function always returns false. If classinfo is a tuple of type objects (or recursively, other such tuples), return true if object is an instance of any of the types. If classinfo is not a type or tuple of types and such tuples, a TypeError exception is raised.

issubclass -> Return true if class is a subclass (direct, indirect or virtual) of classinfo. A class is considered a subclass of itself. classinfo may be a tuple of class objects, in which case every entry in classinfo will be checked. In any other case, a TypeError exception is raised.

iter -> Return an iterator object. The first argument is interpreted very differently depending on the presence of the second argument.

len -> Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

license -> Object that when printed, prints the message “Type license() to see the full license text”, and when called, displays the full license text in a pager-like fashion (one screen at a time).

list -> The list() constructor creates a list in Python.

locals -> Update and return a dictionary representing the current local symbol table. Free variables are returned by locals() when it is called in function blocks, but not in class blocks. Note that at the module level, locals() and globals() are the same dictionary.

map -> Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.

max -> Return the largest item in an iterable or the largest of two or more arguments.

memoryview -> Return a “memory view” object created from the given argument.

min -> Return the smallest item in an iterable or the smallest of two or more arguments.

next -> Retrieve the next item from the iterator by calling its __next__() method. If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

object -> Return a new featureless object. object is a base for all classes. It has the methods that are common to all instances of Python classes. This function does not accept any arguments.

oct -> Convert an integer number to an octal string prefixed with “0o”

open -> The open() function opens the file (if possible) and returns a corresponding file object.

ord -> Given a string representing one Unicode character, return an integer representing the Unicode code point of that character. 

pow -> pow(x, y[, z]): The pow() method returns x to the power of y. If the third argument (z) is given, it returns x to the power of y modulus z, i.e. pow(x, y) % z

print -> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False): Print objects to the text stream file, separated by sep and followed by end. sep, end, file and flush, if present, must be given as keyword arguments.

property -> property(fget=None, fset=None, fdel=None, doc=None): Return a property attribute. fget is a function for getting an attribute value. fset is a function for setting an attribute value. fdel is a function for deleting an attribute value. And doc creates a docstring for the attribute.

quit -> same as exit, raises SystemExit

range -> The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.

repr -> Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.

reversed -> reversed(seq): Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0)

round -> round(number[, ndigits]): Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

set -> The set() constructor constructs a Python set from the given iterable and returns it.

setattr -> setattr(object, name, value): This is the counterpart of getattr(). The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.

slice -> slice(start, stop[, step]): Return a slice object representing the set of indices specified by range(start, stop, step). The start and step arguments default to None. Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Python and other third party extensions.

sorted -> sorted(iterable, *, key=None, reverse=False): Return a new sorted list from the items in iterable.

staticmethod -> Transform a method into a static method. A static method does not receive an implicit first argument

str ->str(object=b'', encoding='utf-8', errors='strict'): Return a string version of object. If object is not provided, returns the empty string. Otherwise, the behavior of str() depends on whether encoding or errors is given

sum -> sum(iterable[, start]): Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

super ->super([type[, object-or-type]]): Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.

tuple -> The tuple() built-in is used to create a tuple in Python.

type -> type(name, bases, dict)/ type(object) -> With one argument, return the type of an object.With three arguments, return a new type object

vars -> Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.

zip -> zip(*iterables) Make an iterator that aggregates elements from each of the iterables.
"""