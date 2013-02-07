# Eventually Consistent

http://nosqlsummer.org/paper/eventually-consistent

[Full paper](http://portal.acm.org/ft_gateway.cfm?id=1466448&type=pdf)

Related:

* Google Spanner

## Summary

Building reliable distributed systems at a worldwide scale demands trade-offs — between consistency and availability.
At the foundation of Amazon’s cloud computing are infrastructure services such as Amazon’s S3 (Simple Storage Service), SimpleDB, and EC2 (Elastic Compute Cloud) that provide the resources for constructing Internet-scale comput- ing platforms and a great variety of applications. The requirements placed on these infrastructure services are very strict; they need to score high marks in the areas of security, scalability, availability, performance, and cost effectiveness, and they need to meet these requirements while serving millions of customers around the globe, continuously.

Under the covers these services are massive distributed systems that operate on a worldwide scale. This scale creates additional challenges, because when a system processes trillions and trillions of requests, events that normally have a low probability of occurrence are now guaranteed to happen and need to be accounted for up front in the design and architecture of the system. Given the worldwide scope of these systems, we use replication techniques ubiquitously to guarantee consistent performance and high availability. **Although replication brings us closer to our goals, it cannot achieve them in a perfectly transparent manner; under a number of conditions the customers of these services will be confronted with the consequences of using replication techniques inside the services**.

One of the ways in which this manifests itself is in the type of data consistency that is provided, particularly when many widespread distributed systems provide an eventual consistency model in the context of data replication. When designing these large-scale systems at Amazon, we use a set of guiding principles and abstractions related to large-scale data replication and focus on the trade-offs between high availability and data consistency. In this article I present some of the relevant background that has informed our approach to delivering reliable distributed systems that need to operate on a global scale. An earlier version of this text appeared as a posting on the All Things Distributed weblog and was greatly improved with the help of its readers.