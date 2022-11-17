gate mechanism: create threads, synchronize by waiting until all threads to finish before next iteration

javac *.java && java SSSP -a 0 -t 5 -n 50 && rm -rf *.class
=======
javac *.java
SSSP -a 3 -n 12


For this assignment, we are trying to solve the shortest path problem concurrently
Step 1: create a graph with random weights
    in this step, we are trying to 
Step 2: create a thread for each node


register with the Coordinator
set up my own bucket array
while there are any nonempty buckets
      while current bucket is nonempty
            identify light and heavy relaxations associated with vertices in current bucket
            clear my current bucket
            identify which light relaxations belong to other threads; enqueue Requests for them in the appropriate queues
            perform all the light relaxations that belong to me; remember the heavy relaxations
            barrier; if nobody sent anybody any requests then exit inner loop
            while my incoming Request queue is nonempty
                  take a request out of the queue and do the specified relaxation(s)
            barrier; if nobody has anything left in their current bucket then exit inner loop
      identify which remembered heavy relaxations belong to other threads; enqueue them in the appropriate queues
      perform all the remembered heavy relaxations that belong to me
      barrier
      while my incoming Request queue is nonempty
            take a request out of the queue and do the specified relaxation(s)
      repeat
            move to next bucket
            barrier; if nobody has anything in their bucket and we've gone all the way around the array then break outer loop
      until bucket is nonempty
unregister with the Coordinator