## Reliable, scalable and maintainable applications
Many applications today are **data-intensive**, as opposed to **compute-intensive**.

??? info "How to measure intensiveness?"

    - Amount of data.
    - Complexity of data.
    - Speed of change.

### Reliability
The system should work correctly even in the face of adversity.

??? info "Faults vs Failure"
    - **Fault**: one component of the system deviating from its spec.
    - **Failure**: the whole system stops providing required services.

- **Hardware faults** happen all the time when you have a lot of machines.
Add **redundancy**.
- **Software errors**: different from hardware faults, software errors are usually correlated across nodes.
- **Human errors**. Humans are the weakest link in many systems.

??? note "Improve fault-tolerance by introducing faults"
    In fault-tolerant systems, it may make sense to deliberately introduce faults **on production**. E.g. [Netflix Chaos Monkey](https://github.com/Netflix/chaosmonkey).
    >Exposing engineers to failures more frequently incentivizes them to build resilient services.

### Scalability
#### Describing load
Load parameters are different depending on the specific system.
Generally we need to consider:

- Request per second.
- Ratio of read and write.
- The bottleneck may be dominated by a small number of extreme cases. E.g. celebrities on twitter have millions of followers, while the average may be less than one hundred.

#### Describing performance

- **Throughput**: the number of records we can process per second
- **Latency**: how fast the system can respond to clients.

??? note "Latency vs Response time"
    - **Latency** is the duration that a request is waiting to be handled.
    - **Response time** is what clients see: the time between a client sending a request and receiving response, including network delay, queueing delay and processing time.

??? note "Tail latency"
    - Since latency varies a lot even for similar requests, we need to think latency as a **distribution** instead of a single number.
    - We often care about **99.9th percentile latency** because it directly affects users' experience.
    - 99.99th percentile latency is often too expensive to improve.

### Maintainability
Majority of the cost of software is not in its initial development, but in its ongoing maintenance.

??? info "How to measure maintenance?"
    - Operability
    - Simplicity
    - Evolvability
    - Beginner friendliness

## Data models and query languages
Data models have a profound effect on how we think about the problems that we are solving.