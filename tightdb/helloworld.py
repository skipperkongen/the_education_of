import tightdb

db = tightdb.SharedGroup("shared_db.tightdb")
if not db.is_valid():
    print "Could not open group"

# Do a write transaction
with db as group:
    # add a single table with two initial rows
    t = group.create_table('table1', ["name",  "string",
                                      "age",   "int",
                                      "hired", "bool"],
                           [["joe",     42, False], # initial rows
                            ["jessica", 22, True]])


# Verify that transaction completed
with db.readable() as group:
    assert("table1" in group)

    t = group["table1"] # get table

    assert(len(t) == 2)
    assert(t[0].name == "joe")