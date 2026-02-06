# Short Polling

## Server Side

**1. Start Server**
`python server.py`

**2. Create EC2 Instance**

`curl http://127.0.0.1:5000/create_ec2/1`
```
{
  "instance_id": "1",
  "message": "EC2 instance started"
}
```
**3. Get status**

`curl http://127.0.0.1:5000/get_status/1`

```
{
  "instance_id": "1",
  "status": "RUNNING"
}
```

## Client Side
`python short_poll_client.py`

```
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  INITIALIZING
Polling again in 2 seconds...
STATUS:  ALLOCATING_RESOURCES
Polling again in 2 seconds...
STATUS:  ALLOCATING_RESOURCES
Polling again in 2 seconds...
STATUS:  ALLOCATING_RESOURCES
Polling again in 2 seconds...
STATUS:  ALLOCATING_RESOURCES
Polling again in 2 seconds...
STATUS:  ALLOCATING_RESOURCES
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  BOOTING_INSTANCE
Polling again in 2 seconds...
STATUS:  RUNNING
Instance is running. Stop Polling.
```