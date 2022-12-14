```
Step to solve High Level Design Questions

1. Requirement Gathering

    A. Functional requirement gathering(eg. Book car, Make payment, etc)
    	- Define scope of your system
	    - Decide on minimum viable product

    B. Non-Functional requirement (Consistency, availability, ease of use, performance, scalability, maintainability)
        1. Consistent or Highly Available?
        2. Read and write latency?

2. Estimation of scale(Include replication factor and autoscaling in mind while estimating)
            -Traffic estimation(Read QPS, Write QPS)
            -Capacity/Storage estimation(Persistence storage)
            -Bandwidth estimation
            -How many App-server, storage-server and caches etc required

3. Trade Off
    A. CAP and PACELC
        -CAP (Consistency, Availability, Partitioning)
        -PACELC(If Partition then tradeoff btw Availability and Consistency Else tradeoff btw Latency and Consistency)
    B. Read and Write Latency

    NOTE: For Read queries CP or AP
          For Write queries CP or AP

4. Architecture deep-dive
    A. System API
    B. Database Schema
    C. Database sharding mechanism(sharding-key)
    D. Caching mechanism
            -Which cache to use : App-cache, Global cache, Client-cache
		    -Decide cache writing policy : Write-around, Write-through, Write-back
		    -Global Cache and Write-around cache policy
    E.Component Design: List down all services in you system
    F.Draw hld diagram to show communication btw different services and component
```