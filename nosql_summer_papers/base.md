# BASE: an Acid Alternative

http://nosqlsummer.org/paper/base-vs-acid

Status: Read summary (Feb 7 2013)

[Full paper](http://portal.acm.org/ft_gateway.cfm?id=1394128&type=pdf)

Relates to: [Eventually Consistent](http://nosqlsummer.org/paper/eventually-consistent)

## Summary

> The acronym is a bit contrived

BASE = *Basically Available, Soft state*

In partitioned databases, trading some consistency for availability can lead to dramatic improvements in scalability.

[What does 'soft-state' in BASE mean?](http://stackoverflow.com/questions/4851242/what-does-soft-state-in-base-mean):

> There's (another) explanation at [stackoverflow.com/questions/3342497...](http://stackoverflow.com/questions/3342497/explanation-of-base-terminology) suggesting that soft-state means that the system will **change state without user intervention due to eventual consistency** (but then the soft-state part of the acronym is redundant)

I personally agree with this (eventually consistent) definition. The other one explanation (that data must be refresh or it is deleted) doesn't make any sense at all!
