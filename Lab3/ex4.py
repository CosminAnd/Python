def build_xml_element (tag, content, **elements):   # ** -> elements va fi considerat un dictionar
    # separator.join(iterable object)
    sep = ', '
    return "<{} {} >{}</{}>".format(tag, sep.join(["{}=\{}\ ".format(key, value) for key, value in elements.items()]), content, tag)


print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ", div= "myDiv"))


"""
The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
https://www.w3schools.com/python/ref_string_join.asp

The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}
https://www.w3schools.com/python/ref_string_format.asp
"""