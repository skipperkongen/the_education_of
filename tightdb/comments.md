# My comments on syntax

This code has been commented by Kostas. These are my initial reactions to the Python extensions "syntax". I'm being as annoying/honest as possible. I apologize in advance.

```python
# A: Create a new shared group
db = tightdb.SharedGroup("shared_db.tightdb")
if not db.is_valid():
    print "Could not open group"
# COMMENTS ON SECTION A
# A1: Minor thing, the SharedGroup class name seems a little strange, when I'm assigning to something called 'db'
#   I was thinking, what is a shared group, and why do I need it? I just want a database... again, this is a minor thing.

# B: Do a write transaction
with db as group:
    # add a single table with two initial rows
    t = group.create_table('table1', ["name",  "string",
                                      "age",   "int",
                                      "hired", "bool"],
                           [["joe",     42, False], # initial rows
                            ["jessica", 22, True]])
# COMMENTS ON SECTION B
# B1: strange that 'with' construct is (almost) mandatory (altenative is to call __enter__/__exit__ yourself)
#   Contrast this with using 'with' for file objects, where it is optional and just a convenience (auto-call close() and such)...
#   conclusion B1: I think 'with' should offered as a convenience to the programmer, not something you have to use.
# B2: create_table, I'm not a fan of the 'alternating' field-name, field-type, and that types are strings. 
#   I'd much prefer kwargs:
#     create_table('table1', name=str, age=int, hired=bool)
# B3: create_table, I'd prefer not having row initialization in there. How useful is that really anyway? 
#   it only seems useful for this kind of tutorial code (a table with two dummy items in it)
# B4: Again, the group name confused me a little. "Why is my database a group?"

# C: Verify that transaction completed
with db.readable() as group:
    assert("table1" in group)

    t = group["table1"] # get table

    assert(len(t) == 2)
    assert(t[0].name == "joe")
# COMMENTS ON SECTION C
# C1: why do I call a function on db here, but not in the B section? Seem inconsistent.
# C2: Strange that 'group' works with 'in' operator and looks like a dict, but is still not iterable? 
#   That is: 'for e in group:' should work... Might not be useful, but it's strange that it doesn't work

# D: One more change
with db.writable("table1") as t:
    t[0].age += 1
# COMMENTS ON SECTION D
# D1: Again inconsistency. Why does writable take an argument, when readable didn't?

# E: Verify changes
with db.readable("table1") as t:
    assert(t[0].age == 43)
    
    # do a query
    view = t.where().hired.isTrue().find_all();
    assert(view[0].name == "jessica")
# COMMENTS ON SECTION E
# E1: Now I'm really confused. 'readble' seems unreasonably overloaded. The same function returns either a group or a table?
#   That is not so intuitive...

# CONCLUSION:
# I think the tightdb concepts are too many and too complex (based on Python extension only). 
# Main take-aways: 
# - The extension should support more ways to write Python (not just one)
# - Not introduce so many concepts (databases, sharedgroups, table, array, dict), to do so relatively little. 
# - Be more consistent. If it looks iterable, it should be iterable (in, key-index, but no for-loops?).

# PLEASE REMEMBER: These are my rookie-rookie-first-10-minutes comments. 
# But the first 10 minutes of a programmer trying a library are often make or break, right?


```