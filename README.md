Seth individual reflection: parallel sorting algorithm

I noticed that splitting the data into 4 parts and sorting them at the same time was faster for large datasets but slower for small ones. 

Hans individual reflection: sequential searching algorithm

I saw that linear search becomes slower because it examines each element individually. I learned from this that sequential searching
is straightforward, however it is ineffective for big data.

Keith individual reflection: Sequential sorting algorithm

I noticed that as the data gets larger it gets slower. The difference between small and large datasets was very clear since sorting 1,000 elements was almost instant while sorting 1,000,000 elements took much longer. There was no overhead from synchronization or process management since everything runs in one process. This made me realize that sequential sorting is simple but has limits when dealing with large data.

Gian individual reflection: Parallel Searching Algorithm

I noticed that searching through each element one by one gets slower as the data gets larger. Dividing the data into 4 parts and searching them at the same time helped reduce the time for large datasets. One challenge was making sure the correct global index was returned after all processes finished. I learned that parallel searching is useful for large data but the overhead makes it slower than sequential search for small datasets.


